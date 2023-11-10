
food_amount=float(input('Enter food amount $:'))
tip_percentage=float(input('Enter tip tip percentage %: '))
tip_amount=(food_amount)*(tip_percentage)/100
total=int(food_amount)+tip_amount
# print(total)
#  lets add some amount sign like doller 
# i need to convert the amount into string
print ('Actual Amount $'+ str(food_amount))  
#  here f used for formatting
print(f'Tip amount: ${tip_amount}')
print('Total is $ ' +str(total))
