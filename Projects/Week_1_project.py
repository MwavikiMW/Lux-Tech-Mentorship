
def fibonnaci(n):
    Array1= [0,1,1]
    num = 0


    while num <= n:
        num = Array1[len(Array1)-2] + Array1[len(Array1)-1]
        Array1.append(num)
    
    return n in Array1

n= int(input("Enter any number: "))
print(fibonnaci(n))
