def test_number5(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True
    else:
        return False
a=int(input("1st number"))
b=int(input("2nd number"))
print(test_number5(a,b))
