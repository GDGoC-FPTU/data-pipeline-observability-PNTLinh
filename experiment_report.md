# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** 2A202600216
**Name:** Nguyễn Thùy Linh
**Date:** 15/04/2026

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent: Based on my data, the best choice is Laptop at $1200. | 10 | Dữ liệu chuẩn hóa, giá cả hợp lý, logic chọn sản phẩm chính xác.|
| Garbage Data (`garbage_data.csv`) | Agent: Based on my data, the best choice is Nuclear Reactor at $999999 | 2 | Agent bị đánh lừa bởi các giá trị cực đoan (outliers) và dữ liệu phi thực tế.|

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

(Viet nhan xet cua ban o day — it nhat 50 tu)

(Hay phan tich cac van de nhu Duplicate IDs, wrong data types, outliers, null values
va giai thich tai sao chung anh huong den ket qua cua Agent.)

Việc Agent đưa ra phản hồi sai lệch khi sử dụng garbage_data.csv xuất phát từ nhiều vấn đề nghiêm trọng về chất lượng dữ liệu:

Wrong Data Types (Sai kiểu dữ liệu): Ở dòng số 4, giá của "Broken Chair" là chuỗi văn bản "ten dollars" thay vì số. Điều này khiến mô hình AI không thể thực hiện các phép toán so sánh hoặc tính toán giá trị trung bình.

Outliers (Giá trị ngoại lai): Sự xuất hiện của "Nuclear Reactor" với giá $999999 là một ví dụ điển hình về nhiễu. Trong một danh sách mua sắm thông thường, giá trị quá lớn này làm lệch hoàn toàn logic gợi ý của Agent.

Duplicate IDs & Null Values: Việc trùng ID (Laptop và Banana cùng ID là 1) và dòng cuối cùng bị trống thông tin (Ghost Item, 0) gây ra sự không nhất quán về mặt logic (Inconsistency).

Thiếu chuẩn hóa: Category không được viết hoa đồng nhất (electronics vs Electronics) làm suy giảm khả năng phân loại và lọc dữ liệu của Agent.

Khi dữ liệu đầu vào là "rác" (Garbage In), Agent dù thông minh đến đâu cũng sẽ trích xuất thông tin sai (Garbage Out), dẫn đến việc đưa ra các quyết định phi thực tế như khuyên người dùng mua lò phản ứng hạt nhân thay vì laptop.
## 3. Ket luan

**Quality Data > Quality Prompt?** (Dong y hay khong? Giai thich ngan gon.)

(Viet ket luan cua ban o day)
Đồng ý. Mặc dù một Prompt tốt giúp Agent hiểu nhiệm vụ, nhưng Dữ liệu chất lượng mới là nền tảng của tri thức. Nếu dữ liệu sai lệch, Prompt dù tinh vi đến đâu cũng chỉ giúp Agent "trình bày sự sai lệch đó một cách trôi chảy hơn". Trong thực tế triển khai các hệ thống RAG hay AI Agent như mình đang làm tại BKAI, việc làm sạch dữ liệu (Preprocessing) luôn chiếm 80% nỗ lực để đảm bảo tính tin cậy của hệ thống.