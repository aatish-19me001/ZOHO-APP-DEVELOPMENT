print("===================================================================WELCOME TO AMAZON ONLINE SHOPPING===================================================================")
username="aadhi"
password=17
vendors=[{"name":"dev","password":1111,"vndrid":"V1001"},{"name":"giri","password":2222,"vndrid":"V1002"},{"name":"koolu","password":3333,"vndrid":"V1003"},{"name":"senthil","password":1201,"vndrid":"V1004"}]
waitvend=[]
suspvend=[]
rjctvend=[]
buyers={"adi":3103,"snake":3007,"gopu":1510}
products=[{"name":"uppers","type":"casuals","brand":"adidas","id":"P001","vndrid":"V1001","stock":"100","price without discount":1250,"price with discount":1000,"discount%":25,"ratings":4.4,"no of voters":100},
          {"name":"hoodies","type":"casuals","brand":"puma","id":"P002","vndrid":"V1002","stock":"100","price without discount":2000,"price with discount":1200,"discount%":20,"ratings":4.6,"no of voters":120},
          {"name":"slippers","type":"casuals","brand":"crocs","id":"P003","vndrid":"V1001","stock":"10","price without discount":1300,"price with discount":1000,"discount%":30,"ratings":4.5,"no of voters":80},
          {"name":"shoes","type":"casuals","brand":"sparx","id":"P004","vndrid":"V1002","stock":"200","price without discount":1000,"price with discount":750,"discount%":33.3,"ratings":4.8,"no of voters":50},
          {"name":"tracks","type":"casuals","brand":"nike","id":"P005","vndrid":"V1003","stock":"300","price without discount":1800,"price with discount":1500,"discount%":20,"ratings":4.7,"no of voters":150},
          {"name":"slippers","type":"casuals","brand":"paragon","id":"P006","vndrid":"V1001","stock":"500","price without discount":1500,"price with discount":1000,"discount%":50,"ratings":3.8,"no of voters":40},
          {"name":"shirts","type":"formals","brand":"adidas","id":"P007","vndrid":"V1001","stock":"40","price without discount":1250,"price with discount":1000,"discount%":25,"ratings":4.4,"no of voters":105},
          {"name":"t-shirs","type":"formals","brand":"puma","id":"P008","vndrid":"V1002","stock":"30","price without discount":1320,"price with discount":1200,"discount%":10,"ratings":4.6,"no of voters":150},
          {"name":"shoes","type":"formals","brand":"bata","id":"P009","vndrid":"V1003","stock":"50","price without discount":1200,"price with discount":1000,"discount%":20,"ratings":4.5,"no of voters":72},
          {"name":"pants","type":"formals","brand":"nike","id":"P010","vndrid":"V1003","stock":"40","price without discount":1500,"price with discount":1200,"discount%":25,"ratings":4.7,"no of voters":80},
          {"name":"belts","type":"formals","brand":"levis","id":"P011","vndrid":"V1002","stock":"100","price without discount":1000,"price with discount":800,"discount%":25,"ratings":4.0,"no of voters":59}]
orders={"adi":"P001","snake":"P004"}

def vndrrmv():
    while True:
        gg=input("ENTER VENDOR NAME :")
        hh=input("ENTER A NUMBER PASSWORD :")
        for ra in vendors:
            if ra["name"]==gg and ra["password"]==hh:
                ii=vendors.index(ra)
                vendors.pop(ii)
                suspvend.append(ii)
                print("THE ACCOUNT WAS SUSPENDED\nKINDLY INFORM TO THE VENDOR\nTHANK YOU!")
                print("SUSPENDED VENDORS :",suspvend)
                return adminwrk()
            else:
                print("SORRY!\nACCOUNT DOES NOT EXISTS")
                return adminwrk()
            
def vndradd():
    while True:
        cc=input("ENTER VENDOR NAME :")
        dd=input("ENTER A NUMBER PASSWORD :")
        for ar in vendors:
            if ar["name"]!=cc and ar["password"]!=dd:
                len2=len(vendors)
                ff='V'+str(1001+len2)
                l={"name":cc,"password":dd,"vndrid":ff}
                vendors.append(l)
                print("THE ACCOUNT WAS CREATED\nKINDLY INFORM TO THE VENDOR\nTHE VENDOR ID IS",ff,"THANK YOU!")
                print("CURRENT VENDORS :",vendors)
                return adminwrk()
            else:
                print("SORRY!\nACCOUNT ALREADY EXISTS")
                return adminwrk()

def approval():
    while True:
        if len(waitvend)!=0:
            print("GOOD JOB\nTHERE IS A VENDOR REQUEST")
            for sa in waitvend:
                print(waitvend[0])
                k=int(input("****VENDOR REQUEST LIST****\n    1-ACCEPT\n    2-REJECT\nCAREFULLY ENTER YOUR CHOICE :"))
                if (k==1):
                    jj=waitvend.index(sa)
                    waitvend.pop(jj)
                    vendors.append(jj)
                    print("THE ACCOUNT WAS APPROVED SUCCESSFULLY\nTHANK YOU!")
                    print("CURRENT VENDORS :",vendors)
                    return approval()
                elif (k==2):
                    kk=waitvend.index(sa)
                    waitvend.pop(kk)
                    rjctvend.append(kk)
                    print("THE ACCOUNT WAS NOT APPROVED\nTHANK YOU!")
                    print("REJECTED VENDORS :",rjctvend)
                    return approval()
                else:
                    print("PLEASE ENTER VALID INPUT")
                    return adminwrk()
        else:
            print("NO REQUESTS HERE\nKINDLY COME BACK LATER")

def adminwrk():
    b=int(input("****ADMIN****\n    1-APPROVE VENDOR\n    2-ADD VENDOR\n    3-REMOVE VENDOR\nENTER YOUR CHOICE :"))
    if (b==1):
        approval()
    elif (b==2):
        vndradd()
    elif (b==3):
        vndrrmv()
    else:
        print("THANK YOU FOR COMING")
        return amazon()

def admin():
    while True:
        un=input("ENTER THE USERNAME :")
        pw=int(input("ENTER THE PASSWORD :"))
        if (un==username) and (pw==password):
            adminwrk()
        else:
            print("SORRY\nUSERNAME OR PASSWORD INCORRECT")
            return amazon()

def prdctadd(aw):
    while True:
        print("XXXX WARNING XXXX")
        print("*****ENTER DETAILS CAREFULLY****\n****KINDLY REFER THE EXAMPLES****")
        pa=input("ENTER PRODUCT NAME(Eg.:SHIRTS,PANTS,etc..,) :")
        pb=input("ENTER PRODUCT TYPE(Eg.:FORMALS,CASUALS,etc..,):")
        pc=input("ENTER PRODUCT BRAND(Eg.:PUMA,NIKE,etc..,) :")
        pca=aw
        pd=int(input("ENTER PRODUCT STOCK(Eg.:100,200,etc..,) :"))
        pe=int(input("ENTER PRODUCT PRICE WITHOUT DISCOUNT(Eg.:1000,500,etc..,) :"))
        pf=int(input("ENTER PRODUCT PRICE WITH DISCOUNT(Eg.:800,450,etc..,)(SHOULD BE LESSER THAN THE PRICE WITHOUT DISCOUNT) :"))
        pg=float(input("ENTER PRODUCT RATING(Eg.:4.0,4.2,3.7,etc..,)(SHOULD BE LESSER THAN 5(>5.0))(SHOULD HAVE A SINGLE DECIMAL VALUE) :"))
        ph=int(input("ENTER THE NO. OF VOTERS(Eg.:55,68,etc..,) :"))
        dpd=pe-pf
        dp=(dpd/pf)*100
        pdp=round(dp,2)
        len3=len(products)
        pi='P0'+str(000+(len3+1))
        pj={"name":pa,"type":pb,"brand":pc,"id":pi,"vndrid":pca,"stock":pd,"price without discount":pe,"price with discount":pf,"discount%":pdp,"ratings":pg,"no of voters":ph}
        products.append(pj)
        print("PRODUCT",pa,"ADDED SUCCESSFULLY")
        print("THE CURRENT LIST OF PRODUCTS IS",products)
        pk=int(input("OKAY!WHAT'S NEXT\n    1-ADD ONE MORE PRODUCT\n    2-ADD PRODUCT LATER\nENTER YOUR CHOICE:"))
        if pk==1 :
            return prdctadd(aw)
        elif pk==2 :
            return vndrwrk(aw)
        else:
            return vendor()

def prdctrmv(aw):
    while True:
        print("XXXX PRODUCT REMOVAL PAGE XXXX")
        for pn in products:
            if pn["vndrid"]==aw:
                pl=input("ENTER PRODUCT ID(Eg.:10,11,etc..,) :")
                pm='P0'+str(pl)
                if pn['id']==pm:
                    products.pop(pn)
                    print("PRODUCT REMOVED SUCCESSFULLY\nWHAT'S NEXT!")
                    pq=int(input("    1-REMOVE PRODUCT\n    2-ADD PRODUCT\n    ENTER YOUR CHOICE :"))
                    if (pq==1):
                        return prdctrmv(aw)
                    elif (pq==2):
                        return prdctadd(aw)
                    else:
                        return vendor()
                else:
                    print("NO SUCH PRODUCT IN THAT ID")
                    return prdctrmv(aw)
            else:
                print("NO PRODUCTS FOUND")
                return vndrwrk(aw)

def vndrwrk(aw):
    while True:
        l=int(input("    1-ADD PRODUCT\n    2-REMOVE PRODUCT\nENTER YOUR CHOICE :"))
        if (l==1):
            print("****ADD PRODUCT****")
            prdctadd(aw)
        elif (l==2):
            print("****REMOVE PRODUCT****")
            prdctrmv(aw)
        else:
            print("THANK YOU FOR COMING")
            break
        
def newvndr():
    while True:
        h=input("ENTER YOUR NAME :")
        i=input("ENTER A NUMBER PASSWORD :")
        for bye in vendors:
            if bye["name"]!=h and bye["password"]!=i:
                len1=len(vendors)+len(waitvend)
                ee='V'+str(1001+len1)
                k={"name":h,"password":i,"vndrid":ee}
                waitvend.append(k)
                print("YOUR ACCOUNT WAS GENERATED\nPLEASE WAIT FOR ADMIN APPROVAL\nYOUR VENDOR ID IS",ee,"\nTHANK YOU!")
                return vendor()
            else:
                print("SORRY\nACCOUNT ALREADY EXISTS")

def existvndr():
    while True:
        usn=input("ENTER THE USERNAME :")
        paw=int(input("ENTER THE PASSWORD :"))
        for hi in vendors:
            if hi['name']==usn and hi['password']==paw:
                print("WELCOME BACK",usn)
                print("VERIFY YOUR DETAILS :",hi)
                aw=hi['vndrid']
                print("YOUR VENDOR ID IS",aw)
                vndrwrk(aw)
            else:
                for hii in waitvend:
                    if hii['name']==usn and hii['password']==paw:
                        print("SORRY\nYOUR ACCOUNT IS WAITING FOR ADMIN APPROVAL")
                        return vendor()
                    else:
                        for hiii in suspvend:
                            if hiii['name']==usn and hiii['password']==paw:
                                print("SORRY\nYOUR ACCOUNT IS SUSPENDED")
                                return amazon()
                            else:
                                print("SORRY\nYOUR ACCOUNT IS REJECTED")
                                return amazon()

def vendor():
    while True:
        c=int(input("****VENDOR****\n    1-NEW VENDOR\n    2-EXISTING VENDOR\nENTER YOUR CHOICE :"))
        if (c==1):
            newvndr()
        elif (c==2):
            existvndr()
        else:
            print("THANK YOU FOR COMING")
            return amazon()

def buyprdct(aa):
    global orders
    while True:
        print("**** PRODUCT BUYING PAGE ***")
        bb=input("ENTER THE PRODUCT :")
        for bc in products:
            if bc['name']==bb:
                bd=bc['id']
                print(bd)
                bf=bc['price with discount']
                be=int(input("DO YOU WANT TO BUY THIS PRODUCT\n    1-YES\n    2-NO\nENTER YOUR CHOICE :"))
                if (be==1):
                    print("THE PRICE OF THE PRODUCT IS:",bf)
                    bg=int(input("DO YOU WANT TO PLACE ORDER FOR THIS PRODUCT\n    0-NO\n    OTHERS-YES\nENTER YOUR CHOICE :"))
                    if (bg==0):
                        print("ORDER NOT PLACED!")
                        bh=int(input("WHAT'S NEXT?\n    1-BUY A DIFFERENT PRODUCT\n    2-BUY PRODUCT LATER\nENTER YOUR CHOICE :"))
                        if (bh==1):
                            return buyprdct(aa)
                        elif (bh==2):
                            return buyer()
                        else:
                            return amazon()
                    else:
                        orders[aa]=bd
                        print("YOUR ORDER WORTH",bf,"PLACED SUCCESSFULLY!")
                        print("KINDLY REMEMBER THE PRODUCT ID (",bd,") FOR FUTURE USE\nTHANK YOU!")
                        print("YOUR PRODUCT WILL BE DELIVERED WITHIN 7 DAYS AFTER PURCHASE")
                        return buyrwrk(aa)
                elif (be==2):
                    return buyprdct(aa)
                else:
                    return buyer()
            else:
                print("PRODUCT NOT FOUND\nTRY ANOTHER PRODUCT")
                return buyrwrk(aa)

def cnclordr(aa):
    global orders
    while True:
        bi=int(input("ENTER YOUR PRODUCT ID(REF:01,12,etc..,) :"))
        bj="P0"+str(bi)
        if (aa,bj) in orders.items:
            del orders["aa"]
            print("ORDER CANCELLED SUCCESSFULLY!")
            return buyrwrk()
        else :
            print("SORRY\nINVALID PRODUCT ID")
            return buyrwrk()

def buyrwrk(aa):
    while True:
        ba=int(input("WELCOME BUYER\n    1-BUY PRODUCT\n    2-CANCEL ORDER\nENTER YOUR CHOICE :"))
        if (ba==1):
            buyprdct(aa)
        elif (ba==2):
            cnclordr(aa)
        else:
            return buyer()

def newbuyr():
    global buyers
    while True:
        e=input("ENTER YOUR NAME :")
        f=input("ENTER A 4-DIGIT NUMBER PASSWORD :")
        g=input("RE-ENTER YOUR PASSWORD :")
        if (e,f) not in buyers.items():
            if (f==g):
                if (len(f)==4):
                    print("YOUR ACCOUNT IS CREATED SUCCESSFULLY\nTHANK YOU!")
                    buyers[e]=f
                    return buyer()
                else:
                    print("SORRY\nYOUR PASSWORD SHOULD CONTAIN ONLY FOUR CHARACTERS")
            else:
                print("SORRY\nYOUR PASSWORDS AREN'T SAME")
        else:
            print("SORRY\nYOUR ACCOUNT IS ALREADY EXISTING")

def existbuyr():
    global buyers
    while True:
        aa=input("ENTER THE USERNAME :")
        bb=int(input("ENTER YOUR PASSWORD :"))
        if (aa,bb) in buyers.items():
            print("WELCOME BACK",aa)
            buyrwrk(aa)
        else:
            print("SORRY!\nUSERNAME OR PASSWORD INCORRECT")

def buyer():
    while True:
        d=int(input("****BUYER****\n    1-NEW BUYER\n    2-EXISTING BUYER\nENTER YOUR CHOICE :"))
        if (d==1):
            newbuyr()
        elif (d==2):
            existbuyr()
        else:
            print("THANK YOU FOR COMING")
            break

def amazon():
    while True:
        a=int(input("****AMAZON****\n    1-ADMIN\n    2-VENDOR\n    3-BUYER\nENTER YOUR CHOICE :"))
        if (a==1):
            admin()
        elif (a==2):
            vendor()
        elif (a==3):
            buyer()
        else:
            print("THANK YOU FOR COMING")
            break
amazon()
