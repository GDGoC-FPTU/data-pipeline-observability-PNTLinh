import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.

    Goi y:
       - Dung json.load() de doc file JSON
       - Xu ly truong hop file khong ton tai (FileNotFoundError)

    Returns:
        list: Danh sach cac records (dictionaries)
    """
    print(f"Extracting data from {file_path}...")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print(f"Successfully extracted {len(data)} records")
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Quy tac validation:
       - Price phai > 0 (loai bo gia am hoac bang 0)
       - Category khong duoc rong

    Goi y:
       - Dung record.get('price', 0) de lay gia
       - Dung record.get('category') de kiem tra category
       - In ra so luong record hop le va khong hop le

    Returns:
        list: Danh sach cac records hop le
    """
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price', 0)
        category = record.get('category', '')
        
        # Check if price is valid (> 0) and category is not empty
        if price > 0 and category and str(category).strip():
            valid_records.append(record)
        else:
            error_count += 1
            if price <= 0:
                print(f"    Record {record.get('id')} rejected: Invalid price ({price})")
            if not category or not str(category).strip():
                print(f"    Record {record.get('id')} rejected: Empty category")

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.

    Yeu cau:
       - Tinh discounted_price = price * 0.9 (giam 10%)
       - Chuan hoa category thanh Title Case (vi du: "electronics" -> "Electronics")
       - Them cot processed_at = timestamp hien tai

    Goi y:
       - Dung pd.DataFrame(data) de tao DataFrame
       - df['discounted_price'] = df['price'] * 0.9
       - df['category'] = df['category'].str.title()
       - df['processed_at'] = datetime.datetime.now().isoformat()

    Returns:
        pd.DataFrame: DataFrame da duoc transform
    """
    if not data:
        return None
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Calculate discounted price (10% discount)
    df['discounted_price'] = df['price'] * 0.9
    
    # Normalize category to Title Case
    df['category'] = df['category'].str.title()
    
    # Add processed_at timestamp
    df['processed_at'] = datetime.datetime.now().isoformat()
    
    print(f"Transform complete. {len(df)} records processed")
    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.

    Goi y:
       - df.to_csv(output_path, index=False)
    """
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")
