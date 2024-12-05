import unittest

from access_control import get_authorized_operations, check_access_currently
from user_type import UserType
from operation import Operation


class TestAuthorizedOperations(unittest.TestCase):

    def test_client(self):
        authorized_operations = get_authorized_operations(UserType.CLIENT.get_roles())
        self.assertEqual(len(authorized_operations), 4)

        self.assertTrue(Operation.ViewAccountBalance in authorized_operations)
        self.assertTrue(Operation.ViewInvestmentPortfolio in authorized_operations)
        self.assertFalse(Operation.ModifyInvestmentPortfolio in authorized_operations)
        self.assertTrue(Operation.ViewFinancialAdvisorContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewFinancialPlannerContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewMoneyMarketInstruments in authorized_operations)
        self.assertFalse(Operation.ViewPrivateConsumerInstruments in authorized_operations)
        self.assertTrue(Operation.Logout in authorized_operations)

    def test_premium_client(self):
        authorized_operations = get_authorized_operations(UserType.PREMIUM_CLIENT.get_roles())
        self.assertEqual(len(authorized_operations), 6)

        self.assertTrue(Operation.ViewAccountBalance in authorized_operations)
        self.assertTrue(Operation.ViewInvestmentPortfolio in authorized_operations)
        self.assertTrue(Operation.ModifyInvestmentPortfolio in authorized_operations)
        self.assertTrue(Operation.ViewFinancialAdvisorContactInfo in authorized_operations)
        self.assertTrue(Operation.ViewFinancialPlannerContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewMoneyMarketInstruments in authorized_operations)
        self.assertFalse(Operation.ViewPrivateConsumerInstruments in authorized_operations)
        self.assertTrue(Operation.Logout in authorized_operations)

    def test_financial_advisor(self):
        authorized_operations = get_authorized_operations(UserType.FINANCIAL_ADVISOR.get_roles())
        self.assertEqual(len(authorized_operations), 5)

        self.assertTrue(Operation.ViewAccountBalance in authorized_operations)
        self.assertTrue(Operation.ViewInvestmentPortfolio in authorized_operations)
        self.assertTrue(Operation.ModifyInvestmentPortfolio in authorized_operations)
        self.assertFalse(Operation.ViewFinancialAdvisorContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewFinancialPlannerContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewMoneyMarketInstruments in authorized_operations)
        self.assertTrue(Operation.ViewPrivateConsumerInstruments in authorized_operations)
        self.assertTrue(Operation.Logout in authorized_operations)

    def test_financial_planner(self):
        authorized_operations = get_authorized_operations(UserType.FINANCIAL_PLANNER.get_roles())
        self.assertEqual(len(authorized_operations), 6)

        self.assertTrue(Operation.ViewAccountBalance in authorized_operations)
        self.assertTrue(Operation.ViewInvestmentPortfolio in authorized_operations)
        self.assertTrue(Operation.ModifyInvestmentPortfolio in authorized_operations)
        self.assertFalse(Operation.ViewFinancialAdvisorContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewFinancialPlannerContactInfo in authorized_operations)
        self.assertTrue(Operation.ViewMoneyMarketInstruments in authorized_operations)
        self.assertTrue(Operation.ViewPrivateConsumerInstruments in authorized_operations)
        self.assertTrue(Operation.Logout in authorized_operations)

    def test_teller(self):
        authorized_operations = get_authorized_operations(UserType.TELLER.get_roles())
        self.assertEqual(len(authorized_operations), 3)

        self.assertTrue(Operation.ViewAccountBalance in authorized_operations)
        self.assertTrue(Operation.ViewInvestmentPortfolio in authorized_operations)
        self.assertFalse(Operation.ModifyInvestmentPortfolio in authorized_operations)
        self.assertFalse(Operation.ViewFinancialAdvisorContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewFinancialPlannerContactInfo in authorized_operations)
        self.assertFalse(Operation.ViewMoneyMarketInstruments in authorized_operations)
        self.assertFalse(Operation.ViewPrivateConsumerInstruments in authorized_operations)
        self.assertTrue(Operation.Logout in authorized_operations)

    def test_time_restriction_within_business_hours(self):
        time = [14, 35]  #2:35 pm (within business hours)

        client_has_access = check_access_currently(UserType.CLIENT.get_roles(), time)
        self.assertTrue(client_has_access)

        premium_client_has_access = check_access_currently(UserType.PREMIUM_CLIENT.get_roles(), time)
        self.assertTrue(premium_client_has_access)

        financial_advisor_has_access = check_access_currently(UserType.FINANCIAL_ADVISOR.get_roles(), time)
        self.assertTrue(financial_advisor_has_access)

        financial_planner_has_access = check_access_currently(UserType.FINANCIAL_PLANNER.get_roles(), time)
        self.assertTrue(financial_planner_has_access)

        teller_has_access = check_access_currently(UserType.TELLER.get_roles(), time)
        self.assertTrue(teller_has_access)


    def test_time_restriction_outside_business_hours(self):
        time = [2, 35]  # 2:35 am (outside business hours)

        client_has_access = check_access_currently(UserType.CLIENT.get_roles(), time)
        self.assertTrue(client_has_access)

        premium_client_has_access = check_access_currently(UserType.PREMIUM_CLIENT.get_roles(), time)
        self.assertTrue(premium_client_has_access)

        financial_advisor_has_access = check_access_currently(UserType.FINANCIAL_ADVISOR.get_roles(), time)
        self.assertTrue(financial_advisor_has_access)

        financial_planner_has_access = check_access_currently(UserType.FINANCIAL_PLANNER.get_roles(), time)
        self.assertTrue(financial_planner_has_access)

        teller_has_access = check_access_currently(UserType.TELLER.get_roles(), time)
        self.assertFalse(teller_has_access)


if __name__ == '__main__':
    unittest.main()
