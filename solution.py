import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
# Sửa lỗi Syntax bằng cách thêm r phía trước đường dẫn
SOURCE_FILE = r'C:\Users\ngoch\Downloads\data-pipeline-observability-PNTLinh\raw_data.json'
OUTPUT_FILE = 'processed_data.csv'

def extract(file_path):
    print(f"Extracting data from {file_path}...")
    try:
        if not os.path.exists(file_path):
            print(f"Lỗi: Không tìm thấy file tại {file_path}")
            return None
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error during extraction: {e}")
        return None

def validate(data):
    # Đã xóa dòng print(file_path) gây lỗi NameError ở đây
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price', 0)
        category = record.get('category', "")
        
        if price > 0 and category and str(category).strip():
            valid_records.append(record)
        else:
            error_count += 1

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records

def transform(data):
    if not data: return None
    df = pd.DataFrame(data)
    df['discounted_price'] = df['price'] * 0.9
    df['category'] = df['category'].astype(str).str.title()
    df['processed_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df

def load(df, output_path):
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    raw_data = extract(SOURCE_FILE)
    if raw_data:
        clean_data = validate(raw_data)
        final_df = transform(clean_data)
        if final_df is not None:
            load(final_df, OUTPUT_FILE)