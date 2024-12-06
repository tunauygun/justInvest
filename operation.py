from enum import Enum

# All operations in the system
class Operation(Enum):
    ViewAccountBalance = (1, "View account balance")
    ViewInvestmentPortfolio = (2, "View investment portfolio")
    ModifyInvestmentPortfolio = (3, "Modify investment portfolio")
    ViewFinancialAdvisorContactInfo = (4, "View Financial Advisor contact info")
    ViewFinancialPlannerContactInfo = (5, "View Financial Planner contact info")
    ViewMoneyMarketInstruments = (6, "View money market instruments")
    ViewPrivateConsumerInstruments = (7, "View private consumer instruments")
    Logout = (8, "Logout")

    def get_id(self):
        return self.value[0]

    def get_name(self):
        return self.value[1]

    def run_operation_menu(self):
        if self.get_id() == Operation.Logout.get_id():
            return True
        else:
            print(f"Your are currently at: {self.get_name()} page")
            input("Press enter to go back to main menu...")
            return False

    @staticmethod
    def get_enum_from_id(operation_id):
        for op in Operation:
            if op.get_id() == operation_id:
                return op
        return None
