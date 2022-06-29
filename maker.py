amount = int(input("How many numbers do you want the program to go to? ")) + 1

f = open("first.py", "w")

f.write("print('Welcome to this calculator!')" + "\n")
f.write("print('It can add, subtract, multiply and divide whole numbers from 0 to " + str(amount - 1) + "')" + "\n")
f.write("num1 = int(input('Please choose your first number: '))" + "\n")
f.write("sign = input('What do you want to do? +, -, /, or *: ')" + "\n")
f.write("num2 = int(input('Please choose your second number: '))" + "\n")

for i in range(4):
    for n in range(amount):
        for m in range(amount):
            if i == 0:
                f.write("if num1 == " + str(n) + " and sign == '+' and num2 == " + str(m) + ":" + "\n")
                f.write("     print(\"" + str(n) + "+" + str(m) + " = " + str(n+m) + "\")" + "\n")
            elif i == 1:
                f.write("if num1 == " + str(n) + " and sign == '-' and num2 == " + str(m) + ":" + "\n")
                f.write("     print(\"" + str(n) + "-" + str(m) + " = " + str(n-m) + "\")" + "\n")
            elif i == 2:
                f.write("if num1 == " + str(n) + " and sign == '*' and num2 == " + str(m) + ":" + "\n")
                f.write("     print(\"" + str(n) + "*" + str(m) + " = " + str(n*m) + "\")" + "\n")
            elif i == 3:
                try:
                    z = n/m
                    
                    f.write("if num1 == " + str(n) + " and sign == '/' and num2 == " + str(m) + ":" + "\n")
                    f.write("     print(\"" + str(n) + "/" + str(m) + " = " + str(z) + "\")" + "\n")
                except ZeroDivisionError:
                        continue
f.close()