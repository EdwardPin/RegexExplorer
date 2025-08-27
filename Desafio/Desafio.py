import re
#Se le pide al usuario el texto para analizar
texto = input("Por favor introducir el texto: ")
#Estos son los diferentes commandos de regular expression para cada diferente tipo de dato
enteros = r"-?\b\d+\b"  
flotante = r"-?\b\d+\.\d+\b"
booleano = r"\b(True|False)\b"
string = r'"(.*?)"'
lista = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
#Aqui se hace la busqueda de cada variable complatible con los comandos previos
resul_enteros = re.findall(enteros,texto)
resul_float = re.findall(flotante,texto)
resul_bool = re.findall(booleano,texto)
resul_string = re.findall(string,texto)
resul_list = re.findall(lista,texto)
#Se imprimen los resultados con la cantidad de elementos en cada resultado
print("Los resultado encontrados fueron: ")
print("1. Se encontraron: ", len(resul_enteros), " enteros, siendo = ", resul_enteros)
print("2. Se encontraron: ", len(resul_float), " flotantes, siendo = ", resul_float)
print("3. Se encontraron: ", len(resul_bool), "booleanos, siendo = ", resul_bool)
print("4. Se encontraron: ", len(resul_string), "strings, siendo = ", resul_string)
print("5. Se encontraron: ", len(resul_list), "listados, siendo = ", resul_list)
