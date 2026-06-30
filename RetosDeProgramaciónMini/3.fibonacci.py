


# num1 = 0
# num2 = 1
# cont = 1
# while cont <= 50:
#     if num1 == 0:
#         print(num1)
#     suma = num1 + num2
#     print(suma)
#     num2 = num1
#     num1 = suma
#     cont += 1


num1 = 0
num2 = 1
for cont in range(51):
    if cont == 0:
        print(cont)
    suma = num1 + num2
    print(suma)
    # num1 = num2
    num2 = num1
    num1 = suma