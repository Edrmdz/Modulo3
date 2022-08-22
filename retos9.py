#Reto semana 9
#Un bucle infinito solicitara una letra
#el usuario especificara la condicion para terminarla
#Se hará un funcipon que imprimaen pantalla la letra previa y siguiente a la elegida

dicc = {'A':["NADA","B"], 'B':["A", "C"], 'C':['B', 'D'],         #diccionario para buscar las letras previas y posteriores
        'D':["C","E"], 'E':["D", "F"], 'F':['E', 'G'],
        'G':["F","H"], 'H':["G", "I"], 'I':['H', 'J'],
        'J':["I","K"], 'K':["J", "L"], 'L':['K', 'M'],
        'M':["L","N"], 'N':["M", "O"], 'O':['N', 'P'],
        'P':["O","Q"], 'Q':["P", "R"], 'R':['Q', 'S'],
        'S':["R","T"], 'T':["S", "U"], 'U':['T', 'V'],
        'V':["U","W"], 'W':["V", "X"], 'X':['W', 'Y'],
        'Y':["X","Z"], 'Z':["Y", "NO HAY"] }
#print (dicc)
def imprime_vecinos():                                              #funcion que imprime letra anterior y siguiente
  #  letra = str(input(" ingresa una letra: ").capitalize)
    print ("LETRA PREVIA ES " + (dicc[letra][0]) + " Y LA SIGUIENTE ES " +(dicc[letra][1]))

while True:                                                         #se crea ciclo infinito con while true
    opcion = input("Ingresa una dato (1) o Terminar (2): ")         # menu para seleccionar ingresar letra o cerrar programa
    #while opcion == 1:
    if opcion == '1':                                               #con opcion 1 se realiza la busqueda de la letra
        letra = str(input(" ingresa una letra en MAYUSCULA: "))
        #letra = (str(input("Ingresa una letra: ")))
        #print(letra)
        imprime_vecinos()                                           #se llama la funcion para imprimir las letras vecinas
    if opcion == '2':                                               #con opcion 2 se cierra termina el ciclo infinito
    #else:
        print("Adios")
        break
