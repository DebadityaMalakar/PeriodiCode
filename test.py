data = {}

def Hydrogen(x):
    variable, value = x.split()
    if variable in data:
        print(f"Error: Variable '{variable}' is already declared.")
    else:
        if value.endswith(";"):
            data[variable] = value[:-1]
        else:
            data[variable] = value  # Store the value without semicolon

def Iron(variable):
    variable = variable.rstrip(";")
    if variable in data:
        print(data[variable])
    else:
        print(f"Error: Variable '{variable}' does not exist.")

def Carbon(numbers):
    try:
        numbers = [data[num] if num in data else num for num in numbers]  # Replace variable names with values if available
        numbers = list(map(int, numbers))
        result = sum(numbers)
        print(result)
    except ValueError:
        print("Error: Unsupported data type for the Carbon function.")

def Oxygen_for(start, end):
    try:
        start_val = int(data[start]) if start in data else int(start)
        end_val = int(data[end]) if end in data else int(end)
        for i in range(start_val, end_val + 1):
            print(i)
    except ValueError:
        print("Error: Invalid start or end value for Oxygen.for.")

def Oxygen_iter(sequence):
    try:
        if sequence in data:
            sequence = data[sequence]
        for item in sequence:
            print(item)
    except TypeError:
        print("Error: 'Oxygen.iter' requires an iterable sequence.")

def validate_command(command):
    if "\n" in command:
        print("\\n Not Allowed.")
        return False

    if command[-1] != ";":
        print("Semicolon required")
        return False

    return True

def parse_command(command):
    a = command.split(" ")
    if a[0] == "Hydrogen":
        try:
            Hydrogen(" ".join(a[1:]))
        except ValueError:
            print("Error: Invalid Hydrogen function syntax.")

    elif a[0] == "Iron":
        if len(a) <= 1:
            print("Error: No variable provided to print.")
        elif len(a) > 2:
            print("Error: Extra arguments after the variable.")
        else:
            variable = a[1]
            Iron(variable)

    elif a[0] == "Carbon":
        if len(a) < 2:
            print("Error: Two or more numbers required for the Carbon function.")
        else:
            numbers = a[1:]
            Carbon(numbers)

    elif a[0] == "Oxygen.for":
        if len(a) != 3:
            print("Error: 'Oxygen.for' requires two arguments.")
        else:
            start, end = a[1], a[2].rstrip(";")
            Oxygen_for(start, end)

    elif a[0] == "Oxygen.iter":
        if len(a) != 2:
            print("Error: 'Oxygen.iter' requires one argument.")
        else:
            sequence = a[1].rstrip(";")
            Oxygen_iter(sequence)

def run_test_cases():
    test_cases = [
        # Valid commands
        "Hydrogen x 10;",
        "Iron x;",
        "Oxygen.for 1 5;",
        "Carbon x 10;",
        "Oxygen.iter [1, 2, 3];",
        # Invalid commands
        "Hydrogen x 10",  # Missing semicolon
        "Iron x",  # Missing semicolon
        "Oxygen.for 1;",  # Missing end argument
        "Carbon x;",  # Missing numbers for Carbon
        "Oxygen.iter 1, 2, 3;",  # Incorrect sequence syntax
    ]

    for test_case in test_cases:
        print("Mendeleev:::")
        command = test_case.strip()
        if not validate_command(command):
            continue
        parse_command(command)

run_test_cases()
