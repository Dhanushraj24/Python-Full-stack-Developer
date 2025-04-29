# Simple Pizza Ordering System

# Get Input from User
a = str(input("Enter a Pizza Size (Small/Medium/Large): "))
b = str(input("Do You want pepper? (Yes/No): "))
c = str(input("Do You want Extra Cheese? (Yes/No): "))

# Prices of Pizza Based on Size and Additional Ingredients
Small = 15 
Medium = 20
Large = 25
pepperS = 2
pepperML = 3
ExtraCheese = 1

# Calculate the Pizza price 
TotalPriceS1 = Small + pepperS + ExtraCheese
TotalPriceS2 = Small + ExtraCheese
TotalPriceS3 = Small + pepperS
TotalPriceM1 = Medium + pepperML + ExtraCheese
TotalPriceM2 = Medium + ExtraCheese
TotalPriceM3 = Medium + pepperML
TotalPriceL1 = Large + pepperML + ExtraCheese
TotalPriceL2 = Large + ExtraCheese
TotalPriceL3 = Large + pepperML 

# This is the Final Step for Calculating the Price of a Pizza Using Conditional Statements.
if a == "Small" and b == "No" and c == "No":
    print("Your Total bill is: ",f"${Small}")
elif a == "Small" and b == "Yes" and c == "Yes":
    print("Your Total bill is: ",f"${TotalPriceS1}")
elif a == "Small" and b == "No" and c == "Yes":
    print("Your Total bill is: ",f"${TotalPriceS2}")
elif a == "Small" and b == "Yes" and c == "No":
    print("Your Total bill is: ",f"${TotalPriceS3}")
elif a == "Medium" and b == "No" and c == "No":
    print("Your Total bill is: ",f"${Medium}")
elif a == "Medium" and b == "Yes" and c == "Yes":
    print("Your Total bill is: ",f"${TotalPriceM1}")
elif a == "Medium" and b == "No" and c == "Yes":
    print("Your Total bill is: ",f"${TotalPriceM2}")
elif a == "Medium" and b == "Yes" and c == "No":
    print("Your Total bill is: ",f"${TotalPriceM3}")
elif a == "Large" and b == "No" and c == "No":
    print("Your Total bill is: ",f"${Large}")
elif a == "Large" and b == "Yes" and c == "Yes":
    print("Your Total bill is: ",f"${TotalPriceL1}")
elif a == "Large" and b == "No" and c == "Yes":
    print("Your Total bill is: ",f"${TotalPriceL2}")
elif a == "Large" and b == "Yes" and c == "No":
    print("Your Total bill is: ",f"${TotalPriceL3}")
else:
    print("Invalid Order")
