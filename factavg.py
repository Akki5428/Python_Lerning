def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac    

def avg(a,b,c,d,e):
    avg = (a+b+c+d+e) / 5 
    print("avg =",avg)

    

a = int(input("Enter 1st number: "))
b = int(input("Enter 2st number: "))
c = int(input("Enter 3st number: "))
d = int(input("Enter 4st number: "))
e = int(input("Enter 5st number: "))

avg(fact(a),fact(b),fact(c),fact(d),fact(e))