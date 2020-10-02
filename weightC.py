your_weight = input('Enter your weight ')
your_choice = input('Enter your conversion in (L)bs or K(g) ').upper()

if your_choice == 'L':
    print(int(your_weight)*0.45)
else:
    print(int(your_weight)/0.45)