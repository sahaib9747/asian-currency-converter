def currancy():
    try:
        welcome = ("WELCOME TO ASIAN MONEY CONVERTER")
        author = ("AUTHOR:MD SAHAIB MRIDHA(RIHAN)")
        welcome = welcome.center(160,"-")
        author = author.center(159,"-")
        print(welcome,"\n",author,"\nCHOOSE YOUR'S OPTION PLEASE:\n1.BANGLADESHI TAKA TO US DOLLER\n2.US DOLLER TO BANGLADESHI TAKA\n3.BANGLADESHI TAKA TO INDIAN RUPEE\n4.INDIAN RUPEE TO BANGLADESHI TAKA\n5.BANGLADESHI TAKA TO SAUDI ARABIAN RIYAL\n6.SAUDI ARABIAN RIYAL TO BANGLADESHI TAKA\n7.BANGLADESHI TAKA TO SRILANKAN RUPEE\n8.SRILANKAN RUPEE IN BANGLADESHI TAKA\n9.BANGLADESHI TAKA TO MALAYSIAN RINGGIT\n10.MALAYSIAN RINGGIT TO BANGLADESHI TAKA\n11.BANGLADESHI TAKA TO CHINESE YUAN\n12.CHINESE YUAN TO BANGLADESHI TAKA\n13.BANGLADESHI TAKA TO SINGAPORE DOLLER\n14.SINGAPORE DOLLER TO BANGLADESHI TAKA\n15.BANGLADESHI TAKA TO MYANMAR KYAT\n16.MYANMAR KYAT TO BANGLADESHI TAKA\n17.BANGLADESHI TAKA TO NEPALESE RUPEE\n18.NEPALESE RUPEE TO BANGLADESHI TAKA\n19.BANGLADESHI TAKA TO KUWAITI DINAR\n20.KUWAITI DINAR TO BANGLADESHI TAKA\n21.BANGLADESHI TAKA TO IRANIAN RIYAL\n22.IRANIAN RIYAL TO BANGLADESHI TAKA\n23.BANGLADESHI TAKA TO IRAQI DINAR\n24.IRAQI DINAR TO BANGLADESHI TAKA\n25.BANGLADESHI TAKA TO QATARI RIYAL\n26.QATARI RIYAL TO BANGLADESHI TAKA\n00.INFORMATION ABOUT ASIAN MONEY CONVERTER")
        option = int(input("Reply:"))
        #INFORMATION ABOUT ASIAN MONEY CONVERTER
        if option == 0:
            print(
              """SOME INFORMATION ABOUT ASIAN MONEY CONVERTER:\n"
              "Mr. MD Sahaib Mridha (Rihan) started the work of Asian money converter in January 2019.
              At first, his goal was to work with the money of 100 countries, but he lost confidence 
              due to lack of adequate support from anyone, but motiveted his own self and after three
              months he Continue his work on Asian money converter, now he working on Asian money converter version 1.00""")
        #BANGLADESHI TAKA TO US DOLLER
        if option == 1:
            print("BANGLADESHI TAKA TO US DOLLER:")
            bdt=float(input("Enter the amount of taka="))
            usd=0.011904761904761904
            bdt_to_usd=bdt*usd
            if bdt>0:
                print(bdt,"Taka in us doller","=",bdt_to_usd,"$")
            else:
                print("Your Amount is zero or value less")

        #US DOLLER TO BANGLADESHI TAKA
        if option == 2:
            print("US DOLLER TO BANGLADESHI TAKA:")
            usd=float(input("Enter the amount of us doller="))
            bdt=84
            usd_to_bdt=usd*bdt
            if usd>0:
                print(usd,"Doller in taka","=",usd_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO INDIAN RUPEE
        if option == 3:
            print("BANGLADESHI TAKA TO INDIAN RUPEE:")
            bdt=float(input("Enter the amount of taka="))
            inr=0.85
            bdt_to_inr=bdt*inr
            if bdt>0:
                print(bdt,"Taka in indian rupee","=",bdt_to_inr)
            else:
                print("Your Amount is zero or value less")

        #INDIAN RUPEE TO BANGLADESHI TAKA
        if option == 4:
            print("INDIAN RUPEE TO BANGLADESHI TAKA:")
            inr=float(input("Enter the amount of indian rupee="))
            bdt=1.18
            inr_to_bdt=inr*bdt
            if inr>0:
                print(inr,"indian rupee to taka","=",inr_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO SAUDI ARABIAN RIYAL
        if option == 5:
            print("BANGLADESHI TAKA TO SAUDI ARABIAN RIYAL:")
            bdt=float(input("Enter the amount of taka="))
            sar=0.045
            bdt_to_sar=bdt*sar
            if bdt>0:
                print(bdt,"Taka in Saudi Arabian riyal","=",bdt_to_sar)
            else:
                print("Your Amount is zero or value less")


        #SAUDI ARABIAN RIYAL TO BANGLADESHI TAKA
        if option == 6:
            print("SAUDI ARABIAN RIYAL TO BANGLADESHI TAKA:")
            sar=float(input("Enter the amount of Saudi Arabian Riyal="))
            bdt=22.37
            sar_to_bdt=sar*bdt
            if sar>0:
                print(sar,"Saudi Arabian Riyal in Taka","=",sar_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO SRILANKAN RUPEE
        if option == 7:
            print("BANGLADESHI TAKA TO SRILANKAN RUPEE:")
            bdt=float(input("Enter the amount of taka="))
            lkr=2.16
            bdt_to_lkr=bdt*lkr
            if bdt>0:
                print(bdt,"Taka in Srilankan rupee","=",bdt_to_lkr)
            else:
                print("Your Amount is zero or value less")


        #SRILANKAN RUPEE IN BANGLADESHI TAKA
        if option == 8:
            print("SRILANKAN RUPEE IN BANGLADESHI TAKA:")
            lkr=float(input("Enter the amount of Srilankan Rupee="))
            bdt=0.46
            lkr_to_bdt=lkr*bdt
            if lkr>0:
                print(lkr,"Srilankan rupee in Taka","=",lkr_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO MALAYSIAN RINGGIT
        if option == 9:
            print("BANGLADESHI TAKA TO MALAYSIAN RINGGIT:")
            bdt=float(input("Enter the amount of taka="))
            myr=0.049
            bdt_to_myr=bdt*myr
            if bdt>0:
                print(bdt,"Taka in Malaysian Ringgit","=",bdt_to_myr)
            else:
                print("Your Amount is zero or value less")


        #MALAYSIAN RINGGIT TO BANGLADESHI TAKA
        if option == 10:
            print("MALAYSIAN RINGGIT TO BANGLADESHI TAKA:")
            myr=float(input("Enter the amount of Malaysian Ringgit="))
            bdt=20.32
            myr_to_bdt=bdt*myr
            if myr>0:
                print(myr,"Malaysian Ringgit in Taka","=",myr_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO CHINESE YUAN
        if option == 11:
            print("BANGLADESHI TAKA TO CHINESE YUAN:")
            bdt=float(input("Enter the amount of taka="))
            cny=0.081
            bdt_to_cny=bdt*cny
            if bdt>0:
                print(bdt,"Taka in Chinese Yuan","=",bdt_to_cny)
            else:
                print("Your Amount is zero or value less")


        #CHINESE YUAN TO BANGLADESHI TAKA
        if option == 12:
            print("CHINESE YUAN TO BANGLADESHI TAKA:")
            cny=float(input("Enter the amount of Chinese Yuan="))
            bdt=12.41
            cny_to_bdt=cny*bdt
            if cny>0:
                print(cny,"Chinese Yuan in Taka","=",cny_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO SINGAPORE DOLLER
        if option == 13:
            print("BANGLADESHI TAKA TO SINGAPORE DOLLER:")
            bdt=float(input("Enter the amount of taka="))
            sgd=0.016
            bdt_to_sgd=sgd*bdt
            if bdt>0:
                print(bdt,"Taka in Singapore Doller","=",bdt_to_sgd)
            else:
                print("Your Amount is zero or value less")


        #SINGAPORE DOLLER TO BANGLADESHI TAKA
        if option == 14:
            print("SINGAPORE DOLLER TO BANGLADESHI TAKA:")
            sgd=float(input("Enter the amount of Singapore Doller="))
            bdt=61.86
            sgd_to_bdt=bdt*sgd
            if sgd>0:
                print(sgd,"Singapore Doller in Taka","=",sgd_to_bdt)
            else:
                print("Your Amount is zero or value less")

        #BANGLADESHI TAKA TO MYANMAR KYAT
        if option == 15:
            print("BANGLADESHI TAKA TO MYANMAR KYAT:")
            bdt=float(input("Enter the amount of taka="))
            mmk=18.18
            bdt_to_mmk=mmk*bdt
            if bdt>0:
                print(bdt,"Taka in Myanmar kyat","=",bdt_to_mmk)
            else:
                print("Your Amount is zero or value less")


        #MYANMAR KYAT TO BANGLADESHI TAKA
        if option == 16:
            print("MYANMAR KYAT TO BANGLADESHI TAKA:")
            mmk=float(input("Enter the amount of Myanmar kyat="))
            bdt=0.055
            mmk_to_bdt=bdt*mmk
            if mmk>0:
                print(mmk,"Myanmar kyat in Taka","=",mmk_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO NEPALESE RUPEE
        if option == 17:
            print("BANGLADESHI TAKA TO NEPALESE RUPEE:")
            bdt=float(input("Enter the amount of taka="))
            npr=1.35
            bdt_to_npr=npr*bdt
            if bdt>0:
                print(bdt,"Taka in Nepalese Rupee","=",bdt_to_npr)
            else:
                print("Your Amount is zero or value less")

        #NEPALESE RUPEE TO BANGLADESHI TAKA
        if option == 18:
            print("NEPALESE RUPEE TO BANGLADESHI TAKA:")
            npr=float(input("Enter the amount of Nepalese Rupee="))
            bdt=0.74
            npr_to_bdt=bdt*npr
            if npr>0:
                print(npr,"Nepalese Rupee in Taka","=",npr_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO KUWAITI DINAR
        if option == 19:
            print("BANGLADESHI TAKA TO KUWAITI DINAR:")
            bdt = float(input("Enter the amount of taka="))
            kwd = 0.0036
            bdt_to_kwd=kwd*bdt
            if bdt>0:
                print(bdt,"Taka in Kuwaiti Diner","=",bdt_to_kwd)
            else:
                print("Your Amount is zero or value less")

        #KUWAITI DINAR TO BANGLADESHI TAKA
        if option == 20:
            print("KUWAITI DINAR TO BANGLADESHI TAKA:")
            kwd=float(input("Enter the amount of Kuwaiti Diner="))
            bdt=276.20
            kwd_to_bdt=bdt*kwd
            if kwd>0:
                print(kwd,"Kuwaiti Diner in Taka","=",kwd_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO IRANIAN RIYAL
        if option == 21:
            print("BANGLADESHI TAKA TO IRANIAN RIYAL:")
            bdt=float(input("Enter the amount of taka="))
            irr=502.66
            bdt_to_irr=irr*bdt
            if bdt>0:
                print(bdt,"Taka in Iranian Riyal","=",bdt_to_irr)
            else:
                print("Your Amount is zero or value less")


        #IRANIAN RIYAL TO BANGLADESHI TAKA
        if option == 22:
            print("IRANIAN RIYAL TO BANGLADESHI TAKA:")
            irr=float(input("Enter the amount of Iranian Riyal="))
            bdt=0.0020
            irr_to_bdt=bdt*irr
            if irr>0:
                print(irr,"Iranian Riyal in Taka","=",irr_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO IRAQI DINAR
        if option == 23:
            print("BANGLADESHI TAKA TO IRAQI DINAR:")
            bdt=float(input("Enter the amount of taka="))
            iqd=14.22
            bdt_to_iqd=iqd*bdt
            if bdt>0:
                print(bdt,"Taka in Iraqi Dinar","=",bdt_to_iqd)
            else:
                print("Your Amount is zero or value less")

        #IRAQI DINAR TO BANGLADESHI TAKA
        if option == 24:
            print("IRAQI DINAR TO BANGLADESHI TAKA:")
            iqd=float(input("Enter the amount of Iraqi Dinar="))
            bdt=0.070
            iqd_to_bdt=bdt*iqd
            if iqd>0:
                print(iqd,"Iraqi Dinar in Taka","=",iqd_to_bdt)
            else:
                print("Your Amount is zero or value less")


        #BANGLADESHI TAKA TO QATARI RIYAL
        if option == 25:
            print("BANGLADESHI TAKA TO QATARI RIYAL:")
            bdt=float(input("Enter the amount of taka="))
            qar=0.043
            bdt_to_qar=qar*bdt
            if bdt>0:
                print(bdt,"Taka in Qatari Riyal","=",bdt_to_qar)
            else:
                print("Your Amount is zero or value less")


        #QATARI RIYAL TO BANGLADESHI TAKA
        if option == 26:
            print("QATARI RIYAL TO BANGLADESHI TAKA:")
            qar=float(input("Enter the amount of Qatari Riyal="))
            bdt=23.00
            qar_to_bdt=bdt*qar
            if qar>0:
                print(qar,"Qatari Riyal in Taka","=",qar_to_bdt)
            else:
                print("Your Amount is zero or value less")
    except:
        print("Sorry!\nKindly Check Or Try Again After Sometimes")
    return None
currancy()