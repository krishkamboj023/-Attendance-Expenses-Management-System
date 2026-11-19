expenses = []
attendance = []
students = []
bills = []


def expense_menu():
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Expense total")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Expense name: ")
            print("Categories: Food, Travel, Bills, Other")
            category = input("Category: ")
            amount = float(input("Amount: "))

            if amount > 0:
                expenses.append([name, category, amount])
                print("Expense added.")
            else:
                print("Amount must be greater than zero.")

        elif choice == "2":
            if len(expenses) == 0:
                print("No expenses found.")
            else:
                for item in expenses:
                    print(item[0], "-", item[1], "-", item[2])

        elif choice == "3":
            total = 0
            for item in expenses:
                total = total + item[2]
            print("Total expenses:", total)

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def attendance_menu():
    while True:
        print("\n1. Add attendance")
        print("2. View attendance")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student name: ")
            total_days = int(input("Total working days: "))
            present_days = int(input("Days present: "))

            if total_days > 0 and present_days >= 0 and present_days <= total_days:
                percentage = (present_days / total_days) * 100
                if percentage >= 75:
                    status = "Eligible"
                else:
                    status = "Shortage"

                attendance.append([name, total_days, present_days,
                                   percentage, status])
                print("Attendance added.")
            else:
                print("Please enter correct number of days.")

        elif choice == "2":
            if len(attendance) == 0:
                print("No attendance records found.")
            else:
                for record in attendance:
                    print("Name:", record[0])
                    print("Attendance:", round(record[3], 2), "%")
                    print("Status:", record[4])
                    print("--------------------")

        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def grading_menu():
    while True:
        print("\n1. Add student marks")
        print("2. View student results")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student name: ")
            marks = []
            total = 0

            number = int(input("Number of subjects: "))
            

            for i in range(number):
                mark = float(input("Enter marks: "))
                marks.append(mark)
                total = total + mark

            average = total / number

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            elif average >= 35:
                grade = "E"
            else:
                grade = "F"

            result = "Pass"

            for mark in marks:
                if mark < 35:
                    result = "Fail"

            students.append([name, marks, total, average, grade, result])
            print("Student result saved.")

        elif choice == "2":
            if len(students) == 0:
                print("No student records found.")
            else:
                for student in students:
                    print("\nName:", student[0])
                    print("Marks:", student[1])
                    print("Total:", student[2])
                    print("Average:", round(student[3], 2))
                    print("Grade:", student[4])
                    print("Result:", student[5])

        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def billing_menu():
    while True:
        print("\n1. Create bill")
        print("2. View bills")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            customer = input("Customer name: ")
            item_count = int(input("Number of items: "))
            total = 0
            items = []

            for i in range(item_count):
                item_name = input("Item name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                amount = price * quantity
                total = total + amount
                items.append([item_name, price, quantity, amount])

            if total >= 5000:
                discount = total * 0.10
            elif total >= 1000:
                discount = total * 0.05
            else:
                discount = 0

            after_discount = total - discount
            tax = after_discount * 0.18
            final_amount = after_discount + tax
            bills.append([customer, items, total, discount, tax, final_amount])

            print("\n--------- BILL ---------")
            print("Customer:", customer)
            for item in items:
                print(item[0], item[1], "x", item[2], "=", item[3])
            print("Subtotal:", total)
            print("Discount:", discount)
            print("Tax (18%):", tax)
            print("Final amount:", round(final_amount, 2))
            print("------------------------")

        elif choice == "2":
            if len(bills) == 0:
                print("No bills found.")
            else:
                for bill in bills:
                    print(bill[0], "- Total:", round(bill[5], 2))

        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def reports_menu():
    print("\n----- REPORTS -----")
    expense_total = 0
    for item in expenses:
        expense_total = expense_total + item[2]

    print("Total expenses:", expense_total)
    print("Attendance records:", len(attendance))
    print("Student records:", len(students))
    print("Bills created:", len(bills))

    if len(students) > 0:
        total_average = 0
        for student in students:
            total_average = total_average + student[3]
        print("Class average:", round(total_average / len(students), 2))


def main():
    while True:
        print("\n===== MANAGEMENT SYSTEM =====")
        print("1. Expense Management")
        print("2. Attendance Management")
        print("3. Student Grading")
        print("4. Billing System")
        print("5. Reports")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            expense_menu()
        elif choice == "2":
            attendance_menu()
        elif choice == "3":
            grading_menu()
        elif choice == "4":
            billing_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()