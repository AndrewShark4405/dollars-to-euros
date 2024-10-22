print("This code will convert dollar amount to euros")
choice = input("Do you want to convert USD to Euros? Yes or No: ")
while choice == str("yes"):
    USD = float(input("Enter the dollar amount: "))
    Euros = USD * .94540
    print("Your amount in euros: "  +  str(Euros))
    choice = input("Do you want to convert USD to Euros? Yes or No: ")
    if choice == "No":
        break
print("Credit to coder: Big Shark")