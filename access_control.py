from role import Role
from helpers import *

# Get a list of all authorized operations for a given list of user roles
def get_authorized_operations(user_roles):
    authorized_operations = set()
    for role in user_roles:
        for op in role.get_authorized_operations():
            authorized_operations.add(op)
    operation_list = list(authorized_operations)
    operation_list.sort(key=lambda op: op.get_id())
    return operation_list

# Given a list of user roles and a time, returns if the user has access to the system
def check_access_currently(user_roles, time):
    hour, minute = time
    print_time(hour, minute)
    print()
    return _has_access_currently(user_roles, [hour, minute])

# Given a list of user roles and a time, returns if the user has access to the system
def _has_access_currently(user_roles, time):
    hour, minute = time
    if _has_all_day_access(user_roles):
        return True
    if within_business_hours(hour, minute):
        return True
    return False

# Given a list of user roles, returns true if the user has access to the system all day
def _has_all_day_access(user_roles):
    return Role.ALL_DAY_ACCESS in user_roles
