import os
os.system("cls")

#Los metodos de cada una de las opciones
#Opcion 1:

def segundoMayor(x,y,z,w):
    
    if x>y:
        primerM=x
        SegundoM=y
    else:
        primerM=y
        SegundoM=x

    if z>primerM:
        SegundoM= primerM
        primerM =z
    elif z>SegundoM:
        SegundoM=z

    if w>primerM:
        SegundoM=primerM  
        primerM=w      
    elif w>SegundoM:
        SegundoM=w
    return SegundoM
#opcion 2
def promediar(nota1,nota2,nota3):
    sumatoria=nota1+nota2+nota3
    menor=nota1
    if nota2<menor:
         menor=nota2
    if  nota3< menor:
        menor =nota3
    promedio =(sumatoria-menor)/2         
    return promedio

#Interfaz o algo asi

print("            Menú           ")
print("<1> Calcular segundo número ")
print("<2> Calcular promedio       ")
print("<3> Salir ")
op =int(input("Ingrese una opcion: "))

while(True):
    if op == 1:
        while (True):
            x=int(input("ingrese el 1er numero: "))
            y=int(input("ingrese el 2do numero: "))
            z=int(input("ingrese el 3er numero: "))
            w=int(input("ingrese el 4to numero: "))

            if not (x==0 or y==0 or z==0 or w==0):
                break
            else:
                print("Error en los datos. ")    
        print("El segundo mayor numero es: ", segundoMayor(x,y,z,w))            


