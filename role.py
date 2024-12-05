from enum import Enum
from operation import Operation as Op


class Role(Enum):
    CLIENT = ("Client",
              [Op.ViewAccountBalance, Op.ViewInvestmentPortfolio, Op.ViewFinancialAdvisorContactInfo, Op.Logout])
    PREMIUM_CLIENT = ("Premium_Client",
                      [Op.ModifyInvestmentPortfolio, Op.ViewFinancialPlannerContactInfo, Op.Logout])
    EMPLOYEE = ("Employee", [Op.ViewAccountBalance, Op.ViewInvestmentPortfolio, Op.Logout])
    FINANCIAL_ADVISOR = ("Financial_Advisor", [Op.ModifyInvestmentPortfolio, Op.ViewPrivateConsumerInstruments])
    FINANCIAL_PLANNER = ("Financial_Planner", [Op.ModifyInvestmentPortfolio, Op.ViewMoneyMarketInstruments,
                                               Op.ViewPrivateConsumerInstruments])
    TELLER = ("Teller", [])
    ALL_DAY_ACCESS = ("All_Day_Access", [])

    def get_name(self):
        return self.value[0]

    def get_authorized_operations(self):
        return self.value[1]

    def is_authorized_for_operation(self, operation):
        return operation in self.get_authorized_operations()

    @staticmethod
    def get_enum_from_name(role_name):
        for r in Role:
            if r.get_name() == role_name:
                return r
        return None
