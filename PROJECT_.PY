# EXPENSE, ATTENDANCE, GRADING AND BILLING MANAGEMENT SYSTEM
# Simple CLI project using basic Python concepts


students = {}       # Roll number is the unique key
expenses = []
bills = []


def get_int(message, low, high):
    while True:
        try:
            value = int(input(message))
            if low <= value <= high:
                return value
            print("Enter a value between", low, "and", high)
        except ValueError:
            print("Please enter a valid number from main menu.")
            print("kartik , 2601940007")


def get_float(message, low, high):
    while True:
        try:
            value = float(input(message))
            if low <= value <= high:
                return value
            print("Enter a value between", low, "and", high)
        except ValueError:
            print("Please enter a valid number.")
            print("kartik , 2601940007")


def add_student():
    roll = input("Enter student roll number: ").strip()

    if roll == "":
        print("Roll number cannot be empty.")
        print("kartik , 2601940007")
        return

    if roll in students:
        print("This roll number already exists.")
        print("kartik , 2601940007")
        return

    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        print("kartik , 2601940007")
        return

    students[roll] = {"name": name, "present": 0, "marks": []}
    print("Student registered successfully.")
    print("kartik , 2601940007")


def attendance():
    if len(students) == 0:
        print("Please register students first.")
        return

    total_days = get_int("Enter total working days: ", 1, 365)

    for roll in students:
        present = get_int(
            "Days present for " + students[roll]["name"] + " (" + roll + "): ",
            0, total_days
        )
        students[roll]["present"] = present
        print("kartik , 2601940007")

    eligible = 0
    warning = 0
    shortage = 0
    total_percentage = 0

    print("\nROLL NO.   NAME             ATTENDANCE     STATUS")
    print("-" * 55)

    for roll in students:
        name = students[roll]["name"]
        present = students[roll]["present"]
        percentage = (present / total_days) * 100
        total_percentage += percentage

        if percentage >= 75:
            status = "Eligible"
            eligible += 1

        elif percentage >= 60:
            status = "Warning"
            warning += 1
        else:
            status = "Shortage"
            shortage += 1

        print(f"{roll:<10} {name:<16} {percentage:>8.2f}%     {status}")
        print("kartik , 2601940007")

    average = total_percentage / len(students)
    print("-" * 55)
    print(f"Average attendance : {average:.2f}%")
    print("Eligible students  :", eligible)
    print("Warning students   :", warning)
    print("Shortage students  :", shortage)
    print("kartik , 2601940007")


def grade_student():
    if len(students) == 0:
        print("Please register students first.")
        return

    roll = input("Enter student roll number: ").strip()

    if roll not in students:
        print("Roll number not found. Register the student first.")
        return

    print("Enter marks of 5 subjects separated by spaces.")
    while True:
        try:
            marks = list(map(float, input("Enter 5 marks: ").split()))
            if len(marks) != 5:
                print("Please enter exactly 5 marks.")
            elif any(mark < 0 or mark > 100 for mark in marks):
                print("Marks must be between 0 and 100.")
            else:
                break
        except ValueError:
            print("Enter numbers only.")

    students[roll]["marks"] = marks

    total = sum(marks)
    average = total / 5
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 35:
        grade = "E"
    else:
        grade = "F"

    # A student fails if even one subject mark is below 35.
    passed = True
    for mark in marks:
        if mark < 35:
            passed = False

    if passed:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n========== REPORT CARD ==========")
    print("Roll Number :", roll)
    print("Student     :", students[roll]["name"])
    for i in range(5):
        print("Subject", i + 1, ":", f"{marks[i]:.2f}")
    print("---------------------------------")
    print(f"Total       : {total:.2f} / 500")
    print(f"Average     : {average:.2f}")
    print(f"Percentage  : {percentage:.2f}%")
    print("Grade       :", grade)
    print("Result      :", result)
    print("=================================")
    print("kartik , 2601940007")


def grading_summary():
    if len(students) == 0:
        print("No students registered.")
        return

    print("\nROLL NO.   NAME             TOTAL       GRADE    RESULT")
    print("-" * 65)

    pass_count = 0
    fail_count = 0
    total_class_percentage = 0
    graded_count = 0

    for roll in students:
        marks = students[roll]["marks"]

        if len(marks) == 5:
            total = sum(marks)
            percentage = (total / 500) * 100
            graded_count += 1
            total_class_percentage += percentage

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            elif percentage >= 35:
                grade = "E"
            else:
                grade = "F"

            passed = True
            for mark in marks:
                if mark < 35:
                    passed = False

            if passed:
                result = "PASS"
                pass_count += 1
            else:
                result = "FAIL"
                fail_count += 1

            print(f"{roll:<10} {students[roll]['name']:<16} "
                  f"{total:>7.2f}     {grade:<7} {result}")
        else:
            print(f"{roll:<10} {students[roll]['name']:<16} "
                  "Marks not entered")
            print("kartik , 2601940007")

    if graded_count > 0:
        print("-" * 65)
        print(f"Class average percentage: "
              f"{total_class_percentage / graded_count:.2f}%")
        print("Pass count:", pass_count)
        print("Fail count:", fail_count)
    else:
        print("No marks have been entered yet.")
        print("kartik , 2601940007")


def add_expense():
    description = input("Enter expense description: ").strip()
    category = input("Enter category (Food/Travel/Utilities/Stationery/Other): ").strip().title()

    categories = ["Food", "Travel", "Utilities", "Stationery", "Other"]
    if category not in categories:
        print("Invalid category.")
        return

    amount = get_float("Enter amount: ", 0.01, 100000000)
    expenses.append({"description": description, "category": category,
                     "amount": amount})
    print("Expense added successfully.")
    print("kartik , 2601940007")


def expense_summary():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    category_total = {
        "Food": 0, "Travel": 0, "Utilities": 0,
        "Stationery": 0, "Other": 0
    }
    grand_total = 0

    print("\nDESCRIPTION          CATEGORY        AMOUNT")
    print("-" * 50)
    for item in expenses:
        print(f"{item['description']:<20} {item['category']:<15} "
              f"{item['amount']:>8.2f}")
        category_total[item["category"]] += item["amount"]
        grand_total += item["amount"]

    print("-" * 50)
    for category in category_total:
        print(f"{category:<20} {category_total[category]:.2f}")
    print(f"GRAND TOTAL: {grand_total:.2f}")


def billing():
    customer = input("Enter customer name: ").strip()
    if customer == "":
        print("Customer name cannot be empty.")
        return

    items = []
    subtotal = 0

    while True:
        item_name = input("Enter item name (or done to finish): ").strip()
        if item_name.lower() == "done":
            break
        if item_name == "":
            print("Item name cannot be empty.")
            continue

        price = get_float("Enter unit price: ", 0.01, 100000000)
        quantity = get_int("Enter quantity: ", 1, 100000)

        line_total = price * quantity
        items.append((item_name, price, quantity, line_total))
        subtotal += line_total

    if len(items) == 0:
        print("No items added. Bill not created.")
        return

    if subtotal >= 10000:
        discount_rate = 0.15
    elif subtotal >= 5000:
        discount_rate = 0.10
    elif subtotal >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    taxable = subtotal - discount
    tax = taxable * 0.18
    grand_total = taxable + tax

    print("\n============== INVOICE ==============")
    print("Customer:", customer)
    print("-------------------------------------")
    print(f"{'Item':<15}{'Price':>9}{'Qty':>6}{'Total':>10}")
    for item_name, price, quantity, line_total in items:
        print(f"{item_name:<15}{price:>9.2f}{quantity:>6}{line_total:>10.2f}")
    print("-------------------------------------")
    print(f"Subtotal          : {subtotal:.2f}")
    print(f"Discount          : {discount:.2f}")
    print(f"Taxable amount    : {taxable:.2f}")
    print(f"Tax (18%)         : {tax:.2f}")
    print(f"GRAND TOTAL       : {grand_total:.2f}")
    print("=====================================")

    bills.append({"customer": customer, "total": grand_total})
    print("kartik , 2601940007")


def main():
    while True:
        print("\n====== MAIN MENU ======")
        print("1. Register Student")
        print("2. Attendance Management")
        print("3. Grading System")
        print("4. Expense Management")
        print("5. Billing System")
        print("6. Exit")


        choice = get_int("Enter your choice (1-6): ", 1, 6)

        if choice == 1:
            add_student()
        elif choice == 2:
            attendance()
        elif choice == 3:
            grade_student()
        elif choice == 4:
            print("\n1. Add Expense")
            print("2. View Expense Summary")
            sub_choice = get_int("Enter choice (1-2): ", 1, 2)
            if sub_choice == 1:
                add_expense()
            else:
                expense_summary()
        elif choice == 5:
            billing()
        elif choice == 6:
            print("Thank you for using the system. Goodbye!")
            break
        print("kartik , 2601940007")

try:
    main()
except KeyboardInterrupt:
    print("\nProgram closed safely.")