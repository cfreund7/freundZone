# add summary

num = input("Enter an Integer: ")
num = int(num)

collatzList = [num]

while num > 1:
    if num % 2 == 0:
        num /= 2
        collatzList.append(int(num))
    else:
        num = 3*num + 1
        collatzList.append(int(num))

print(collatzList)