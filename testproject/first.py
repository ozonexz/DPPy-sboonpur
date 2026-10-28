"""Income-Expense Tracker - terminal app (beginner level)

Covers: menu + user input, data structure (list of dict), conditional logic,
loops, functions, input validation, error handling, file I/O (JSON).
"""

import json
from datetime import datetime

DATA_FILE = "records.json"


# ---------- File handling ----------
def load_records():
    """Load records from JSON file. Return empty list if missing/corrupted."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Data file is corrupted. Starting with empty records.")
        return []


def save_records(records):
    """Save records to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print("Data saved.")
    except OSError as e:
        print(f"Could not save data: {e}")


# ---------- Input helpers (validation) ----------
def get_int(prompt, min_v, max_v):
    while True:
        try:
            n = int(input(prompt))
            if min_v <= n <= max_v:
                return n
            print(f"Please enter a number between {min_v} and {max_v}.")
        except ValueError:
            print("Invalid input. Numbers only.")


def get_amount(prompt, allow_blank=False):
    """Return positive float. If allow_blank and input empty, return None."""
    while True:
        text = input(prompt).strip()
        if allow_blank and text == "":
            return None
        try:
            value = float(text)
            if value <= 0:
                print("Amount must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_text(prompt, allow_blank=False):
    while True:
        text = input(prompt).strip()
        if text or allow_blank:
            return text
        print("This field cannot be empty.")


def get_date(prompt, allow_blank=False):
    """Return date string YYYY-MM-DD. Blank = today (or None when editing)."""
    while True:
        text = input(prompt).strip()
        if text == "":
            return None if allow_blank else datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date. Use format YYYY-MM-DD (e.g. 2026-10-28).")


def get_type(prompt, allow_blank=False):
    while True:
        text = input(prompt).strip().lower()
        if allow_blank and text == "":
            return None
        if text in ("1", "income"):
            return "income"
        if text in ("2", "expense"):
            return "expense"
        print("Enter 1 (income) or 2 (expense).")


def find_record(records, record_id):
    for r in records:
        if r["id"] == record_id:
            return r
    return None


# ---------- Display ----------
def print_table(rows):
    if not rows:
        print("No records found.")
        return
    print(f"\n{'ID':<4} {'Date':<11} {'Type':<8} {'Category':<15} {'Amount':>12}")
    print("-" * 54)
    for r in rows:
        print(f"{r['id']:<4} {r['date']:<11} {r['type']:<8} "
              f"{r['category']:<15} {r['amount']:>12,.2f}")
    print("-" * 54)


def calc_totals(rows):
    income = sum(r["amount"] for r in rows if r["type"] == "income")
    expense = sum(r["amount"] for r in rows if r["type"] == "expense")
    return income, expense, income - expense


def print_totals(rows):
    income, expense, balance = calc_totals(rows)
    print(f"Total income : {income:>12,.2f}")
    print(f"Total expense: {expense:>12,.2f}")
    print(f"Balance      : {balance:>12,.2f}")


# ---------- Menu functions ----------
def show_menu():
    print("\n===== INCOME-EXPENSE TRACKER =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Search and Summary")
    print("5. Exit")


def add_record(records):
    print("\n--- Add Record ---")
    date = get_date("Date (YYYY-MM-DD, Enter = today): ")
    rec_type = get_type("Type (1 = income, 2 = expense): ")
    category = get_text("Category (e.g. food, salary, travel): ").lower()
    amount = get_amount("Amount: ")
    new_id = max((r["id"] for r in records), default=0) + 1
    records.append({"id": new_id, "date": date, "type": rec_type,
                    "category": category, "amount": amount})
    print("Record added successfully!")


def view_records(records):
    print("\n--- All Records ---")
    print_table(sorted(records, key=lambda r: (r["date"], r["id"])))
    if records:
        print_totals(records)


def update_record(records):
    print("\n--- Update Record ---")
    if not records:
        print("No records to update.")
        return
    print_table(records)
    record_id = get_int("Enter record ID: ", 1, max(r["id"] for r in records))
    record = find_record(records, record_id)
    if record is None:
        print("Record ID not found.")
        return

    print("1. Edit  2. Delete  3. Cancel")
    action = get_int("Choose: ", 1, 3)

    if action == 1:
        print("Press Enter to keep the current value.")
        date = get_date(f"Date [{record['date']}]: ", allow_blank=True)
        rec_type = get_type(f"Type 1/2 [{record['type']}]: ", allow_blank=True)
        category = get_text(f"Category [{record['category']}]: ", allow_blank=True)
        amount = get_amount(f"Amount [{record['amount']}]: ", allow_blank=True)
        if date:
            record["date"] = date
        if rec_type:
            record["type"] = rec_type
        if category:
            record["category"] = category.lower()
        if amount is not None:
            record["amount"] = amount
        print("Record updated successfully!")
    elif action == 2:
        confirm = input("Delete this record? (y/n): ").strip().lower()
        if confirm == "y":
            records.remove(record)
            print("Record deleted.")
        else:
            print("Cancelled.")
    else:
        print("Cancelled.")


def search_summary(records):
    print("\n--- Search and Summary ---")
    if not records:
        print("No records yet.")
        return
    print("1. Search by category")
    print("2. Search by month")
    print("3. Overall summary")
    choice = get_int("Choose: ", 1, 3)

    if choice == 1:
        keyword = get_text("Category: ").lower()
        matches = [r for r in records if keyword in r["category"]]
        print(f"Matching records: {len(matches)}")
        print_table(matches)
        if matches:
            print_totals(matches)

    elif choice == 2:
        while True:
            month = input("Month (YYYY-MM): ").strip()
            try:
                datetime.strptime(month, "%Y-%m")
                break
            except ValueError:
                print("Invalid month. Use format YYYY-MM (e.g. 2026-10).")
        matches = [r for r in records if r["date"].startswith(month)]
        print(f"Matching records: {len(matches)}")
        print_table(matches)
        if matches:
            print_totals(matches)

    else:
        print_totals(records)
        by_category = {}
        for r in records:
            if r["type"] == "expense":
                by_category[r["category"]] = by_category.get(r["category"], 0) + r["amount"]
        if by_category:
            print("\nExpenses by category:")
            for cat, total in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
                print(f"  {cat:<15} {total:>12,.2f}")


# ---------- Main ----------
def main():
    records = load_records()
    while True:
        show_menu()
        choice = get_int("Choose: ", 1, 5)
        if choice == 1:
            add_record(records)
        elif choice == 2:
            view_records(records)
        elif choice == 3:
            update_record(records)
        elif choice == 4:
            search_summary(records)
        else:
            save_records(records)
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
