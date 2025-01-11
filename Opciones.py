print("Seleccionar una opcion")
print("1. Saludar")
print("2. Suma")
print("3. Multiplicacion")
print("4. Division")
print("5. Resta")
print("6. Factorial")
print("7. Temeratura")
print("8. Tablas")
print("9. Par o impar")
print("10. Numero primo")
print("11. Piedra, papel o tijera")
print("12. Generador de contrasenias")
print("13. Generador de piramides de caracteres")
print("14. Fibonacci")
print("15. Adivinador numerico")


print("100. Salir")


opcion=input("Elije una opcion:  ")
if opcion == "1":
    print("Hola")
#Suma####################################################################################################################################################
elif opcion =="2":
    print("Elejiste la opcion suma")
    num1=float(input("Ingresa el primer numero:  "))
    num2=float(input("Ingresa el segundo numero:  "))
    print("La suma es:  ", num1+num2)
#Multiplicacion###########################################################################################################################################
elif opcion =="3":
    print("Elejiste la opcion multiplicacion")
    num1=float(input("Ingresa el primer numero:  "))
    num2=float(input("Ingresa el segundo numero:  "))
    print("La multiplicacion es:  ", num1*num2)
#Division##############################################################################################################################################
elif opcion =="4":
    print("Elejiste la opcion division")
    num1=float(input("Ingresa el primer numero:  "))
    num2=float(input("Ingresa el segundo numero:  "))
    print("La division es:  ", num1/num2)
#Resta#################################################################################################################################################
elif opcion =="5":
    print("Elejiste la opcion resta")
    num1=float(input("Ingresa el primer numero:  "))
    num2=float(input("Ingresa el segundo numero:  "))
    print("La resta es:  ", num1-num2)
#Factorial#############################################################################################################################################
elif opcion =="6":
    print("Elejiste la opcion factorial")
    num1=int(input("Ingresa un numero:  "))
    factorial = 1
    for i in range(1, num1 + 1):
        factorial *=i
    print("El factorial de:  ", num1, "es", factorial)
#Temperatura############################################################################################################################################
elif opcion =="7":
    print("Seleccionaste temperatura, ahora selecciona Celsius o Fahrenheit")
    print("1. Celsius a Fahrenheit")
    print("2. Farenheit a Celsius")
    opcion1=input("Elije una opcion:  ")
    if opcion1 == "1":
        print("Usted selecciono 1.")
        cel = float(input("Ingresa la temperatura en celsius  "))
        Far=(cel*9/5)+32
        print(cel, "C son equivalentes a", Far,"F")
    elif opcion1 =="2":
        print("Usted selecciono 2.")
        Far = float(input("Ingresa la temperatura en Fahrenheit  "))
        cel=((Far-32)/(1.8))
        print(Far, "F son equivalentes a", cel,"C")        
    else:
        print("Opcion no valida")
#Tablas#####################################################################################################################################################
elif  opcion == "8":
    numeroT=int(input("De que numero quieres la tabla de multiplicar?  "))
    print(f"Tabla de multiplicar del {numeroT}:")
    div1=int(input("Hasta que numero quieres la tabla?  "))
    for i in range (1,div1+1):
        print (f"{numeroT} x {i} = {numeroT*i}")
#Par o Impar###################################################################################################################################################
elif  opcion == "9":
    par = int(input("Ingresa un numero: "))
    if par%2==0:
        print("El numero ",par," es par")
    else:
        print("El numero ",par," es impar" )
#Primo#############################################################################################################################################################
elif opcion=="10":
    def es_pri(pri):
        if pri <= 1:
            return False
        for i in range(2,int(pri**0.5)+1):
            if pri %i==0:
                return False
        return True
    pri=int(input("Ingresa un numero: "))    
    if es_pri(pri):
        print(f"{pri } es un numero primo")
    else:
        print(f"{pri } no es un numero primo")
#Piedra, papel o tijera############################################################################################################################
elif opcion=="11":

    import random
    def juego(op_jugador):
        opciones=["piedra, papel o tijera"]
        op_pc=random.choice(opciones)
        print(f"La computadora eligio: {op_pc}")
        if op_jugador == op_pc:
            return"Es un empate"
        elif(op_jugador=="piedra" and op_pc=="tijera") or (op_jugador == "papel" and op_pc=="piedra") or (op_jugador=="tijera" and op_pc=="papel"):
            return "Gananste"
        else:
              return"Perdiste"
    
    print("Juego: Piedra, papel o tijera") 
    op_jugador = input("Elige: " ).lower()
    if op_jugador in ["piedra", "papel", "tijera"]:
     print(juego(op_jugador))
    else:
      print("Opcion no valida")

#Generador de contrasenias#######################################################################################################################      
elif opcion=="12":

    import random
    import string
    
    def gen_con(longitud):
        cac=string.ascii_letters+string.digits
        return ''.join(random.choice(cac) for _ in range(longitud))
    longitud = int(input("De cuantos caracteres quieres tu contrasenia?:  "))
    print("Tu contrasenia generada es:  ",gen_con(longitud))


#Generador de piramides de caracteres #####################################################################################################################
elif opcion=="13":
    cual=(input("Con cual caracter quieres formar los triangulos?  "))
    filas=int(input("Cuantas filas quieres en el triangulo?  "))
    for i in range (1,filas+1):
        print(" "*(filas-i)+cual*(2*i-1))




#Fibonacci#####################################################################################################################################################
elif opcion=="14":
    def fibo_hasta(limite):
        fib=[0,1]
        while fib[-1]+fib[-2]<limite:
            fib.append(fib[-1]+fib[-2])
        return fib
    limitefib = int(input("Ingresa el limite maximo para la secuencia de Fibonacci:  "))
    print(f"Secuencia de Fibonacci hasta {limitefib}:  {fibo_hasta(limitefib)}")




#Adivinador Numerico#############################################################################################################################################################################################

elif opcion=="15":

    import random

    def guess_with_hints():
        print("Chinga tu cola")

    
        while True:
            number = random.randint(1,100)
            print("Adivina el numero entre 1 a 100  ")
            while True:
                try:
                    guess = int(input("Tu numero:  "))

                    if guess < number:
                        print("Mas alto")
                    elif guess > number:
                        print("Mas bajo")
                    else:
                        print("Acertaste")
                    break
                except ValueError:
                    print("Por favor ingresa un numero valido")
            play_again=input("Quieres jugar de nuevo baboso? (s/n):  ").lower()
            if play_again != 's':
                print("Gracias por jugar")
                break
    guess_with_hints()







#Adios##########################################################################################################################################################3
elif opcion=="100":
    print("Adios")
else:
    print("Opcion no valida")