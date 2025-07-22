KM = int(input("ระยะทางที่จะขนส่ง :"))
bath = 0
ส่งมั่ย = True
if(KM < 5):
    ส่งมั่ย = False
elif(KM < 50):
    bath = 10
elif(KM < 100):
    bath = 15
elif(KM < 300):
    bath = 25
elif(KM < 500):
    bath = 35
else:
    bath = 45

if(ส่งมั่ย):
    print("=================[ สรุป ]================")
    print(f"ระยะทางการขนส่งทั้งหมด {KM} กิโลเมตร")
    print(f"ค่าส่ง {bath} บาท")
    print("ᕙ(⇀‸↼‶)ᕗ")
else:
    print("ระยะทางต่ำกว่า 5 กิโลเมตร ไม่ส่ง")
    print("(┳Д┳)")