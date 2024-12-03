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

# def get_int_input(prompt=" > ", min: int = None, max: int = None):
#     while True:
#         try:
#             user_input = int(input(prompt))
#             if (min is not None and user_input < min) or (max is not None and user_input > max):
#                 print(" Please enter a valid input. (Between {} and {})".format(min, max))
#                 continue
#             break
#         except ValueError:
#             print(" Please enter a valid input.")
#
#     return user_input
