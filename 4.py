#5x^2-14x+17=0

try:
    a = int (input ("введите a:"))
except ValueError:
    print ("Вы ввели не число")
print(a)

try:
    b = int (input ("введите b:"))
except ValueError:
    print("Вы ввели не число")
print(b)

try:
    c = int (input ("введите c:"))
except ValueError:
    print("Вы ввели не число")
print(c)

D = b**2 - 4*a*c
if D > 0:
    x1 = (b + D**0.5)/2*a
    x2 = (b - D**0.5)/2*a
    print("D = ", D)
    print(x1, x2)
elif D == 0:
    print(1)
else:
    print(":)")

if __name__ == '__main__':
    pass
#ДЗ: сделать то же, но a, b и с должны вводитьс в терминале