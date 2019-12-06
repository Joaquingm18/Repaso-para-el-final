import os, random
os.system("cls")

def calculardistancia(x,y):
    distancia = ((x)**2 +(y)**2)**0.5
    return distancia
print("")
print("Punto 1:")
print("")
px1=float(input("X1= "))
py1=float(input("Y1= "))
print("")


print("Punto 2:")
print("")
px2=float(input("X2= "))
py2=float(input("Y2= "))

#los metodo etc

dist1= calculardistancia(px1,py1)
dist2= calculardistancia(px2,py2)
print("")
print("El punto más cerca al origen es: ")
if dist1<dist2:
    print("Punto 1. ")
else:
    print("Punto 2. ")    