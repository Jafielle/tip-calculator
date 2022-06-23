#Lo que aparece en pantalla para usuario
print("Welcome to the tip calculator!")
bill=input("What was the total bill? $")
tip=input("How much tip would you like to give? 10, 12, or 15? ")
people=input("How many people to split the bill? ")
#convertir los datos recogidos de string a integer
bill=float(bill)
tip=float(tip)
people=float(people)
#operaciones
x=tip/100+1
splitpay=(bill/people*x)
pay=(round(splitpay,2))
#mensaje con resultado
print(f"Each person should pay: {pay}")
