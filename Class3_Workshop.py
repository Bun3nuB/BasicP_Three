
while True:
    MonsterDead = False
    totalDamage = 0
    Revivecount = 0
    ChoiceGoblin = False
    ChoiceDragon = False
    ChoiceMinotaur = False
    ChoiceLichKing = False
    MonsterEffect = ""
    SwordDamage = 20
    Axe = 35
    Gun = 45
    print("-----ยินดีต้อนรับนักผจญภัยทุกท่าน-----")
    menuChoice = int(input("ท่านจะทำอะไร (1: สู้กับมอนสเตอร์, 2: ออกจากเกม): "))
    if(menuChoice == 1):
        while True:
            print("===========เลือกบอส=========== \n 1.มังกร \n ไม่มีความสามารถพิเศษแต่มีพลังชีวิตจำนวนมาก")
            print("=============================\n2.ราชาก็อบลิน \n คุณถูกขโมยอาวุธปืน")
            print("=============================\n3.มิโนทอร์ \n หนังที่หนาทำให้ดาเมจลดลง 10 หน่วย")
            print("=============================\n4.ลิชคิง \n บังคับให้คุณต่อสู้กับมันใน 6 รอบเท่านั้น\n=============================")
            Monsterchoice = int(input("ท่านต้องการที่จะเผชิญหน้ากับมอนสเตอร์ตัวไหน :"))
            if(Monsterchoice == 1):
                Monstername = "มังกร"
                MonsterHP = 250.0
                ChoiceDragon = True
                MonsterEffect = "ไม่มีความสามารถพิเศษแต่มีพลังชีวิตจำนวนมาก"
                break
            elif Monsterchoice == 2:
                Monstername = "ราชาก็อบลิน"
                MonsterHP = 150.0
                ChoiceGoblin = True
                MonsterEffect  = "คุณถูกขโมยอาวุธปืน"
                break
            elif Monsterchoice == 3:
                Monstername = "มิโนทอร์"
                MonsterHP = 175.0
                ChoiceMinotaur = True
                MonsterEffect = "หนังที่หนาทำให้ดาเมจลดลง 10 หน่วย"
                SwordDamage -= 10
                Axe -= 10
                Gun -= 10
                break
            elif Monsterchoice == 4:
                Monstername = "ลิชคิง"
                MonsterHP = 145.0
                ChoiceLichKing = True
                MonsterEffect = "บังคับให้คุณต่อสู้กับมันใน 6 รอบเท่านั้น"
                break
            else:
                print("ใส่ข้อมูลผิดพลาด โปรดลองใหม่")
        print(f"=====Event===== \nท่านพบกับ{Monstername} {Monstername}ตัวนี้มีเลือดทั้งหมด {MonsterHP} หน่วย")
        HitRound = int(input(f"คุณต้องการจะตีกับ{Monstername}กี่รอบ :"))
        if(ChoiceLichKing):
            HitRound = 6
            print(Monstername,MonsterEffect)
        print(f"ท่านจะสู้กับ{Monstername} ทั้งหมด{HitRound} รอบ")
        for i in range(1,HitRound+1):
                Run = input(f"=====หลบหนี===== \nท่านต้องการที่จะหลบหนีจาก{Monstername}หรือไม่(1 = ใช่ หรือ 2 = ไม่ :)")
                if Run == "1":
                    print(f"ท่านได้หลบหนีจาก{Monstername}")
                    break
                elif Run == "2":
                    if(ChoiceGoblin == True):
                        Gun = 0
                        print(f"=====เลือกอาวุธ=====\n{MonsterEffect}\nท่านเลือกที่จะต่อสู้ยืนหยัดกับ{Monstername} \nรอบที่ {i}\n1.ดาบ(20 ดาเมจ)\n2.ขวาน(35 ดาเมจ)")
                    else:
                        print(f"=====เลือกอาวุธ===== \nท่านเลือกที่จะต่อสู้ยืนหยัดกับ{Monstername} \nรอบที่ {i} \n1.ดาบ(20 ดาเมจ) \n2.ขวาน(35 ดาเมจ) \n3.ปืน(45 ดาเมจ)")
                        if(ChoiceMinotaur):
                            print("มิโนทอร์หนังหนาตีไม่เข้าจะลดดาเมจที่คุณทำได้ 10 หน่วย")
                    while True:
                        Weapon = int(input(f"โปรดเลือกอาวุธที่ท่านจะใช้ต่อสู้กับ{Monstername}:"))
                        if(Weapon == 1 ):
                            MonsterHP -= SwordDamage
                            totalDamage += SwordDamage
                            break
                        elif Weapon == 2:
                            MonsterHP -= Axe
                            totalDamage += Axe
                            break
                        elif Weapon == 3 and ChoiceGoblin == False:
                            MonsterHP -= Gun
                            totalDamage += Gun
                            break
                        else:
                            print("ใส่ข้อมูลผิดพลาดลองใหม่")
                    print(f"{Monstername}เหลือเลือดทั้งหมด {MonsterHP} หน่วย")
                    if(MonsterHP == 0):
                        MonsterDead = True
                        break
                    elif MonsterHP < 0:
                        MonsterHP = 20
                        Revivecount += 1
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
        fightReport = int(input("ต้องการดูรายงานการต่อสู้หรือไม่ (1 = ใช่, 2 = ไม่): "))
        if(fightReport == 1):
            print("=====รายงานการต่อสู้=====")
            print(f"จำนวนรอบที่สู้: {i}\nมอนสเตอร์ที่คุณต่อสู้: {Monstername}\nความเสียหายทั้งหมดที่คุณทำ: {totalDamage}\nจำนวนครั้งที่มอนสเตอร์ฟื้นคืนชีพ: {Revivecount}")
    elif(menuChoice == 2):
        break
    else:
        print("ใส่ข้อมูลผิดพลาด กรุณาใส่ใหม่")
print("ขอบคุณที่มาเล่นเกมนี้")



