
Movielist = [
        {"Movie":"Avegy : The Buffet War","Price":180,"Rate":"R"},
        {"Movie":"Hatman The Kitten Knight","Price":190,"Rate":"G"},
        {"Movie":"HatMan vs SuperSigmaMan","Price":170,"Rate":"PG-13"},
        {"Movie":"Avegy:EndGay","Price":200,"Rate":"NC-17"},
        {"Movie":"CaptianCambodia:The First Avegy","Price":190,"Rate":"G"},
        {"Movie":"WhitePolar : dawakan Forever","Price":185,"Rate":"PG-13"}
    ]

def MovieList():
    print("============MovieList============")
    for movie in Movielist:
        print(movie["Movie"]," : Rate",movie["Rate"] ," : ",movie["Price"],"Bath")
        print("====================================================")
def Buyticket():
    print("============BuyTicket============")
    B = 0
    for movie in Movielist:
        B += 1
        print(f"{B}. ",movie["Movie"])
    MovieChioce = int(input("ท่านจะซื้อตั่วหนังเรื่องไหน :"))
    print("Movie :", Movielist[MovieChioce-1]["Movie"])
    
def Menu():
    menuChoice = int(input("=====ยินดีต้อนรับสู่Ohio Cinema=====\n1: แสดงหนังทั้งหมด \n2: ซื้อตั่วหนัง \nท่านต้องการจะทำอะไร :"))
    if menuChoice == 1:
        MovieList()
    elif menuChoice == 2:
        Buyticket()
        
while True:
    Menu()
    break
    

    
    



    
    