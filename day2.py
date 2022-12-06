# Tip Calculator

bill = int(input("How much do you owe by the bill? "))
people = int(input("You and your crew, are about how many people? "))
tip =int(input("The tip for the waitress will be of: 12%, 15% or 20%? "))

percent_tip = tip/100
to_pay = (bill/people) * percent_tip

final_amount = "{:.2f}".format(to_pay)
print(f"Each person must pay the amount of: $ {final_amount} to the waitress")
