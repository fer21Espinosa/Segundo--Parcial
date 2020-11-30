import csv
import numpy

 #piv es pivote
 # r es renglon
 # c es columna

def impresion1():
        print(""" \n\t\t
\t\t\t██▄██ █▀▀ █▄░█ █░░█
\t\t\t█░▀░█ █▀▀ █▀██ █░░█
\t\t\t▀░░░▀ ▀▀▀ ▀░░▀ ░▀▀░\n""")


def leer_opcion():
    while True: 
         try:
                 impresion1()
                 print("""\n\n\t\t1.Ingrese un sistema de ecuaciones\n\t\t2.Ver un ejemplo\n\t\t3.Salir""")
                 opcion=int(input("\nSu opcion= ")) 
                 return opcion
         except ValueError:
                  print ("La opcion es incorrecta: escribe un numero entero") 
                  print("""
\t\t\t▄██████████████▄▐█▄▄▄▄█▌
\t\t\t██████▌▄▌▄▐▐▌███▌▀▀██▀▀
\t\t\t████▄█▌▄▌▄▐▐▌▀███▄▄█▌
\t\t\t▄▄▄▄▄██████████████▀   \n""")

def DatosMatriz():
        aux =numpy.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
       
        for i in range (0,3):
                 print("Ingrese los coeficientes de la ecuacion ", (i+1))
                 for j in range (0,4) :
                         if j == 0 :
                                 while True: 
                                         try:
                                                 aux[i][j]=int(input("Ingrese el valor de x= ")) 
                                                 break
                                         except ValueError:
                                                 print ("La entrada es incorrecta: escribe un numero entero")         
                         else:
                                 if j==1 :	
                                         while True:
                                                 try: 
                                                         aux[i][j] =int(input("Ingrese el valor de y= "))
                                                         break
                                                 except ValueError:
                                                         print ("La entrada es incorrecta: escribe un numero entero") 
                                             							
                                 else:
                                         if j==2 :	
                                                 while True :
                                                         try:
                                                                 aux[i][j]=int(input("Ingrese el valor de z= "))
                                                                 break
                                                         except ValueError:
                                                                 print ("La entrada es incorrecta: escribe un numero entero") 
                                                
                                         else:
                                                  while True:
                                                         try:
                                                                 aux[i][j]=int(input("Ingrese el resultado= "))
                                                                 break
                                                         except ValueError:
                                                                 print ("La entrada es incorrecta: escribe un numero entero") 
                                                 
        return aux


def IngresarMatriz(data):
      with open('Datos_Ejemplo.csv', 'w') as csvfile:
          writer = csv.writer(csvfile, delimiter=',')
          writer.writerows(data)

def leerMatriz():
    reader=csv.reader(open('C:/Users/fer_e/Desktop/Segundo Parcial/MontantePy-master/Datos_Ejemplo.csv', "r"),delimiter=',')
    listR=list(reader)
    matriz=numpy.array(listR).astype('int')
    return matriz

resultado= lambda diagonal,resultado:resultado/diagonal  
elemento= lambda a,b,c,d,e: (a*b-c*d)/e
#matriz[r][c]=(matriz[pivN][pivN] * matriz[r][c] -matriz[r][pivN]*matriz[pivN][c])/pivAnt

def metodomontante(matriz):

 print ("""\n╔══╦═╦══╦╦╦╦══╗╔╦═╦╦╦═╦╦═╦╗═
║║║║╩╠╗╔╣╔╣╠╝╔╣║║║║║║╠╣║╩║╚╗
╚╩╩╩╩╝╚╝╚╝╚╩══╝╚╩╩═╩╩═╩╩╩╩═╝
\n\n""" + str(matriz))
 print(""" \n\n$$$$$$´´ ´´´´´´ ´´´´´´´ ´´´´´´´ ´´´´´´´ ´´´´´´ ´´´´´´´
$$´´´$$´ ´´´´´´ ´´´´´´´ ´´´´´´´ ´$$$$´´ ´$$$$´ ´´´´´´´
$$´´´$$´ $$´$$´ ´$$$$´´ ´$$$$$´ $$´´$$´ $$´´´´ ´$$$$´´
$$$$$$´´ $$$´$´ $$´´$$´ $$´´´´´ $$$$$$´ ´$$$´´ $$´´$$´
$$´´´´´´ $$´´´´ $$´´$$´ $$´´´´´ $$´´´´´ ´´´$$´ $$´´$$´
$$´´´´´´ $$´´´´ ´$$$$´´ ´$$$$$´ ´$$$$$´ $$$$´´ ´$$$$´´
 """)
 pivAnt = 1
 if matriz[0][0]==0 and matriz[0][0]==0 and matriz[0][0]==0:
     print("La diagonal principal esta llena de 0, por el momento no se puede resolver")
 else :
         for pivN in range(0,3):
             for r in range(0,3):
                     for c in range(0,4):
                             if c != pivN and r!= pivN:
                                     matriz[r][c]= elemento(matriz[pivN][pivN],matriz[r][c],matriz[r][pivN],matriz[pivN][c],pivAnt)
                     if r != pivN:
                              matriz[r][pivN]= 0
             print ("\n" + str(matriz))
             pivAnt=matriz[pivN][pivN]


         print ("""\n╔══╦═╦══╦╦╦╦══╗╔═╦╦═╦╦═╦╗═
║║║║╩╠╗╔╣╔╣╠╝╔╣║╔╣║║║║╩║╚╗
╚╩╩╩╩╝╚╝╚╝╚╩══╝╚╝╚╩╩═╩╩╩═╝\n\n"""+ str(matriz)	)

         x=resultado(matriz[0][0],matriz[0][3])
         y=resultado(matriz[1][1],matriz[1][3])
         z=resultado(matriz[2][2],matriz[2][3])

         print ("\nEl determinate es: ", pivAnt)
         print ("\nValores de x,y,z:\n" )
         print ("X = ", x)
         print ("Y = ", y)
         print ("Z = ", z)
 

def main(): 
     opcion=leer_opcion()
     while (opcion < 1 or opcion > 3):
             print("\n\nERROR: Su opcion fue incorrecta, Ingrese una opcion valida")
             opcion=leer_opcion()
     if opcion!=3 :
             if opcion == 1:
                     #IngresarMatriz(DatosMatriz())
                     metodomontante(DatosMatriz())

             else :
                     metodomontante(leerMatriz())  
             
             print("\n\nEste fue el Metodo Montante")
             print("\n\n¿Que desea hacer?")      
             main()     


print("""
      Segundo Examen Parcial            Fernando Esparza Espinosa
      
 Programa que resuelve un sistema de ecuaciones de 3x3 por el Metodo Montante
 
\t\t╔╦══╦══╦╦═══╦╦══╦══╦════╦╦═════╦╦═══╗
\t\t║║║║╠═╦╣╠╦═╦╝╠═╗║║║╠═╦═╦╣╠╦═╦═╦╣╠╦═╗║
\t\t║║║║║╩╬╗╔╣║║║║║║║║║║║║║╠╗╔╬╝║║╠╗╔╣╩╣║
\t\t║╚╩╩╩═╝╚═╩═╩═╩═╝╚╩╩╩═╩╩╝╚═╩═╩╩╝╚═╩═╝║
\t\t╚═══════════════════════════════════╝""")
main()                    
print("Eso fue todo")


