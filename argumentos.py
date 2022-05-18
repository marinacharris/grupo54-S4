def suma (a,b):
    return a+b 

print(suma(6,5))

def suma2 (*args):
    total = 0
    for i in args:
        #total = total + i
        total +=i
    return total   

print(suma2(4,3,29,0)) 
print(suma2(7,8,5,4,7,8,5,4,5,8,5,4,5))
    
def suma3(**kwargs):
    total = 0
    for i in kwargs:
        total = total + kwargs[i]
        # total += kwargs[i]
    return total

print(suma3(a=1,b=2,c=50))
print(suma3(a=1,b=2,c=10, d=50))
