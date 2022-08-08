#--------choose number-------

first_number= float(input("Enter the first_number is:"))


second_number = float(input("Enter the second_number is:"))


third_number = float(input("Enter the third_number is:"))

#----------------------------------------------------
pylist= list((first_number,second_number,third_number))
print("list number :",(pylist))
#---------------------------------------------------
if (first_number >= second_number) and (first_number >= third_number):
    largest = first_number
    
    
elif (second_number >= first_number) and (second_number >= third_number):
    largest = second_number
    
else:
    largest = third_number
    
    print("the largest number is :" ,(largest))

