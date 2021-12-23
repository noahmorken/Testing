from employee import Employee

# Initializes the list and stores responses in it.
employee_list = Employee([], [], [])
employee_list.begin_input()
print("Enter 'q' at any time to quit.\n")
while True:
    first = input("First name: ")
    if first == 'q':
        break

    last = input("Last name: ")
    if last == 'q':
        break

    while True:
        salary = input("Salary: ")
        if salary == 'q':
            break
        try:
            salary = int(salary)
        except ValueError:
            print("That's not a number!")
        else:
            break
    if salary == 'q':
        break

    raise_confirm = input("Would you like to give this employee a raise? ")
    if raise_confirm.lower() == 'yes':
        raise_value = input("How much of a raise would you like to give? ")
        if raise_value == '':
            salary = employee_list.give_raise(salary)
        else:    
            try:
                raise_value = int(raise_value)
            except ValueError:
                print("That's not a number!")
            else:
                salary = employee_list.give_raise(salary, raise_value)

    employee_list.store_response(first, last, salary)

    print("\n")

# Show the survey results.
print("\nThank you to all employees!")
employee_list.show_results()