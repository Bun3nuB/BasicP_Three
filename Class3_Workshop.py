MonsterHP = 0
Monstername = ""
SwordDamage = 20
Axe = 25
Gun = 45
MonsterDead = False

print("-----ยินดีต้อนรับนักผจญภัยทุกท่าน-----")
while True:
    menuChoice = int(input("ท่านจะทำอะไร (1: สู้กับมอนสเตอร์, 2: ออกจากเกม): "))
    if(menuChoice == 1):
        while True:
            Monsterchoice = int(input("1.มังกร \n2.ราชาก็อบลิน \n3.มิโนทอร์ \n4.ลิชคิง \nท่านต้องการที่จะเผชิญหน้ากับมอนสเตอร์ตัวไหน :"))
            if(Monsterchoice == 1):
                Monstername = "มังกร"
                MonsterHP = 200.0
                break
            elif Monsterchoice == 2:
                Monstername = "ราชาก็อบลิน"
                MonsterHP = 150.0
                break
            elif Monsterchoice == 3:
                Monstername = "มิโนทอร์"
                MonsterHP = 175.0
                break
            elif Monsterchoice == 4:
                Monstername = "ลิชคิง"
                MonsterHP = 145.0
                break
            else:
                print("ใส่ข้อมูลผิดพลาด โปรดลองใหม่")
        print(f"ท่านพบกับ{Monstername} {Monstername}ตัวนี้มีเลือดทั้งหมด {MonsterHP} หน่วย")
        HitRound = int(input(f"คุณต้องการจะตีกับ{Monstername}กี่รอบ :"))
        print(f"ท่านจะสู้กับ{Monstername} ทั้งหมด{HitRound} รอบ")
        for i in range(1,HitRound+1):
                Run = input(f"ท่านต้องการที่จะหลบหนีจาก{Monstername}หรือไม่(1 = ใช่ หรือ 2 = ไม่ :)")
                if Run == "1":
                    print(f"ท่านได้หลบหนีจาก{Monstername}")
                    break
                elif Run == "2":
                    print(f"ท่านเลือกที่จะต่อสู้ยืนหยัดกับ{Monstername} \nรอบที่ {i} \n1.ดาบ(20 ดาเมจ) \n2.ขวาน(25 ดาเมจ) \n3.ปืน(45 ดาเมจ)")
                    while True:
                        Weapon = int(input(f"โปรดเลือกอาวุธที่ท่านจะใช้ต่อสู้กับ{Monstername}:)"))
                        if(Weapon == 1):
                            MonsterHP -= SwordDamage
                            break
                        elif Weapon == 2:
                            MonsterHP -= Axe
                            break
                        elif Weapon == 3:
                            MonsterHP -= Gun
                            break
                        else:
                            print("ใส่ข้อมูลผิดพลาดลองใหม่")
                    print(f"{Monstername}เหลือเลือกทั้งหมด {MonsterHP} หน่วย")
                    if(MonsterHP == 0):
                        MonsterDead = True
                        break
                    if(MonsterHP < 0):
                        MonsterHP = 20
                        print(f"{Monstername} กลับมามีพลังอีกครั้ง! \nเลือด {Monstername} กลับมาที่ {MonsterHP} หน่วย")
                else:
                    print("ใส่ข้อมูลผิดพลาด ลองใหม่")
        print("=========จบเกม=========")
        if(MonsterDead == True):
            print(f"คุณฆ่า {Monstername} ได้สำเร็จ \nยินดีด้วย คุณชนะเกมนี้แล้ววว")
        elif Run == "1":
            print(f"ท่านหลบหนีจาก {Monstername} สำเร็จ")
        elif(MonsterDead == False):
            print(f"คุณถูก{Monstername}ฆ่าตาย! \nเสียใจด้วยคล้ายหน้าเอาใหม่นะ")
    elif(menuChoice == 2):
        break
    else:
        print("ใส่ข้อมูลผิดพลาด กรุณาใส่ใหม่")
print("ขอบคุณที่มาเล่นเกมนี้")



