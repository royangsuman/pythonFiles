price_of_house = 1000000
cust_credit = True

if cust_credit:
    amt_payable = 0.1* price_of_house
    print(f"Amount payable as down is ${amt_payable}")
else:
    amt_payable = 0.2* price_of_house
    print(f"Amount payable as down is ${amt_payable}")
