import time
from helpers import *
from user_management import register_and_login
from access_control import get_authorized_operations, check_access_currently


def main():
    try:
        while True:
            clear_page()
            print("justInvest System\n" + "-" * 35)
            user = register_and_login()
            clear_page()

            has_access = check_access_currently(user.get_roles(), get_random_time())
            if has_access:
                print("ACCESS GRANTED!")
            else:
                print("ACCESS DENIED!")
                time.sleep(3)
                print("Logging out...")
                time.sleep(3)
                continue

            while True:
                authorized_operations = get_authorized_operations(user.get_roles())
                selected_operation = get_enum_selection(authorized_operations, "Your authorized operations: ")
                clear_page()
                is_logged_out = selected_operation.run_operation_menu()
                clear_page()
                if is_logged_out:
                    print("Logged out...")
                    time.sleep(1)
                    user = None
                    break

    except KeyboardInterrupt as ke:
        print(("\n" * 40) + "EXITING...")
        exit(0)


if __name__ == '__main__':
    main()
