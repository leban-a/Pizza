base = input("Would you like a thin or thick crust?\n> ")

size = input("Pick a pizza size from 8, 10, 12, 14 or 18 inches\n> ")

cheese = input("Would you like cheese? Y/N\n> ")

pizza_type = input("Which pizza type would you like?\n\
Margherita, Vegetable, Vegan, Hawaiian or Meat Feast\n> ")

voucher = input("If you have a voucher code, enter it now\
Press enter to skip\n> ")


base_cost = 10 if base.capitalize() == 'Thin'  else (8 if base.capitalize() == 'Thick' else None)
size_cost = 0 if size in ['8','10'] else (2 if size in ['12','14','18'] else None)
cheese_cost = 0 if cheese.upper() == 'Y' else -0.5
pizza_type_cost = 0 if pizza_type.capitalize() in ["Margarita"] else (1 if pizza_type.capitalize() in ["Vegetable","Vegan"] else (0 if pizza_type.capitalize() in ["Hawaiian","Meat feast"] else None ))
voucher_discount = -2 if voucher == 'FunFriday' and base == 18 else 0



total_cost  = base_cost + size_cost + pizza_type_cost + voucher_discount
print(f"You choose:\
      \nBase: {base.capitalize()}\
      \nSize: {size}\
      \nCheese: {cheese.capitalize()}\
      \nType: {pizza_type.capitalize()}\
      \nVoucher: {voucher.capitalize()}\
      \n\nTotal Cost: £{total_cost:.2f}")