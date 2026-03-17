#bài 1 
n = int(input("Nhập n: "))
print(n * 2)

#bài 2
a = float(input("Nhập chiều rộng a: "))
b = float(input("Nhập chiều dài b: "))

r = a / 2
s_hcn = a * b
s_tron = 3.14 * (r ** 2)
# s_con_lai = s_hcn - s_tron

# In kết quả lấy 2 chữ số thập phân
print(f"{s_con_lai:.2f}")

#bài 3
c = input("Nhập 1 ký tự: ")

if c.isupper():
    print(c.lower())
elif c.islower():
    print(c.upper())
else:
    print(c)

#bài 4
c = input("Nhập 1 ký tự: ")

if c.isalpha():
    print(f"{c} là kí tự alphabet")
else:
    print(f"{c} không phải là kí tự alphabet")

# bài 5
A = input("Nhập chữ cái hoa: ")

# Chuyển sang thường
a_thuong = A.lower()

if A == 'A':
    print('z') # Trường hợp đặc biệt
else:
    # ord() dùng để lấy mã ASCII, chr() để chuyển ngược lại từ mã sang ký tự
    lien_truoc = chr(ord(a_thuong) - 1)
    print(lien_truoc)

# bài 6
import math
a, b, c = map(int, input().split())
if a + b > c and  a + c > b and b + c > a :
p = (a+b+c)/2
s = math.sqrt (p*(p-a)*(p-b)*(p-c))
print (f"{s:.1f}")
else :
print("Khong phai 3 canh cua tam giac")

#bài 7
chuoi = input("Nhập chuỗi (độ dài >= 20): ")
print("Chữ cái thứ năm là:", chuoi[4])
print("Chữ cái thứ chín là:", chuoi[8])

#bài 8
def tinh_tien_dien():
    ten_chu_ho = input("Ten chu ho: ")
    chi_so_cu = int(input("Chi so thang truoc: "))
    chi_so_moi = int(input("Chi so thang nay: "))
    
    # 2. Tính tổng số điện tiêu thụ
    so_dien = chi_so_moi - chi_so_cu
    tien_chua_thue = 0
    # 3. Tính tiền theo từng bậc (Dùng cách bóc tách từ cao xuống thấp)
    if so_dien > 400:
        tien_chua_thue += (so_dien - 400) * 3460
        so_dien = 400
    if so_dien > 300:
        tien_chua_thue += (so_dien - 300) * 3350
        so_dien = 300
    if so_dien > 200:
        tien_chua_thue += (so_dien - 200) * 2998
        so_dien = 200
    if so_dien > 100:
        tien_chua_thue += (so_dien - 100) * 2380
        so_dien = 100
    if so_dien > 50:
        tien_chua_thue += (so_dien - 50) * 2050
        so_dien = 50
    if so_dien > 0:
        tien_chua_thue += so_dien * 1984

    # 4. Tính thuế VAT 8% dựa trên TỔNG TIỀN các bậc
    tong_tien_cuoi = tien_chua_thue * 1.08
    
    # Làm tròn đến đơn vị đồng theo yêu cầu đề bài
    ket_qua = round(tong_tien_cuoi)

    # 5. Xuất kết quả đúng định dạng mẫu
    print("-" * 20)
    print(f"Ho va ten: {ten_chu_ho}")
    print(f"Tien phai tra la: {ket_qua}")
tinh_tien_dien()
        

    
    


   

