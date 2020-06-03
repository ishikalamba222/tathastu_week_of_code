a=input("enter any string")
reverse=a[::-1]
print("the reversed string is",reverse)
duplicatestring=""
for i in a:
    if i not in duplicatestring:

        duplicatestring+=i

print(duplicatestring)
