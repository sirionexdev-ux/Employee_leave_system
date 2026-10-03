# Employee Leave Management System

employee_id = 101
employee_name = "Rahul"
employee_department = "CSE"

total_leaves = 20
used_leaves = 0
remaining_leaves = total_leaves

while True:

    print("\n===== EMPLOYEE LEAVE MANAGEMENT =====")

    print("1. Apply Leave")
    print("2. Check Leave Balance")
    print("3. Employee Details")
    print("4. Exit")

    employee_choice = int(input("Enter your choice: "))

    # Main menu
    match employee_choice:

        # Apply Leave
        case 1:

            print("\n===== LEAVE TYPES =====")
            print("1. Casual Leave")
            print("2. Sick Leave")
            print("3. Emergency Leave")

            leave_type = int(input("Select leave type: "))
            number_of_days = int(input("Enter number of days: "))

            if number_of_days <= 0:
                print("Invalid number of days.")
                continue

            if number_of_days > remaining_leaves:

                print("Leave request rejected.")
                print("Insufficient leave balance.")

            else:

                # Leave type selection
                match leave_type:

                    case 1:
                        print("Leave Type: Casual Leave")

                    case 2:
                        print("Leave Type: Sick Leave")

                    case 3:
                        print("Leave Type: Emergency Leave")

                    case _:
                        print("Invalid leave type.")
                        continue

                used_leaves = used_leaves + number_of_days
                remaining_leaves = total_leaves - used_leaves

                print("Leave approved.")
                print("Days approved:", number_of_days)
                print("Remaining leaves:", remaining_leaves)

        # Check leave balance
        case 2:

            print("\n===== LEAVE BALANCE =====")
            print("Total Leaves:", total_leaves)
            print("Used Leaves:", used_leaves)
            print("Remaining Leaves:", remaining_leaves)

        # Employee details
        case 3:

            print("\n===== EMPLOYEE DETAILS =====")

            employee_details = [
                employee_id,
                employee_name,
                employee_department
            ]

            for detail in employee_details:
                print(detail)

        # Exit
        case 4:

            print("Thank you for using the system.")
            break

        # Default case
        case _:

            print("Invalid choice.")
            print("Please select an option from 1 to 4.")
