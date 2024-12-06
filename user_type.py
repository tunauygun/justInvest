from enum import Enum
from role import Role

# All user types within the system
class UserType(Enum):
    CLIENT = (1, "Client", [Role.CLIENT, Role.ALL_DAY_ACCESS])
    PREMIUM_CLIENT = (2, "Premium Client", [Role.PREMIUM_CLIENT, Role.CLIENT, Role.ALL_DAY_ACCESS])
    FINANCIAL_ADVISOR = (3, "Financial Advisor", [Role.FINANCIAL_ADVISOR, Role.EMPLOYEE, Role.ALL_DAY_ACCESS])
    FINANCIAL_PLANNER = (4, "Financial Planner", [Role.FINANCIAL_PLANNER, Role.EMPLOYEE, Role.ALL_DAY_ACCESS])
    TELLER = (5, "Teller", [Role.TELLER, Role.EMPLOYEE])

    def get_id(self):
        return self.value[0]

    def get_name(self):
        return self.value[1]

    def get_roles(self):
        return self.value[2]

    def has_role(self, role):
        return role in self.get_roles()

    @staticmethod
    def get_enum_from_id(user_type_id):
        for ut in UserType:
            if ut.get_id() == user_type_id:
                return ut
        return None
