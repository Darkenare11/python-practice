s=input("input a string")
d=i=0
for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        i+=1
    else:
        pass
print("letters",i)
print("digits",d)
