a=int(input("enter any number"))
count=0
while(a!=0):
    rem = a % 10
    count = count * 10 + rem
    a = a //10

print(count)
