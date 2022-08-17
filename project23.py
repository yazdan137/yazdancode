print("This is buddy mass index program (BMI)\n")

while 1:

    W = float(input("Enter your Wight(kg_g):"))

    H =float(input("Enter your Hight(meter):"))
    if H > 4:
        print("your entries Hight is invalid \n Did you mean ",H/100,"meter ?")
        massage = input("(yes | no) ?")
        if massage == "no":
            print("it is invalid")
            H = float(input("Enter your Hight (meter) again(0.5 to 4):"))
        elif massage == "yes":
            H = H/100
            

    BMI = W/pow(H,2)

    print("your BMI is:" , BMI)

    W_max = 25*pow(H,2)

    W_min = 20*pow(H,2)
    
    

    if BMI > 25:

        W_over_weight = W - W_max

        print("you have over weight and your over weight is:" , W_over_weight ,"kg")

    elif BMI < 20:

        W_under_weight = W_min - W

        print("you have under weight and your under weight is:" , W_under_weight , "kg")

    else:

        print("you have normal weight and\n good weight for you are between" , 

              W_min ,"and" , W_max , "kg")
    massage = input("\n Do you want continue (yes | no):")
    if massage == "no":
        break
    elif massage == "yes":
        continue
    else:
        print("please just say 'yes' or 'no' ")
        massage = input("(yes | no)")
        if massage == "yes":
            continue
        else:
            break
        
        
    
        
                

    
    
        






