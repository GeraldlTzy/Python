def multi(num1,num2):
    if type(num1)==int or type(num1)==float:
        if type(num2)==int:
            contador=0
            resultado=num1
            while contador!=(abs(num2)-1):
                resultado+=num1
                contador+=1
            if num2 < 0:
                return -resultado
            else:
                return resultado
        else:
            return "Error: segundo argumento debe ser entero"
    else:
        return "Error: primer argumento debe ser un número real y segundo argumento debe ser un número entero"

#Ejercicio 2,
#Explicacion: Esta funcion retorna un número con las cifras invertidas
#Entradas: numero
#Restricciones: Es un número entero.
#Herramientas: funciones type() y abs(), igualdad, desigualdad, multiplicación, división entera, suma, módulo y cambio de signo
#Salidas: resultado, 'Argumento inválido, digite un número entero'
def invertir(num):
    if type(num)==int:
        if num<0:
            negativo=True
        else:
            negativo=False
        num=abs(num)
        resultado=0
        while num!=0:
            resultado=resultado*10+num%10
            num=num//10
        if negativo==True:
            resultado=-(resultado)
        return resultado
    else:
        return 'Argumento inválido, digite un número entero'
#Ejercicio 3,
#Explicacion: Esta función recibe un número entero y devuelve como resultado la suma de sus dígitos, para ello se trabaja con el valor absoluto, se establece una variable guardar para conservar
#los dígitos que posee número, se entra a un ciclo con la condición de que el número sea distinto de 0, a guardar se le sumando cada dígito del número y a el número se le aplica división entera
#para salir del ciclo.
#Entradas: num
#Restricciones: Es un numero entero
#Herramientas: función type y abs, suma, módulo, division entera, igualdad, desigualdad
#Salidas: guardar, 'Error en las entradas, digite un número entero'
def sumaDig(num):
    if type(num)==int or type(num)==float:
        num=abs(num)
        guardar=0
        while (num%10)!=0:
            num*=10
        while num!=0:
            guardar=guardar+num%10
            num=num//10
        return int(guardar)
    else:
        return 'Error en las entradas, digite un número entero'
#Ejercicio 4,
#Explicacion: Esta funcion indica si un número es palíndromo o no
#Entradas: numero
#Restricciones: Es un número entero.
#Herramientas: funciones type() y abs(), multiplicación, división entera, suma y módulo
#Salidas: True, False, 'Argumentos inválidos, digite un número entero'
def palindromo(num):
    if type(num)==int:
        num=abs(num)
        guardar=num
        resultado=0
        while num!=0:
            resultado=resultado*10+num%10
            num=num//10
        if resultado==guardar:
            return True
        else:
            return False
    else:
        return 'Argumentos inválidos, digite un número entero'
#Ejercicio: 5
#Explicacion: Esta función retorna el resultado de la sumatoria desde cero hasta un número entero positivo n, para ello se crean dos variables, contador servirá para
#el ciclo de repetición y la otra para representar el resultado, se va incrementando contador en uno y resultado se incrementa con respecto a contador 
#Entradas: n
#Restricciones: Es un numero entero positivo
#Herramientas: función type, mayor que, mayor o igual que, suma
#Salidas: resultado, 'Error en las entradas, digite un número entero positivo'
def sumaCoc(n):
    if type(n)==int and 0<n:
        resultado=0
        contador=0
        denominador=1
        while contador<=n:
            denominador=contador*(contador+1)
            contador+=1
        resultado=1/denominador
        return resultado
    else:
        return 'Error en las entradas, digite un número entero positivo'

# Ejercicio: 6
def calculoE(x,n):
    if type(x)==int and(type(n)==int):
        def productoria(a):
            contador=1
            resultado=1
            if a==0:
                return 1
            while contador<=a:
                resultado*=contador
                contador+=1
            return resultado
        resultado=0
        inicio=0
        for i in range (inicio,n+1):
            resultado=resultado+(x**i/productoria(i))
        return resultado
    else:
        return 'Argumentos inválidos, deben ser números enteros y A debe ser menor o igual que B'
#Ejercicio: #7
def multdig(num1,num2):
    nuevoNumero=0
    resultado=0
    while num1!=0:
        producto=((num1%10)*(num2%10))%10
        num1=num1//10
        num2=num2//10
        nuevoNumero=nuevoNumero*10+producto
    if num1==num2:
        while nuevoNumero!=0:
            resultado=resultado*10+nuevoNumero%10
            nuevoNumero=nuevoNumero//10
        return resultado
    else:
        'Error: deben ser número enteros del mismo tamaño'
# Ejercicio: #8
def hormiguitas(n):
    parejas=5
    contador=0
    hormiguitas=parejas*2
    while contador<=n:
        hormiguitas=hormiguitas - hormiguitas + parejas*3
        parejas=hormiguitas//2
        contador+=1
    return hormiguitas
# Ejercicio: #9
def numAppend(num1,num2):
    cantidadDig=0
    digitosAñdir=0
    global invertir
    if num2==0:
        cantidadDig=1
    while num2!=0:
        digitosAñdir=digitosAñdir*10+num2%10
        num2//=10
        cantidadDig+=1
    return num1*(10**cantidadDig)+invertir(digitosAñdir)
# Ejercicio:  #10
def div(dig,num):
    guardar=num
    digitosNum=0
    resultado=0
    while num!=0:
        digitosNum=num%10
        resultado=resultado*10+digitosNum//dig
        num//=10
    global invertir
    if guardar%10==0:
        return invertir(resultado)*10
    else:
        return invertir(resultado)
# Ejercicio: #11
# Ejercicio: #12
# Ejercicio: #13
# Ejercicio: #14
# Ejercicio: #15
# Ejercicio: #16
# Ejercicio: #17
# Ejercicio: #18
# Ejercicio: #19