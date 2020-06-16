import re
#Expresiones regulares
 
while True:
#Ingresa las operaciones en una cadena
    entrada = input("Ingrese la operación : ")
    entrada = entrada.replace(" ", "")
 
    if entrada=="0":
        break
 
    valores=re.findall("([0-9]+)([\+\-*\/])?",entrada)
 
    if valores:
 
        for i in range(0,len(valores)):
            if i==0:
                resultado=int(valores[i][0])
            else:
                if operacion=="+":
                    resultado=resultado+int(valores[i][0])
                elif operacion=="-":
                    resultado=resultado-int(valores[i][0])
                elif operacion=="*":
                    resultado=resultado*int(valores[i][0])
                elif operacion=="/":
                    resultado=resultado/int(valores[i][0])
 
            operacion=valores[i][1];
 
        print("Resultado: ",resultado)
