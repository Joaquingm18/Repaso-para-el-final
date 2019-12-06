import os, random
os.system("cls")

n=-1

while n<=0:
    n=int(input("Ingrese un numero mayor a cero. "))
    if n<=0:
        print("Error , ingrese un numero que cumpla lo pedido. ")
print("")        
print("Su número es: "+ str(n))

k= random.randint(2,9)
print("Valor aletorio generado es: "+ str(k))
