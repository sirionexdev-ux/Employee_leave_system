# ============================================================
# EMPLOYEE LEAVE MANAGEMENT SYSTEM


# -------------------- DATA --------------------

employees = {
    101: {"name": "Rahul", "department": "CSE"},
    102: {"name": "Priya", "department": "ECE"},
    103: {"name": "Arjun", "department": "IT"},
    104: {"name": "Sneha", "department": "CSE"},
    105: {"name": "Kiran", "department": "EEE"},
    106: {"name": "Anjali", "department": "IT"},
    107: {"name": "Vijay", "department": "ECE"},
    108: {"name": "Meena", "department": "CSE"},
    109: {"name": "Ravi", "department": "MECH"},
    110: {"name": "Divya", "department": "IT"}
}


leave_types = ("Casual", "Sick", "Emergency")


menu = (
    "Display Employees",
    "Apply Leave",
    "Check Leave Balance",
    "Employee Details",
    "Leave History",
    "Employees Currently on Leave",
    "Available Leave Types",
    "Exit"
)


employees_on_leave = set()

leave_history = []


leave_balance = {
    101: 20,
    102: 20,
    103: 20,
    104: 20,
    105: 20,
    106: 20,
    107: 20,
    108: 20,
    109: 20,
    110: 20
}


# ============================================================
# DECORATOR
# ============================================================

def log_activity(function):

    def wrapper(*args, **kwargs):

        print("\n--------------------------------")
        print("Executing:", function.__name__)
        print("--------------------------------")

        result = function(*args, **kwargs)

        print("--------------------------------")
        print("Operation completed.")
        print("--------------------------------")

        return result

    return wrapper


# ============================================================
# GENERAL FUNCTIONS
# ============================================================

def display_title(title="EMPLOYEE LEAVE MANAGEMENT"):
    """
    Default Argument
    """

    print("\n========================================")
    print(title)
    print("========================================")


def get_employee(employee_id):
    """
    Positional Argument
    Return employee details.
    """

    if employee_id in employees:
        return employees[employee_id]

    return None


def employee_exists(employee_id):
    """
    Positional Argument
    Return True/False.
    """

    return employee_id in employees


def get_employee_name(employee_id):

    employee = get_employee(employee_id)

    if employee:
        return employee["name"]

    return "Unknown"


# ============================================================
# *ARGS EXAMPLE
# ============================================================

def print_message(*messages):
    """
    *args example.

    Accepts any number of arguments.
    """

    for message in messages:
        print(message)


# ============================================================
# **KWARGS EXAMPLE
# ============================================================

def create_leave_record(**details):
    """
    **kwargs example.

    Accepts any number of keyword arguments.
    """

    return details


# ============================================================
# DISPLAY EMPLOYEES
# ============================================================

@log_activity
def display_employees():

    display_title("EMPLOYEE LIST")

    for employee_id, details in employees.items():

        print(
            employee_id,
            "-",
            details["name"],
            "-",
            details["department"]
        )


# ============================================================
# VALIDATE LEAVE
# ============================================================

def validate_leave(employee_id, leave_choice, number_of_days):
    """
    Multiple positional arguments.

    Returns True if leave request is valid.
    """

    if not employee_exists(employee_id):

        print("Employee not found.")
        return False


    if leave_choice < 1 or leave_choice > len(leave_types):

        print("Invalid leave type.")
        return False


    if number_of_days <= 0:

        print("Invalid number of days.")
        return False


    if number_of_days > leave_balance[employee_id]:

        print("Insufficient leave balance.")
        return False


    return True


# ============================================================
# APPLY LEAVE
# ============================================================

@log_activity
def apply_leave(employee_id, leave_choice, number_of_days=1):
    """
    Positional arguments + Default argument.
    """

    if not validate_leave(
        employee_id,
        leave_choice,
        number_of_days
    ):
        return


    selected_leave = leave_types[leave_choice - 1]


    # Update balance

    leave_balance[employee_id] -= number_of_days


    # Add employee to set

    employees_on_leave.add(employee_id)


    # Create record using **kwargs

    record = create_leave_record(
        employee_id=employee_id,
        leave_type=selected_leave,
        days=number_of_days
    )


    # Add record to history

    leave_history.append(record)


    print("\nLeave Approved!")

    print_message(
        "Employee: " + employees[employee_id]["name"],
        "Leave Type: " + selected_leave,
        "Days: " + str(number_of_days),
        "Remaining Leaves: " + str(leave_balance[employee_id])
    )


# ============================================================
# CHECK LEAVE BALANCE
# ============================================================

@log_activity
def check_leave_balance(employee_id):

    if not employee_exists(employee_id):

        print("Employee not found.")
        return


    total_leaves = 20

    used_leaves = total_leaves - leave_balance[employee_id]

    remaining_leaves = leave_balance[employee_id]


    print("\n===== LEAVE BALANCE =====")

    print("Employee:", get_employee_name(employee_id))

    print("Total Leaves:", total_leaves)

    print("Used Leaves:", used_leaves)

    print("Remaining Leaves:", remaining_leaves)


# ============================================================
# EMPLOYEE DETAILS
# ============================================================

@log_activity
def employee_details(employee_id):

    employee = get_employee(employee_id)


    if employee is None:

        print("Employee not found.")

        return


    print("\n===== EMPLOYEE DETAILS =====")

    print("Employee ID:", employee_id)

    print("Name:", employee["name"])

    print("Department:", employee["department"])

    print("Remaining Leaves:", leave_balance[employee_id])


# ============================================================
# GENERATOR
# ============================================================

def leave_history_generator():

    """
    Generator function.

    Yields one leave record at a time.
    """

    for leave in leave_history:

        yield leave


# ============================================================
# DISPLAY LEAVE HISTORY
# ============================================================

@log_activity
def display_leave_history():

    print("\n===== LEAVE HISTORY =====")


    if len(leave_history) == 0:

        print("No leave applications found.")

        return


    # Calling generator

    history = leave_history_generator()


    for leave in history:

        employee_id = leave["employee_id"]


        print("\nEmployee ID:", employee_id)

        print(
            "Name:",
            get_employee_name(employee_id)
        )

        print(
            "Leave Type:",
            leave["leave_type"]
        )

        print(
            "Days:",
            leave["days"]
        )


# ============================================================
# EMPLOYEES CURRENTLY ON LEAVE
# ============================================================

@log_activity
def employees_currently_on_leave():

    print("\n===== EMPLOYEES CURRENTLY ON LEAVE =====")


    if len(employees_on_leave) == 0:

        print("No employees are currently on leave.")

        return


    for employee_id in employees_on_leave:

        print(
            employee_id,
            "-",
            get_employee_name(employee_id)
        )


# ============================================================
# AVAILABLE LEAVE TYPES
# ============================================================

def display_leave_types():

    print("\n===== AVAILABLE LEAVE TYPES =====")


    for index, leave in enumerate(
        leave_types,
        start=1
    ):

        print(index, "-", leave)


# ============================================================
# MENU GENERATOR
# ============================================================

def menu_generator():

    """
    Generator for menu options.
    """

    for index, option in enumerate(
        menu,
        start=1
    ):

        yield index, option


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():

    print("\n===== MENU =====")


    for index, option in menu_generator():

        print(index, option)


# ============================================================
# *ARGS + **KWARGS DEMONSTRATION
# ============================================================

def generate_report(*employees, **options):

    """
    *args  -> employee IDs
    **kwargs -> report options
    """

    print("\n===== REPORT =====")


    print("Requested Employees:")

    for employee_id in employees:

        if employee_exists(employee_id):

            print(
                employee_id,
                "-",
                get_employee_name(employee_id)
            )


    print("\nReport Options:")

    for key, value in options.items():

        print(key, ":", value)


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    display_title()

    display_menu()


    try:

        choice = int(
            input("\nEnter your choice: ")
        )

    except ValueError:

        print("Please enter a valid number.")

        continue


    match choice:

        # ----------------------------------------------------
        # 1. DISPLAY EMPLOYEES
        # ----------------------------------------------------

        case 1:

            display_employees()


        # ----------------------------------------------------
        # 2. APPLY LEAVE
        # ----------------------------------------------------

        case 2:

            print("\n===== APPLY LEAVE =====")


            try:

                employee_id = int(
                    input("Enter Employee ID: ")
                )


                if not employee_exists(employee_id):

                    print("Employee not found.")

                    continue


                display_leave_types()


                leave_choice = int(
                    input("Select leave type: ")
                )


                number_of_days = int(
                    input("Enter number of days: ")
                )


                apply_leave(
                    employee_id,
                    leave_choice,
                    number_of_days
                )


            except ValueError:

                print("Please enter valid numbers.")


        # ----------------------------------------------------
        # 3. CHECK BALANCE
        # ----------------------------------------------------

        case 3:

            try:

                employee_id = int(
                    input("Enter Employee ID: ")
                )


                check_leave_balance(
                    employee_id
                )


            except ValueError:

                print("Invalid Employee ID.")


        # ----------------------------------------------------
        # 4. EMPLOYEE DETAILS
        # ----------------------------------------------------

        case 4:

            try:

                employee_id = int(
                    input("Enter Employee ID: ")
                )


                employee_details(
                    employee_id
                )


            except ValueError:

                print("Invalid Employee ID.")


        # ----------------------------------------------------
        # 5. LEAVE HISTORY
        # ----------------------------------------------------

        case 5:

            display_leave_history()


        # ----------------------------------------------------
        # 6. EMPLOYEES ON LEAVE
        # ----------------------------------------------------

        case 6:

            employees_currently_on_leave()


        # ----------------------------------------------------
        # 7. LEAVE TYPES
        # ----------------------------------------------------

        case 7:

            display_leave_types()


        # ----------------------------------------------------
        # 8. EXIT
        # ----------------------------------------------------

        case 8:

            print(
                "\nThank you for using "
                "Employee Leave Management System."
            )

            break


        # ----------------------------------------------------
        # INVALID
        # ----------------------------------------------------

        case _:

            print("Invalid choice.")
