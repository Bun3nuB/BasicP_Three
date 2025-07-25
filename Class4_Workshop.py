
Movielist = [
        {"Movie":"Avegy : The Buffet War","Price":180,"Rate":"R","Genre":"History"},
        {"Movie":"Hatman The Kitten Knight","Price":190,"Rate":"G","Genre":"Action"},
        {"Movie":"HatMan vs SuperSigmaMan","Price":170,"Rate":"PG-13","Genre":"Romance"},
        {"Movie":"Avegy:EndGay","Price":200,"Rate":"NC-17","Genre":"Fantasy"},
        {"Movie":"CaptianCambodia:The First Avegy","Price":190,"Rate":"G","Genre":"Fantasy"},
        {"Movie":"WhitePolar : dawakan Forever","Price":185,"Rate":"PG-13","Genre":"Comedy"},
    ]
def MovieList():
    print("============================{ MovieList }============================")
    for movie in Movielist:
        print(f"{movie['Movie']} : Rate {movie['Rate']}  : {movie['Price']} Bath : {movie['Genre']}")
        print("====================================================================")
def Buyticket():
    CanWatch = True
    print("============BuyTicket============")
    B = 0
    for movie in Movielist:
        B += 1
        print(f"{B}. ",movie["Movie"])
    MovieChioce = int(input("ท่านจะดูหนังเรื่องไหน :"))
    print("Movie :", Movielist[MovieChioce-1]["Movie"])
    Age = int(input("ท่านอายุเท่าไหร่ :"))
    if Age < 18 and Movielist[MovieChioce-1]["Rate"] == "NC-17":
        CanWatch = False
    elif Age < 18 and Movielist[MovieChioce-1]["Rate"] == "R":
        print("ท่านควรได้รับคำแนะนำจากผู้ปกครองก่อนดูหนังเรื่องนี้")
    elif Age < 13 and Movielist[MovieChioce-1]["Rate"] == "PG-13":
        print("ท่านควรได้รับคำแนะนำจากผู้ปกครองก่อนดูหนังเรื่องนี้")
    else:
        print("ท่านสามารถดูหนังเรื่องนี้ได้")
    if CanWatch:
        while True:
            print("============Choicedub============")
            Voicedub = int(input("1: Thai \n2: English\nท่านต้องการดูภาษาอะไร :"))
            if Voicedub == 1:
                print("ท่านเลือกดูหนังเสียงพากย์ไทย")
                Movielist[MovieChioce-1]["Dub"] = "Thai"
                break
            elif Voicedub == 2:
                print("ท่านเลือกดูหนังเสียงพากย์อังกฤษ")
                Movielist[MovieChioce-1]["Dub"] = "English"
                break
            else:
                print("ท่านเลือกผิด")
        if  Movielist[MovieChioce-1]["Genre"] == "Fantasy":
            print("============UpPrice============")
            print("ท่านเลือกหนังแนว Fantasy")
            Movielist[MovieChioce-1]["Price"] += 50
            print(f"หนังเรื่อง {Movielist[MovieChioce-1]['Movie']} มีการปรับราคาใหม่เป็น {Movielist[MovieChioce-1]['Price']} บาท เพราะเป็นหนังแนวแฟนตาซี")
        print("============Ticket Information============")
        print(f"=================================================================================== \n=")
        print(f"=      Movie Name : {Movielist[MovieChioce-1]['Movie']}         Rate : {Movielist[MovieChioce-1]['Rate']}        ")
        print(f"=")
        print(f"=      Age : {Age} Year Old          Dub : {Movielist[MovieChioce-1]['Dub']}        ")
        print(f"=")
        print(f"=      Price : {Movielist[MovieChioce-1]['Price']} Bath          Genre : {Movielist[MovieChioce-1]['Genre']}       \n=")
        print(f"===================================================================================")
        print("ท่านสามารถชำระเงินได้ที่เคาเตอร์")
    else:
        print("ท่านไม่สามารถดูหนังเรื่องนี้ได้")
def Menu():
    while True:
        menuChoice = int(input("=====ยินดีต้อนรับสู่Ohio Cinema=====\n1: แสดงหนังทั้งหมด \n2: ซื้อตั่วหนัง \nท่านต้องการจะทำอะไร :"))
        if menuChoice == 1:
            MovieList()
        elif menuChoice == 2:
            Buyticket()
            break
Menu()
    
    

    
    



    
    