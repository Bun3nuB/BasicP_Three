MonsterHP = 200.0
Monstername = "มังกร"
SwordDamage = 15.5
Axe = 24.5
Gun = 45
MonsterDead = False

print("-----ยินดีต้อนรับนักผจญภัยทุกท่าน-----")
while True:
    menuChoice = int(input("ท่านจะทำอะไร (1: สู้กับมอนสเตอร์, 2: ออกจากเกม): "))
    if(menuChoice == 1):
        print(f"ท่านพบกับ{Monstername} {Monstername}ตัวนี้มีเลือดทั้งหมด {MonsterHP} หน่วย")
        HitRound = int(input(f"คุณต้องการจะตีกับ{Monstername}กี่รอบ :"))
        print(f"ท่านจะสู้กับ{Monstername} ทั้งหมด{HitRound} รอบ")
        for i in range(1,HitRound+1):
                Run = input(f"ท่านต้องการที่จะหลบหนีจาก{Monstername}หรือไม่(1 = ใช่ หรือ 2 = ไม่ :)")
                if Run == "1":
                    print(f"ท่านได้หลบหนีจาก{Monstername}")
                    break
                elif Run == "2":
                    print(f"ท่านเลือกที่จะต่อสู้ยืนหยัดกับ{Monstername}")
                    print(f"รอบที่ {i}")
                    print("1.ดาบ(20 ดาเมจ)")
                    print("2.ขวาน(24.5 ดาเมจ)")
                    print("3.ปืน(45 ดาเมจ)")
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
                        print(f"{Monstername} กลับมามีพลังอีกครั้ง!")
                        print(f"เลือด {Monstername} กลับมาที่ {MonsterHP} หน่วย")
                else:
                    print("ใส่ข้อมูลผิดพลาด ลองใหม่")
        if(MonsterDead == True):
            print("ยินดีด้วย คุณชนะเกมนี้แล้ววว")
        elif(MonsterDead == False):
            print("หมดเวลาแล้วว!")
            print("เสียใจด้วยคล้ายหน้าเอาใหม่นะ")
    elif(menuChoice == 2):
        break
    else:
        print("ใส่ข้อมูลผิดพลาด กรุณาใส่ใหม่")
print("ขอบคุณที่มาเล่นเกมนี้")



