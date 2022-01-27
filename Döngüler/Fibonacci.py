a=0
b=1
for i in range (0,20):
    a,b = b,a+b
    print("a:",a,"b:",b)
    print(b)