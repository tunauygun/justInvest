def get_authorized_operations(user_roles):
    authorized_operations = set()
    for role in user_roles:
        for op in role.get_authorized_operations():
            authorized_operations.add(op)
    operation_list = list(authorized_operations)
    operation_list.sort(key=lambda op: op.get_id())
    return operation_list
