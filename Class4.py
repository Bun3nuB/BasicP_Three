
# # # def add(a,b):
# # #     return a+b
# # # def introduction(Name):
# # #     print(f"My Name is :{Name}")
# # #     tellage()
# # # def tellage():
# # #     TellAge = int(input("Enter your age :"))
# # #     print(f"Your age is : {TellAge}")
# # # def spam(Text):
# # #     print("=====================")
# # #     print(type(Text))
# # #     Round = int(input("วนกี่รอบ :"))
# # #     for i in range(1,Round +1):
# # #         print(f"รอบที่ {i} \n {Text}")
# # # def H1():
# # #     spam("Ugaga")
# # #     spam(7.00)
# # #     spam(6)
# # #     spam(True)
# # # sum = add(1,2)
# # # print(sum)

# # x = ["three","show",2,3,7.0]
# # x[3] = 178 
# # name = []
# # v= 0
# # print(x)
# # round = int(input("How many name you want to Enter :"))
# # for i in range(round):
# #     Valu = input("What you want to enter :")
# #     name.append(Valu)
# # print(name)
# # for i in name:
# #     v += 1
# #     print(f"{v}.{i}")
# # i = int(input(f"you need to Delete some name what name you want to Delete:"))
# # name.pop(i-1)
# # print(name)

# students = [
#     {"name":"Three","id":68130500055},
#     {"name":"Ga","id":68130500054},
#     {"name":"hu","id":68130500053}
# ]
# def findstudent():
#     find = False
#     studentid = int(input("Enter STUDENT ID :"))
#     for student in students:    
#         if student["id"] == studentid:
#             return "Student name is "+ student["name"]
#     if not find:
#         return "this id is not in the list"
# print(findstudent())
