def clamp(number):
    if number < 0:
        while number < 0:
            number += 100
    else:
        while number > 99:
            number -= 100 
        
    return number



input = open("01_input.txt")
lines = input.readlines()
input.close()
value = 50
result = 0
for line in lines:
    temp =line.rstrip("\n")
    amount = int(temp[1:])
    if temp.startswith("L"):
        amount *= -1
    value = clamp(value+amount)
    if value == 0:
        result += 1


print(result)









