
#5x^2-14x+17=0

D = 14**2 - 4*5*17
if D > 0:
    x1 = (-14 + D**0.5)/2*5
    x2 = (-14 - D**0.5)/2*5
    print(D)
    print(x1, x2)
elif D == 0:
    print(1)
else:
    print(":)")

#ДЗ: сделать то же, но a, b и с должны вводитьс в терминале