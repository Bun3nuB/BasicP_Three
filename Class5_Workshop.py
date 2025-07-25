lottos = [
    {"Number":"027394","Stock":6},
    {"Number":"134567","Stock":8},
    {"Number":"129508","Stock":7},
    {"Number":"340721","Stock":9},
    {"Number":"568930","Stock":5},
    {"Number":"782114","Stock":6},
    {"Number":"905336","Stock":7},
    {"Number":"112245","Stock":8},
    {"Number":"223456","Stock":9},
    {"Number":"230089","Stock":10},
    {"Number":"449001","Stock":8},
    {"Number":"699875","Stock":9},
    {"Number":"986396","Stock":10}
]

def Menu():
    while True:
        menuChoice = int(input("=====ยินดีต้อนรับสู่ ITSantis999=====\n1: แสดงLottoryทั้งหมด \n2: ซื้อLottory \nท่านต้องการจะทำอะไร :"))
        if menuChoice == 1:
                lottoList()
                
        elif menuChoice == 2:
                Buylotto()
                break
        else:
             print ("ใส่ดีๆ")
def Buylotto():
    while True:
        i = 0
        for lotto in lottos:
            i += 1
            print(f"{i}. {lotto['Number']}")
            print("========================")
        buy_number = int(input("กรุณาใส่หมายเลข :"))
        if(0 < buy_number <= 13):
            numberchoice = lottos[buy_number-1]["Number"]
            StockChoice = lottos[buy_number-1]["Stock"]
            print(f"ท่านเลือก หมายเลข :{numberchoice}")
            break
        else:
             print("ใส่เลขผิด ลองใหม่")
    print("==============Stock==============")
    while True:  
        print(f"ท่านได้เลือก {numberchoice} มีจำนวนทั้งหมด {StockChoice} ใบ")
        chooseStock = int(input("1.ชุด \n2.ใบเดียว \nท่านจะซื้อแบบไหน : "))
        if(chooseStock == 1):
            print(f"ท่านได้เลือกซื้อแบบชุด")
            Howmany = int(input("ท่านจะซื้อกี่ใบ :"))
            if(Howmany > StockChoice):
                 print("เรามีจำนวนไม่พอ ใส่ใหม่")
            elif(0 < Howmany <= StockChoice):
                 print(f"ท่านได้ซื้อ {numberchoice} เป็นจำนวน {Howmany} ใบ")
                 StockChoice -= Howmany
                 break
            else:
                 print("ใส่ดีๆ ระวังตีน") 
        elif(chooseStock == 2):
            print(f"ท่านได้ซื้อ {numberchoice} 1 ใบ")
            Howmany = 1
            StockChoice -= Howmany
            break
        else:
             print("กรอกใหม่")
    print("==========Pay==========")
    while True:
         Pay = int(input(f"ชำระเงินเลยไหม \n1.Yes/2.No :"))
         if(Pay == 1):
              print("=========Bill=========")
              print(f"ท่านได้ซื้อ {numberchoice} เป็นจำนวน {Howmany} ใบ และราคาทั้งหมดคือ {Howmany* 80} บาท")
              print("ขอบคุณที่ใช้บริการ")
              break
         elif(Pay == 2):
              print("ไม่ซื้อไม่เป็นไร แต่ห้ามกวนตีน")
              break
         else:
            print("ใส่ดีๆระวังหน้า")
              
              
    return
def lottoList():
    print("==================LottoList==================")
    for Lotto in lottos:
         print(f"เลขหวย : {Lotto['Number']} มีจำนวน {Lotto['Stock']} ใบ")
         print("============================================")
Menu()