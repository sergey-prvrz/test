#5x^2-14x+17=0

a = input ("введите a:")
a1 = int (a)
print(a1)
b = input ("введите b:")
b1 = int (b)
print(a1)
c = input ("введите c:")
c1 = int (c)
print(a1)

D = b1**2 - 4*a1*c1
if D > 0:
    x1 = (b1 + D**0.5)/2*a1
    x2 = (b1 - D**0.5)/2*a1
    print(D)
    print(x1, x2)
elif D == 0:
    print(1)
else:
    print(":)")

if __name__ == '__main__':
    pass
#ДЗ: сделать то же, но a, b и с должны вводитьс в терминале