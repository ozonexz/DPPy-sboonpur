# main.py
data = []  # ใช้ list เก็บ dict ตามเกณฑ์

# Function 1: คำนวณเงินคงเหลือ (มี param + มี return)
def get_balance(items):
    money = 0
    for x in items:
        if x["type"] == "in":
            money += x["amount"]
        else:
            money -= x["amount"]
    return money

# Function 2: เพิ่มรายการ (มี param)
def add_item(name, cat, t_type, amount):
    data.append({"name": name, "cat": cat, "type": t_type, "amount": amount})
    print(" บันทึกแล้ว!")

# Function 3: แสดงรายการทั้งหมด
def show_all():
    if not data:
        print(" ยังไม่มีข้อมูล")
        return
    for i, x in enumerate(data, 1):
        t = "รายรับ" if x["type"] == "in" else "รายจ่าย"
        print(f"{i}. {x['name']} ({x['cat']}) - {t} {x['amount']} บาท")

# Function 4: ลบรายการ[cite: 4, 5]
def delete_item():
    show_all()
    num = input("ใส่ลำดับที่ต้องการลบ: ")
    if num.isdigit() and 1 <= int(num) <= len(data):
        deleted = data.pop(int(num) - 1)
        print(f" ลบ '{deleted['name']}' แล้ว")
    else:
        print(" ลำดับไม่ถูกต้อง")

# Function 5: ค้นหาและคำนวณยอดรวม (Algorithm)[cite: 5]
def search_cat():
    keyword = input("ใส่หมวดหมู่ที่ต้องการค้นหา: ")
    total = 0
    found = 0
    for x in data:
        if keyword in x["cat"]:
            print(f"- {x['name']}: {x['amount']} บาท")
            total += x["amount"]
            found += 1
    print(f"เจอ {found} รายการ | รวม: {total} บาท")

# Main Loop & Menu (Interactive Menu 4 ตัวเลือก + 1 ออก)[cite: 4]
while True:
    bal = get_balance(data)
    print(f"\n💰 ยอดเงินคงเหลือ: {bal} บาท")
    print("1. บันทึก   2. ดูประวัติ   3. ลบรายการ   4. ค้นหาหมวดหมู่   5. ออก")
    
    choice = input("เลือกเมนู (1-5): ")

    if choice == "1":
        name = input("ชื่อรายการ: ").strip()
        # Rule 1: ชื่อห้ามว่างเปล่า[cite: 5]
        if not name:
            print(" ชื่อห้ามว่าง"); continue

        cat = input("หมวดหมู่: ").strip() or "ทั่วไป"
        t_type = input("ประเภท (in/out): ").strip().lower()
        if t_type not in ["in", "out"]:
            print(" เลือกเฉพาะ in หรือ out"); continue

        try:
            amt = float(input("จำนวนเงิน: "))
        except ValueError:
            print(" ต้องเป็นตัวเลขเท่านั้น"); continue  # ป้องกันโปรแกรม crash[cite: 3, 6]

        # Rule 2: เงินต้องมากกว่า 0[cite: 5, 6]
        if amt <= 0:
            print(" จำนวนเงินต้องมากกว่า 0"); continue

        # Rule 3: เงินต้องพอจ่าย[cite: 5]
        if t_type == "out" and amt > bal:
            print(f" เงินไม่พอ! มีแค่ {bal} บาท"); continue

        add_item(name, cat, t_type, amt)

    elif choice == "2":
        show_all()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        search_cat()
    elif choice == "5":
        print(" บ๊ายบาย!"); break
    else:
        print(" เลือก 1-5 เท่านั้น")

