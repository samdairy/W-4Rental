class RentalProperty:
    def __init__(self, purchase_price, rental_income, expenses, financing):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses
        self.financing = financing

    def calculate_cash_flow(self):
        cash_flow = self.rental_income - self.expenses
        return cash_flow
    
    #Cap_Rate property based on the income that the property is expected to generate.

    def calculate_cap_rate(self):
        net_income = self.rental_income - self.expenses
        cap_rate = net_income / self.purchase_price
        return cap_rate
    

    def calculate_roi(self):
        down_payment = self.purchase_price * self.financing['down_payment']
        loan_amount = self.purchase_price - down_payment
        mortgage_payment = (loan_amount * self.financing['interest_rate']) 
        annual_cash_flow = self.calculate_cash_flow() * 12
        total_investment = down_payment + (self.expenses * 12)
        total_return = annual_cash_flow / total_investment
        investment = total_return * 100
        return investment
    

# Example usage:
property1 = RentalProperty(300000, 2500, 870, {'down_payment': 0.2, 'interest_rate': 0.05, 'loan_term': 15})
print('Cash Flow:', property1.calculate_cash_flow())
print('Cap Rate:', property1.calculate_cap_rate())
print('ROI:',property1.calculate_roi()) 



    









   












