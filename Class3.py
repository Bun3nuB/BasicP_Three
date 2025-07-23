def Nestif():
    IHAVERICE = input("มีข้าวหรือไม่ (1 = True/2 = False): ") == "1"
    IHAVESPOON = input("มีช้อนหรือไม่ (1 = True/2 = False): ") == "1"
    if IHAVERICE:
        print("มีข้าวแล้ว")
        if IHAVESPOON:
            print("มีช้อนด้วยได้กินข้าวแล้ว")
        else:
            print("ต้องหา ช้อนก่อน")
    else:
        print("ต้องหา ข้าวก่อน")
def forloop():
    Box = 0
    Looptime = int(input("จำนวนรอบที่ต้องการวนลูป: "))
    for i in range(1,Looptime+1):
        Box += i
        print (f"Box รอบที่ {i} = {Box}")
    print("=========================================")
    print(f"Box ผลรวมทั้งหมด = {Box}")
def whileloop():
    Box = 0
    Looptime = int(input("จำนวนรอบที่ต้องการวนลูป: "))
    i = 1
    while i <= Looptime:
        Box += i
        print(f"Box รอบที่ {i} = {Box}")
        i += 1
        if  i > 10:
            break
    print("=========================================")
    print(f"Box ผลรวมทั้งหมด = {Box}")