n= input('enter the no')
sm=0
ln=len(n)
for i in n:
    sm+=int(i)**ln
if sm==int(n):
    print(True)
else :
    print(False)    