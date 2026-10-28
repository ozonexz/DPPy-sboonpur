# สมุดจดเงิน - เวอร์ชันง่ายที่สุด

records = []  # กล่องเก็บของ: แต่ละชิ้นคือ 1 รายการ (list ของ dict)


def show_menu():
    print("\n===== MY MONEY BOOK =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Search and Summary")
    print("5. Exit")


def add_record():
    name = input("What is it? (e.g. candy): ")
    if name == "":                       # ห้ามเว้นว่าง
        print("Name cannot be empty!")
        return
    try:
        amount = float(input("How much money? "))
    except ValueError:                   # พิมพ์ตัวอักษรมา
        print("Please type a number!")
        return
    if amount <= 0:                      # ห้ามติดลบ
        print("Money must be more than 0!")
        return
    kind = input("Money in or out? (in/out): ")
    if kind != "in" and kind != "out":
        print("Please type in or out only!")
        return
    records.append({"name": name, "amount": amount, "kind": kind})
    print("Record added successfully!")


def view_records():
    if len(records) == 0:
        print("Nothing here yet.")
    for number, r in enumerate(records, 1):   # วนดูทีละชิ้น
        print(number, r["name"], r["kind"], r["amount"])


def update_record():
    view_records()
    if len(records) == 0:
        return
    try:
        number = int(input("Which number to change? "))
        new_amount = float(input("New money amount: "))
        records[number - 1]["amount"] = new_amount
        print("Record updated!")
    except (ValueError, IndexError):     # พิมพ์ผิด หรือเลขไม่มีในกล่อง
        print("Oops, wrong input!")


def search_summary():
    word = input("Search word: ")
    count = 0
    for r in records:
        if word in r["name"]:
            print(r["name"], r["kind"], r["amount"])
            count = count + 1
    print("Matching records:", count)

    money_in = 0
    money_out = 0
    for r in records:
        if r["kind"] == "in":
            money_in = money_in + r["amount"]
        else:
            money_out = money_out + r["amount"]
    print("Money in :", money_in)
    print("Money out:", money_out)
    print("Money left:", money_in - money_out)


def main():
    while True:                          # วนเมนูไปเรื่อยๆ จนกด 5
        show_menu()
        choice = input("Choose: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            search_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1-5")


main()