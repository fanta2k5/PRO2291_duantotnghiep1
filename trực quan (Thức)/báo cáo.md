# BÁO CÁO CÂU CHUYỆN DỮ LIỆU & Ý NGHĨA HỆ THỐNG DASHBOARD
**Môn học:** Dự Án Tốt Nghiệp (PRO2291)  
**Sinh viên thực hiện:** Nguyễn Hữu Thức  
**Trường:** FPT Polytechnic (Ho Chi Minh City)  

---

## PHẦN LỜI MỞ ĐẦU: ĐẶT VẤN ĐỀ (CONTEXT)
Trong kỷ nguyên số, dữ liệu thô (Raw data) của một doanh nghiệp bán lẻ và thương mại điện tử giống như một mỏ quặng chưa được khai phá. Nếu chỉ nhìn vào những con số rời rạc, ban giám đốc không thể đưa ra quyết định chiến lược chính xác. 

Dự án này thực hiện quy trình chuẩn hóa dữ liệu xuyên suốt từ khâu làm sạch dữ liệu thô (**Raw**), xử lý ngoại lệ (**Cleaned**), tổ chức lưu trữ theo mô hình Star Schema (**Dim & Fact**) cho đến việc tổng hợp dữ liệu thương mại (**Aggregates**). Mục tiêu cuối cùng là xây dựng hệ thống **02 Dashboard phân tích chuyên sâu** nhằm trả lời hai câu hỏi lớn mang tính sống còn của doanh nghiệp:
1. **Dòng tiền đang chảy như thế nào và đâu là cốt lõi tăng trưởng tài chính?** (Dashboard 1)
2. **Ai là người đang nuôi sống doanh nghiệp và họ tập trung ở đâu?** (Dashboard 2)

---

## DASHBOARD 1: TỔNG QUAN HOẠT ĐỘNG KINH DOANH & DOANH THU

### 1. Mục đích của các biểu đồ cấu thành
Hệ thống đồ thị trong Dashboard 1 được lựa chọn để bóc tách bài toán tài chính từ tổng quan (Thời gian) đến chi tiết (Sản phẩm/Địa lý):

* **Biểu đồ 1 - Xu hướng doanh thu theo từng tháng (Line Chart):** Dùng biểu đồ đường kết hợp các điểm nút dữ liệu (`marker='o'`) nhằm giúp người xem nhận diện ngay lập tức sự biến động của dòng tiền theo dòng thời gian. Mục đích chính là tìm ra **tính chu kỳ, mùa vụ** của hoạt động kinh doanh.
* **Biểu đồ 2 - Cơ cấu doanh thu theo Danh mục sản phẩm (Horizontal Bar Chart):** Biểu đồ cột ngang sắp xếp giảm dần giúp phân loại rõ ràng sức nặng doanh số của từng nhóm ngành hàng. Tránh việc doanh nghiệp dàn trải nguồn lực vào những ngành hàng kém hiệu quả.
* **Biểu đồ 3 - Phân bổ doanh thu theo Vùng địa lý (Vertical Bar Chart):** Sử dụng dải màu tương phản (`coolwarm`) để thể hiện độ nóng/lạnh của sức mua tại 4 vùng chiến lược lớn (South, Midwest, West, Northeast).
* **Biểu đồ 4 - Top 10 mã sản phẩm mang lại doanh thu cao nhất (Horizontal Bar Chart):** Đi sâu vào cấp độ phân tử của dữ liệu (mã SKU). Biểu đồ giúp định danh chính xác những "Key Product" gánh vác phần lớn doanh thu cho công ty.

---

### Câu chuyện dữ liệu (Data Story) của Dashboard 1

> **"Dòng chảy tài chính và Hiệu ứng mùa vụ bùng nổ"**

Bức tranh tài chính của doanh nghiệp mở ra một con số vô cùng ấn tượng: **Tổng doanh thu toàn doanh nghiệp đạt ngưỡng gần 500 triệu USD**. Tuy nhiên, dòng chảy này không hề bình lặng mà biến động dữ dội theo thời gian.

**Điểm thắt nút đầu tiên** nằm ở biểu đồ xu hướng tháng. Dữ liệu chỉ ra một sự tăng trưởng mang tính "đột biến" vào **tháng 12 năm 2020** khi doanh thu chạm đỉnh lịch sử (gần **$139.3M**), gấp hơn 10 lần so với các tháng bình thường khác như tháng 1 hay tháng 2 năm 2021 (chỉ lẹt đẹt quanh mức **$10M - $14M**). 
* *Insight:* Đây là minh chứng rõ nét của **hiệu ứng mùa vụ lễ hội cuối năm (Mega Sale/Giáng Sinh)**. Khách hàng có xu hướng bùng nổ chi tiêu vào tháng 12 và thắt chặt hầu bao ngay sau Tết (tháng 1, tháng 2).

**Nguyên nhân của sự bùng nổ này là gì?** Khi nhìn sang biểu đồ cơ cấu danh mục, câu trả lời đã lộ diện. Ngành hàng **Mobiles & Tablets** chính là "long mạch" của công ty khi chiếm vị trí độc tôn với **$280.3M** (chiếm hơn một nửa tổng doanh thu), theo sau là đồ điện tử gia dụng (**Appliances** với **$72.0M**). 
* *Insight:* Doanh nghiệp đang phụ thuộc rất lớn vào các thiết bị công nghệ giá trị cao. Các hãng công nghệ thường tung ra dòng sản phẩm mới hoặc giảm giá sâu vào cuối năm, kết hợp với nhu cầu mua sắm tự thưởng của người dùng tạo nên cú hích doanh thu cho nhóm ngành này vào tháng 12.

**Dòng tiền này chảy về đâu nhiều nhất?** Biểu đồ phân bổ vùng miền chỉ ra **Vùng South (Miền Nam)** là thị trường cốt lõi, mang về tới **$189.5M**, bỏ xa các khu vực còn lại. Đồng thời, doanh nghiệp cần chú ý đặc biệt đến nhóm **Top 10 sản phẩm (SKU)**, nổi bật là mã `matsam59db757fb47a2` khi một mình nó tự mang về **$14.6M** cho công ty.

---

## DASHBOARD 2: CHÂN DUNG KHÁCH HÀNG & PHÂN KHÚC THỊ TRƯỜNG

### 1. Mục đích của các biểu đồ cấu thành
Dashboard 2 chuyển dịch góc nhìn từ "Tiền" sang "Con người" bằng phương pháp khớp nối dữ liệu (Merge Data):

* **Biểu đồ 1 - Tỷ lệ đóng góp doanh thu theo Giới tính (Pie Chart):** Giúp xác định nhanh xem sản phẩm của công ty phù hợp với nam hay nữ, từ đó định hình phong cách thiết kế hình ảnh và thông điệp truyền thông.
* **Biểu đồ 2 - Doanh thu theo phân khúc độ tuổi (Vertical Bar Chart):** Chia nhỏ khách hàng thành các nhóm tuổi sinh học. Mục đích là tìm ra phân khúc khách hàng mục tiêu (Target Customer) có giá trị cao nhất.
* **Biểu đồ 3 - So sánh doanh thu giữa Khách hàng mới và Khách hàng cũ (Vertical Bar Chart):** Đây là thước đo sức khỏe của doanh nghiệp, giúp đánh giá hiệu quả giữa đội ngũ Marketing (kiếm khách hàng mới) và đội ngũ CRM/Chăm sóc khách hàng (giữ chân khách hàng cũ).
* **Biểu đồ 4 - Top 10 Thành phố đạt doanh thu cao nhất (Horizontal Bar Chart):** Cụ thể hóa dữ liệu địa lý từ cấp "Vùng" xuống cấp "Thành phố" để tối ưu hóa bài toán Logistics, kho bãi và giao hàng.

---

### Câu chuyện dữ liệu (Data Story) của Dashboard 2

> **"Chân dung khách hàng trưởng thành và Sức mạnh của lòng trung thành"**

Sau khi biết được tiền đến từ đâu, chúng ta đi tìm câu trả lời cho câu hỏi: **Ai là người đã chi trả lượng ngân sách khổng lồ đó?**

Đầu tiên, doanh nghiệp có một tệp khách hàng rất văn minh và cân bằng. Biểu đồ tròn cho thấy tỷ lệ đóng góp doanh thu giữa **Nam và Nữ gần như là tuyệt đối cân bằng (Ví dụ: ~50% mỗi bên)**. 
* *Insight:* Sản phẩm của chúng ta có tính đại chúng cao, không bị thiên vị giới tính. Do đó, các chiến dịch Marketing đại chúng (Mass Marketing) sẽ mang lại hiệu quả tối ưu hơn là việc cố gắng cá nhân hóa theo giới tính.

**Tuy nhiên, sự khác biệt xuất hiện rõ rệt ở độ tuổi.** Dữ liệu đập tan tư duy lối mòn rằng người trẻ sẽ mua sắm online nhiều nhất. Biểu đồ nhóm tuổi chứng minh nhóm **25-35 tuổi** và **36-45 tuổi** mới là "mỏ vàng" thực sự của doanh nghiệp khi đóng góp phần lớn doanh số. 
* *Insight:* Đây là tệp khách hàng độc lập về tài chính, có thu nhập ổn định và có nhu cầu mua sắm thực tế cho bản thân cũng như gia đình (đặc biệt thích hợp với nhóm hàng Mobiles và Appliances ở Dashboard 1).

**Điểm sáng đắt giá nhất của đồ án nằm ở biểu đồ Loại khách hàng (Customer Type).** Doanh thu đến từ khách hàng cũ quay lại (Repeated Customers) chiếm tỷ trọng áp đảo so với khách hàng mới.
* *Insight:* Doanh nghiệp đang có **chỉ số giữ chân khách hàng (Customer Retention Rate) cực kỳ tốt**. Việc chăm sóc khách hàng cũ đang phát huy tác dụng tối đa, giúp công ty duy trì nguồn thu bền vững mà không bị phụ thuộc quá nhiều vào chi phí chạy quảng cáo tìm khách hàng mới.

Cuối cùng, dòng chảy mua sắm này được định vị chính xác tại các **đầu tàu đô thị**. Biểu đồ Top 10 thành phố đã chỉ mặt đặt tên những đô thị có sức mua lớn nhất, giúp doanh nghiệp biết chính xác cần phải đặt kho hàng chặng cuối (Last-mile delivery) ở đâu để tối ưu chi phí vận chuyển.

---

## KẾT LUẬN CHIẾN LƯỢC (ACTIONABLE INSIGHTS)
Kết hợp mối tương quan giữa **Doanh thu (Dashboard 1)** và **Khách hàng (Dashboard 2)**, em xin đề xuất 2 giải pháp chiến lược cho doanh nghiệp:

1.  **Chiến lược Sản phẩm & Tồn kho:** Tập trung tối đa nguồn lực vào nhóm hàng cốt lõi (Mobiles & Tablets) và các mã sản phẩm Top 10. Do tính mùa vụ tháng 12 cực cao, doanh nghiệp bắt buộc phải lên kế hoạch gom hàng và chuẩn bị chuỗi cung ứng ngay từ tháng 10, tránh tình trạng đứt gãy hàng hóa lúc nhu cầu đạt đỉnh.
2.  **Chiến lược Khách hàng & Tiếp thị:** Do doanh thu phụ thuộc lớn vào khách hàng cũ thuộc độ tuổi 25-45, doanh nghiệp nên ngừng việc đốt tiền quảng cáo vô tội vạ cho khách hàng mới. Thay vào đó, hãy tái đầu tư ngân sách vào các **Chương trình khách hàng thân thiết (Loyalty Program)**, tặng voucher nâng cấp đời máy công nghệ cho tập khách hàng cũ tại các thành phố lớn ở vùng phía Nam nhằm tối ưu hóa giá trị vòng đời khách hàng (Customer Lifetime Value).