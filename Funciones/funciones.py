#Estudiante: Gerald Estifen Calderón Castro
#TareaCorta01 Ejercicios de practica 1
#PARES
#
#Ejercicio 2, Esta funcion convierte numeros a letras
def numLetras(numero):
    if (type(numero)==int and 0<=numero<=9):
        if numero==0:
            return 'cero'
        elif numero==1:
            return 'uno'
        elif numero==2:
            return 'dos'
        elif numero==3:
            return 'tres'
        elif numero==4:
            return 'cuatro'
        elif numero==5:
            return 'cinco'
        elif numero==6:
            return 'seis'
        elif numero==7:
            return 'siete'
        elif numero==8:
            return 'ocho'
        else:
            return 'nueve'
    else:
       return 'Argumento inválido digite un número entero entre 0 y 9'
#Ejercicio 4, foo misterio
def foo(op):
    return op/7
#Ejercicio 6, Esta funcion retorna el desglose del dinero en denominaciones de 1,5,10,20,50 y 100
def desglose(dinero):
    if (type(dinero)==int or type(dinero)==float)and dinero>=0:
        cambio=[0,0,0,0,0,0]
        while dinero>0:
            if 100<=dinero:
                cambio[0]+=1
                dinero-=100
            elif 50<=dinero:
                cambio[1]+=1
                dinero-=50
            elif 20<=dinero:
                cambio[2]+=1
                dinero-=20
            elif 10<=dinero:
                cambio[3]+=1
                dinero-=10
            elif 5<=dinero:
                cambio[4]+=1
                dinero-=5
            else:
                cambio[5]+=1
                dinero-=1
        resultado=tuple(cambio)
        return resultado
    return 'Argumento inválido, debe ser un número entero o real, mayor o igual que 0'
#Ejercicio 8, Esta funcion ordena 3 números de mayor a menor
def orden(a,b,c):
    if (type(a)==int or type(a)==float)and(type(b)==int or type(b)==float)and(type(c)==int or type(c)==float):
        resultado=[a,b,c]
        resultado.sort(reverse=True)
        resultado=tuple(resultado)
        return resultado
    else:
        return 'Argumentos inválidos, deben ser números reales'
#Ejercicio 10, Evaluar invocaciones
def misterio(a, c):
    b=lambda x: a**2
    d=b(c)+10
    return d
#Ejercicio 12, Esta funcion calcula salario del trabajador dadas las horas trabajadas y la tarifa por hora
def calcSalario(horas,tarifa):
    if (type(horas)==int  or type(horas)==float)and horas>=0 and (type(tarifa)==int or type(tarifa)==float) and tarifa>=0:
        if horas>40:
            horas_extra=(horas-40)
            tarifaExtra=horas_extra*tarifa*0.50
            horas_normales=horas-horas_extra
            salario=horas_normales*tarifa+tarifaExtra
        else:
            salario=horas*tarifa
        return salario
    else:
        return 'Argumentos inválido, deben ser números reales matemáticos y mayores o iguales que 0'
#Ejercicio 14, Esta funcion determina cuantos minutos restan para culminar el día
def faltante(horas,minutos,segundos):
    if (type(horas)==int and 0<=horas<=23) and (type(minutos)==int and 0<=minutos<=59) and (type(segundos)==int and 0<=segundos<=59):
        minutos_totales=horas*60+minutos+segundos/60
        minutos_faltantes=1440-minutos_totales
        return minutos_faltantes
    else:
        return 'Argumentos inválidos, digite las horas con valores de 0 a 23, los minutos y segundos con valores de 0 a 59'
#Ejercicio 16, Esta funcion indica el dígito más significativo de un número de tres dígitos
def significativo(num):
    if type(num)==int and abs(num)//100!=0 and abs(num)//1000==0:
        num=abs(num)
        return num//100
    return 'Error en numero de entrada'
#Ejercicio 18, Esta funcion calcula la cantidad futura de dinero aplicando el impuesto compuesto despues de n años
def interesCompuesto(P, i, n):
    if (type(P)==int or type(P)==float and P>=0) and (type(i)==int or type(i)==float) and (type(n)==int or type(n)==float and n>=0):
        F=P*(1+i)**n
        return F
    else:
        return 'Error en entradas, i debe ser un número real y P, n deben ser números reales mayor o iguales que 0'
#Ejercicio 20, Esta funcion retorna un número con las cifras invertidas
def invertir(numero):
    if type(numero)==int:
        if numero<0:
            negativo=True
        else:
            negativo=False
        numero=abs(numero)
        resultado=0
        while numero!=0:
            resultado=resultado*10+numero%10
            numero=numero//10
        if negativo==True:
            resultado=-(resultado)
        return resultado
    else:
        return 'Argumento inválido, digite un número entero'
#Explicacion: Esta funcion se encarga de convertir los grados Celsius a Fahrenheit
def convertir(Celsius):
    if (type(Celsius)==int or type(Celsius)==float):
        Fahrenheit=9/5*Celsius+32
        return Fahrenheit

    else:
        return 'Argumento inválido, debe ser un número real matemático'
#Ejercicio 2: 
#Explicacion: Esta funcion compone un numero a partir de 3 digitos
def formaNum(dig1,dig2,dig3):
    if (type(dig1)==int and 0<=dig1<10)and(type(dig2)==int and 0<=dig2<10)and(type(dig3)==int and 0<=dig3<10):
        digitos=[dig1,dig2,dig3]
        digitos.sort()
        numero=digitos[2]*100+digitos[1]*10+digitos[0]
        return numero
    else:
        return 'Argumentos inválidos, debe ser cada uno un digito'
#Ejercicio 3:
#Explicacion: Esta funcion convierte numeros a letras
def convertir_a_letras(numero):
    if (type(numero)==int and 1<=numero<=5):
        if numero==1:
            return 'uno'
        elif numero==2:
            return 'dos'
        elif numero==3:
            return 'tres'
        elif numero==4:
            return 'cuatro'
        else:
            numero==5
            return 'cinco'
    else:
       return 'Argumento inválido digite un número entero de 1 a 5'
#Ejercicio 4:
#Explicacion: Esta funcion calcula las raices de una ecuación cuadratica
def ecuacion_cuadra(a,b,c):
    if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float) and (type(c)==int or type(c)==float):
        if a==0:
            return 'Argumento inválido, se hace cero el denominador'
        else:
            x1=(-b+((b**2)-4*a*c)**(1/2))/(2*a)
            x2=(-b-((b**2)-4*a*c)**(1/2))/(2*a)
            if x1==x2:
                return x1
            return x1, x2
    else:
        return 'Argumentos inválidos digite números reales matemáticos'
#Ejercicio 5:
#Explicacion: Esta funcion determina el estado de notas del estudiante
def estado_estudiante(nota):
    if ((type(nota)==int or type(nota)==float) and 0<=nota<=100):
        if nota>=70:
            return 'Aprobado'
        elif 60<=nota<=69:
            return 'Aplazado'
        else:
            return 'Reprobado'
    else:
        return 'Argumento inválido, debe ser un número real matemático de 0 a 100'
#Ejercicio 6:
#Explicacion: Esta funcion calcula la pendiente de una ecuacion lineal
def pendiente(x1,y1,x2,y2):
    if (type(x1)==int or type(x1)==float) and (type(y1)==int or type(y1)==float) and (type(x2)==int or type(x2)==float) and (type(y2)==int or type(y2)==float):
        if x2-x1==0:
            return 'El denominar se hace 0 y indefine la ecuación'
        else:
            resultado=(y2-y1)/(x2-x1)
            return resultado
    else:
        return 'Argumentos inválidos, digite números reales matemáticos'
#EJERCICIOS ESTRUCTURAS DE REPETICION
#Explicacion: Esta funcion imprime los numeros desde 1 hasta N
def imprimir_1_a_N(N):
    if type(N)==int and N>=1:
        resultado=0
        while resultado!=N:
            resultado=resultado+1
            print(resultado)
    else:
        return 'Argumento inválido, debe ser un número entero positivo'
#Explicacion: Esta funcion suma los numeros desde 1 hasta N
def suma_1_a_N(N):
    if type(N)==int and N>=1:
        resultado=0
        contador=0
        while contador!=N:
            contador+=1
            resultado=contador+resultado
        return resultado
    else:
        return 'Argumento inválido, debe ser un número entero positivo'
#Explicacion: Esta funcion suma los numeros desde N hasta M
def suma_N_a_M(N,M):
    if (type(N)==int and N<=M)and(type(M)==int):
        resultado=N
        while N!=M:
            N+=1
            resultado=N+resultado
        return resultado
    else:
        return 'Argumentos inválidos, deben ser números enteros y N debe ser menor o igual que M'
#Explicacion: Esta funcion cuenta los digitos de un numero entero
def cuenta_Digitos(numero):
    if type(numero)==int:
        resultado=0
        numero=abs(numero)
        if numero==0:
            return 1
        else:
            while numero!=0:
                numero=numero//10
                resultado+=1
            return resultado
    return 'Argumento inválido, debe ser un número entero'
#Explicacion: Esta funcion cuenta los digitos pares de un numero entero
def cuenta_Digitos_Pares(numero):
    if type(numero)==int:
        resultado=0
        numero=abs(numero)
        if numero==0:
            return 1
        else:
            while numero!=0:
                if (numero%10)%2==0:
                    resultado+=1
                numero=numero//10
            return resultado
    return 'Argumento inválido, debe ser un número entero' 
#PRACTICA_DE_CLASE_02
#Estudiante: Gerald Estifen Calderon Castro
#
#Explicación es igual a estrategia de solución
def tieneCeros(num):
    if type(num)==int:
        num=abs(num)
        cantidad=True
        if num!=0:
            cantidad=False
        while num!=0:
            if num%10==0:
                cantidad=True
            num=num//10
        return cantidad
    else:
        return 'Error en las entradas, debe ser un número entero'
#Ejercicio: #2
#Explicacion: Para Determinar cuantos ceros tiene el numero entero de entrada
def cuentaCeros(num):
    if type(num)==int:
        num=abs(num)
        cantidad=1
        if num!=0:
            cantidad=0
        while num!=0:
            if num%10==0:
                cantidad+=1
            num=num//10
        return cantidad
    else:
        return 'Error en las entradas, debe ser un número entero'
#Ejercicio: #3
#Explicacion: Para Determinar si un numero entero de entrada posee al menos una vez un digito de entrada
def tieneDigito(dig,num):
    if type(num)==int and type(dig)==int and 0<=dig<10:
        num=abs(num)
        if dig==0 and num==0:
            return True
        cantidad=False
        while num!=0:
            if num%10==dig:
                cantidad=True
            num=num//10
        return cantidad
    else:
        return 'Error en las entradas, debe ser un dígito y un número entero'
    
#Ejercicio: #4
#Explicacion: Para Determinar cuantas veces aparece un digito de entrada en un numero entero de entrada
def cuentaDigito(dig,num):
    if type(num)==int and type(dig)==int and 0<=dig<10:
        num=abs(num)
        cantidad=0
        if dig==0 and num==0:
            cantidad=1
        while num!=0:
            if num%10==dig:
                cantidad+=1
            num=num//10
        return cantidad
    else:
        return 'Error en las entradas'
#Ejercicio: 5
#Explicacion: Esta función retorna el resultado de la sumatoria desde cero hasta un número entero positivo n
def sumatoria(n):
    if type(n)==int and 0<n:
        resultado=0
        contador=0
        while contador<=n:
            resultado+=contador
            contador+=1
        return resultado
    else:
        return 'Error en las entradas, digite un número entero positivo'
#Ejercicio: #6
#Explicacion: Esta función retorna el resultado de la productoria desde cero hasta un número entero positivo n, para ello se crean dos variables, i servirá para
def productoria(n):
    if type(n)==int and 0<n:
        i=1
        resultado=1
        while i<=n:
            resultado*=i
            i+=1
        return resultado
    else:
        'Error en las entradas, digite un número entero positivo'
#Ejercicio: #7
#Explicacion: Esta función devuelve el resultado de elevar x a la n-ésima potencia (xn) utilizando el algoritmo de multiplicaciones sucecivas
def potencia(x,n):
    if (type(x)==int or type(x)==float)and(type(n)==int or type(n)==float):
        if n==0:
            return 1
        else:
            contador=0
            resultado=x
            while contador<n-1:
                resultado*=x
                contador+=1
            return resultado
    else:
        'Error en las entradas, debe ser un número real'
#Ejercicio: #8
#Explicacion: Esta función estaba basada en el algoritmo de Euclides
def mcd(M,N):
    if (type(M)==int and type(N)==int and N<M and 0<N):
        R=M%N
        while R!=0:
            M=N
            N=R
            R=M%N
        return N
    else:
        return'Error en las entradas, deben ser números enteros positivos y M debe ser mayor que N'
#Ejercicio: #9
#Explicacion: Esta funcion suma desde un valor inicial denominado A hasta un valor final denominado B
def sumaAB(A,B):
    if type(A)==int and(type(B)==int)and A<=B:
        resultado=A
        while A!=B:
            A+=1
            resultado=A+resultado
        return resultado
    else:
        return 'Argumentos inválidos, deben ser números enteros y A debe ser menor o igual que B'
#Ejercicio: #10
#Explicacion: Esta funcion recibe A, B y una función cualquiera de un parametro
def sumaFuncAB(A,B,func):
    if type(A)==int and(type(B)==int)and A<=B:
        resultado=0
        for i in range (A,B+1):
            resultado=resultado+func(i)
        return resultado
    else:
        return 'Argumentos inválidos, deben ser números enteros y A debe ser menor o igual que B'
#Ejercicio: #11
#Explicacion: Esta función recibe un número entero y devuelve como resultado la suma de sus dígitos
def sumaDigitos(num):
    if type(num)==int:
        num=abs(num)
        guardar=0
        while num!=0:
            guardar=guardar+num%10
            num=num//10
        return guardar
    else:
        return 'Error en las entradas, digite un número entero'
#Ejercicio: #12
#Explicacion: Esta función recibe un número entero y devuelve como resultado la multiplicación de sus dígitos
def multiDigitos(num):
    if type(num)==int:
        num=abs(num)
        resultado=1
        if num==0:
            return 0
        else:
            while num!=0:
                resultado*=num%10
                num=num//10
            return resultado
    else:
        return 'Error en las entradas, digite un número entero'
#Ejercicio: #13
def esPrimo(num):
    if type(num)==int and 0<num:
        num=abs(num)
        div=2
        while div<num:
            if num%div==0:
                return False
            div+=1
        return True
    else:
        return 'Error en las entradas, digite un número entero'
#Ejercicio: #14
def esPrimoPlus(num):
    if type(num)==int and 0<num:
        from math import sqrt
        num=abs(num)
        if num==1:
            return True
        elif num==2:
            return True
        if num%2==0:
            return False
        div=3
        while div<=sqrt(num):
            if num%div==0:
                return False
            div+=2
        return True
    else:
        return 'Error en las entradas, debe ser un número entero'
#Estudiante: Gerald Calderón Castro
#Grupo: 41
#TareaCorta01
#
#Ejercicio 1, calculo del área y circunferencia de un circulo
def circulo(radio):
    if (type(radio)==int or type(radio)==float) and radio>0:
        import math
        Area=math.pi*radio**2
        Circunferencia=2*math.pi*radio
        return {'Area': Area, 'Circunferencia': Circunferencia}
    else:
        return 'Argumento inválido, digite un número entero o real positivo'
#Ejercicio 3, calcular el área y volumen de una esfera
def esfera(radio):
    if (type(radio)==int or type(radio)==float) and radio>0:
        import math
        volumen=4/3*math.pi*radio**3
        area=4*math.pi*radio**2
        return {'area' : area,'volumen' : volumen}
    else:
        return 'Argumento inválido, digite un número entero o real positivo'
#Ejercicio 5, determinar si un año es bisiesto o no
def bisiesto(año):
    if (type(año)==int)and año>0:
        if (año%4==0 or año%400==0)and año%100!=0:
            return True
        else:
            return False
    else:
        return 'Argumento inválido, digite un número entero positivo'
#Ejercicio 7, calcular el mediano de tres argumentos numéricos
def mediano(a,b,c):
    if (type(a)==int or type(a)==float)and(type(b)==int or type(b)==float)and(type(c)==int or type(c)==float):
        mediano=a+b+c-max(a,b,c)-min(a,b,c)
        return mediano
    else:
        return 'Argumentos inválidos, deben ser números reales'
#Ejercicio 9, expresa una cantidad de gigabytes en bytes
def disco(capacidad):
    if (type(capacidad)==int or type(capacidad)==float)and capacidad>=0:
        capacidad=capacidad*(1024**3)
        return capacidad
    else:
        return 'Argumento inválido, debe ser un numero entero o real, mayor que o igual que 0'
#Ejercicio 11, conversión de metros ya sea a; centímetros, pulgadas, pies o yardas.
def convertir(distancia,tipo):
    if (type(distancia)==float or type(distancia)==int) and distancia>=0 and (type(tipo)==int and 0<tipo<5):
        if tipo==1:
            distancia*=100
        elif tipo==2:
            distancia=distancia*100/2.54
        elif tipo==3:
            distancia=distancia*100/2.54/12
        else:
            distancia=distancia*100/2.54/12/3
        return distancia
    else:
        return 'Argumentos inválidos, digite una distancia que sea un número real y un tipo que sea entero de 1 a 4'
#Ejercicio 13, determinar el salario con aumento de un jugador y el valor correspondiente a dicho aumento
def aumento(salario):
    if type(salario)==int or type(salario) and salario>=0:
        valorAumento=lambda salario,porcentaje: salario*porcentaje
        salarioAumentado=lambda salario,porcentaje: salario+(salario*porcentaje)
        if salario<=1000000:
            porcentaje=20/100
        elif salario<=1500000:
            porcentaje=10/100
        elif salario<=2000000:
            porcentaje=5/100
        else:
            porcentaje=0
        return salarioAumentado(salario,porcentaje),valorAumento(salario,porcentaje)
    else:
        return 'Argumento inválido, debe ser un número real mayor o igual que 0'
#Ejercicio 15, determinar si un número es palíndromo o no
def palindromo(numero):
    if type(numero)==int:
        numero=abs(numero)
        guardar=numero
        resultado=0
        while numero!=0:
            resultado=resultado*10+numero%10
            numero=numero//10
        if resultado==guardar:
            return True
        else:
            return False
    else:
        return 'Argumentos inválidos, digite un número entero'
#Ejercicio 17, adjuntar un dígito a un número entero
def adjunto(num, dig):
    if type(num)==int and type(dig)==int and 0<=dig<=9:
        num=num*10+dig
        return num
    else:
        return 'Error en entradas, debe ser un número entero y un dígito'
#Ejercicio 19, calcular el área de superficie y volumen de un toro (especie de poliedro)
def toro(a,b):
    if (type(a)==int or type(a)==float and a>0)and(type(b)==int or type(b)==float and b>0):
        from math import pi 
        AreadelaSuperficie=(pi**2)*(b**2-a**2)
        Volumen=(pi**2*(a+b)*((b-a)**2))/4
        return {'area' : AreadelaSuperficie, 'volumen' : Volumen}
    else:
        return 'Error en entradas, a y b deben ser números reales positivos'
#Ejercicio 21, convertir un número entero a letras
def numLetras2(numero):
    if type(numero)==int:
        unidades=[0,1,2,3,4,5,6,7,8,9]
        nombre=['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
        resultado=""
        numero=abs(numero)
        while numero!=0:
            guardar=numero%10
            numero=numero//10
            for i in unidades:
                if guardar==i:
                    resultado=nombre[i]+"-"+resultado
        resultado=resultado[:-1]
        return resultado
    else:
        return 'Argumento inválido, digite un número entero'