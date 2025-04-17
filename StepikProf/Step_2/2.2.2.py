rus = "АаВСсЕеНКМОоРрТХху"
eng = "AaBCcEeHKMOoPpTXxy"

a, b, c = input(), input(), input()
en = ru = 0

if a in rus:
    ru += 1
elif a in eng:
    en += 1

if b in rus:
    ru += 1
elif b in eng:
    en += 1

if c in rus:
    ru += 1
elif c in eng:
    en += 1

if ru == 3:
    print("ru")
elif en == 3:
    print("en")
else:
    print("mix")
