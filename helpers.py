import random

from operation import Operation


def get_enum_selection(enum, title: str = "Available Options:"):
    enums = {}
    enum_ids = []

    print(title)
    for e in enum:
        print(f' {e.get_id()}. {e.get_name()}')
        enums[e.get_id()] = e
        enum_ids.append(e.get_id())
    selected_enum_id = get_valid_input_from_list(enum_ids)
    return enums[selected_enum_id]


def get_input_from_options(options: list[str], title: str = "Available Operations:"):
    print(title)
    for index, option in enumerate(options):
        print(f' {index + 1}. {option}')
    return get_valid_input_from_list([i + 1 for i in range(len(options))])


def display_operation_list(operations: list[Operation], title: str = "Available Operations:"):
    print(title)
    for op in operations:
        print(f' {op.get_id()}. {op.get_name()}')


def get_valid_input_from_list(valid_inputs: list[int], prompt: str = " > "):
    while True:
        try:
            user_input = int(input(prompt))
            if not user_input in valid_inputs:
                print(" Please enter a valid input!")
                continue
            break
        except ValueError:
            print(" Please enter a valid input!")
    return user_input


def clear_page():
    print("\n" * 40)


def get_random_time():
    h = random.randint(0, 23)
    m = random.randint(0, 59)
    return h, m


def print_time(hour, minute):
    am_pm = "am" if hour < 12 else "pm"
    hour %= 12
    print(f'Current time is {hour:02}:{minute:02} {am_pm}')


def within_business_hours(hour, minute):
    if (hour >= 9 and hour < 17) or (hour == 17 and minute == 0):
        return True
    return False
