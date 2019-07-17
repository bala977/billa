ip=0
Num = int(input(""))
S= 0
while(Num > 0):
    ip= Num % 10
    S = S+ip
    Num = Num //10
print(S)
