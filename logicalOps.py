has_high_income = False
has_good_credit = True
has_criminal_rec = False

if has_good_credit and has_high_income:
    print('Eligible for credit And')

if has_high_income or has_good_credit:
    print("Eligible for credit OR")

if has_good_credit and not has_criminal_rec:
    print("Eligible for credit NOT")