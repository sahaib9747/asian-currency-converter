def qartotaka():
    try: 
        qar=float(input("Enter the amount of Qatari Riyal="))
        bdt=23.00
        qar_to_bdt=bdt*qar
        if qar>0:
            print(qar,"Qatari Riyal in Taka","=",qar_to_bdt)
        else:
            print("Your Amount is zero or value less")
    except:
        print("Please Call qartotaka() function and Give your amount")
qartotaka()