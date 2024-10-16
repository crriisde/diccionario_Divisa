print (" ") #Esta linea Define las comillas a mostrar 
print ("Cristian David Salas De La O 3-W") #Esta linea Muestra el nombre del programador 
print (" ") #Esta linea Define las comillas a mostrar  
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}  #Esta linea define el simbolo de cada divisa
divisa_usuario = input("Introduce una divisa: ")  #Esta linea solicita introudcir una divisa
if divisa_usuario in divisas:  #Esta linea define el if de la funcion
    print(f"El simbolo de {divisa_usuario} es: {divisas[divisa_usuario]}") #Esta linea muestra las divisas
else: #Esta linea define que hacer si no se cumple el if
    print("La divisa no esta en el diccionario.") #Esta linea muestra que la divisa no esta en la funcion 
