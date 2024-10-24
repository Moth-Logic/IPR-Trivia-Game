""" Bibliotecas """
import time
from random import choice

""" Variables Globales """

Continuar_Jugando = True

""" Funciones """
def Imprimir_Bienvenida():
    """
    
        Descripción: 
        
        Función que imprime un mensaje de bienvenida al juego de Trivia.

        Entradas: 
        - Ninguna

        Salidas:
        - Mensaje de bienvenida.

    """

    # REVISAR: AÑADIR UN LOGO

    print("\n\n¡Bienvenido al Juego de Trivia: La Gran Batalla de Conocimientos!\n\n")
    print("\n\n¡Empecemos!\n\n")


def Imprimir_Pantalla_Blanco():

    """
    
        Descripción:

        Función que imprime una pantalla en blanco.

        Entradas:
        - Ninguna

        Salidas:
        - Pantalla en blanco.

    """

    print("\n" * 30)


def Imprimir_Menu_Opciones():
    """
    
        Descripción:

        Función que imprime un menú con las opciones de jugar o salir del juego.

        Entradas:
        - Ninguna

        Salidas:
        - Menú con las opciones de jugar, ver instrucciones, ver puntajes o salir del juego.

    """

    print("Menú de opciones:\n\n")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Puntajes")
    print("4. Salir\n\n")
    

def Obtener_Opcion_Menu():

    """
    
        Descripción:

        Función que obtiene la opción seleccionada por el usuario.

        Entradas:
        - Opción seleccionada por el usuario: int (1-4).

        Salidas:
        - Opción seleccionada por el usuario.

    """
    try:
        Opcion = int(input("Ingrese la opción deseada: "))
    except:
        raise TypeError("Por favor, ingrese un número entero entre 1 y 4.")

    if Opcion < 1 or Opcion > 4:
        raise ValueError("Por favor, ingrese un número entero entre 1 y 4.")

    return Opcion


def Obtener_Preguntas_Respuestas():

    """
    
        Descripción:

        Función que obtiene las preguntas y respuestas del archivo de 
        texto editable para poder actualizar el número de preguntas.

        Entradas:
        - Texto del archivo de preguntas y respuestas.

        Salidas:
        - Diccionario con las preguntas y respuestas.

    """

    try:
        with open('preguntas_respuestas.txt', 'r', encoding='utf-8') as archivo:

            cuestionario = archivo.readlines()
            matriz=[]
            nueva_lista=[]
            respuestas=[]

            for linea in cuestionario:

                letras=["A","B","C","D"]

                if linea[:1] in "123456789":

                    nueva_lista=[]
                    respuestas=[]

                    nueva_lista.append(linea)

                elif linea!="\n":
                    respuestas.append(linea)

                if len(respuestas)==4:

                    while respuestas!=[]:

                        opcion=choice(respuestas)  
                        respuesta=f"{letras[0]}{opcion.strip()}"
                        nueva_lista.append(respuesta)
                        respuestas.remove(opcion)
                        letras.remove(letras[0])  

                    matriz.append(nueva_lista)
        return matriz
    except Exception as error:
        raise Exception(f"Error:{error}")


def Obtener_Jugadores():

    '''

    Descripción:

    Funcion que recibe la cantidad de jugadores y sus nombres a un diccionario global.

    Entradas y Restriciones:
    
    -El numero de participantes: tiene que ser un numero entre el 1 al 5
    -El nombre de los participantes: Los nombres de los participantes no puede estar vacia y no puede haber nombres repetidos

    Salidas: Jugadores en un diccionario global

    '''

    Continuando = True

    while Continuando:

        try:

            Participantes = {}

            Nombres = []

            Numero_Participantes = int(input("Inserte la cantidad de participantes minimo 1 y maximo 5: "))
            
            while Numero_Participantes < 1 or Numero_Participantes > 5:
                print("El numero de participantes ingresados es incorrecto, vuelve a intentarlo.\n")
                Numero_Participantes = int(input("Inserte la cantidad de participantes (Número entre 1-5): "))

            for numero in range(Numero_Participantes):
                
                nombre = input(f"Ingrese el {numero + 1}.º jugador: ").strip().upper()

                print(nombre) # Debugging

                while nombre in Nombres or nombre=="" or not nombre.isalpha():
                    
                    if nombre in Nombres:
                        print("El nombre ya esta en uso o no es válido, este tiene que tener solo letras.\n")
                    
                    else:
                        print("El nombre ya esta en uso o no es válido, este tiene que tener solo letras.\n")
                    
                    nombre = input(f"Ingrese el {numero+1}.º jugador: ").strip().upper()
                
                Nombres.append(nombre)

            for usuario in Nombres:
                Participantes[usuario] = 0
            
            Continuando = False

        except Exception as error:

            if ValueError:
                print("Asegurese de ingresar solo numeros.\n")
            else:
                print (f"Error:{error}")

    return Participantes


def Obtener_Numero_Preguntas():

    """
    
        Descripción:

        Función que obtiene el número de preguntas que se le harán a cada jugador.

        Entradas:
        - Número de preguntas.

        Salidas:
        - Número de preguntas.

    """


def Guardar_Puntajes(Jugadores):

    """
    
        Descripción:

        Función que envia los puntajes de los jugadores a un archivo de texto.

        Entradas:
        - Jugadores es una tupla con el nombre y el puntaje.

        Salidas:
        - Archivo de texto con los puntajes de los jugadores.

    """

    text_file = open("Puntajes.txt", "w")

    for Jugador, Puntaje in Jugadores:
        text_file.write(f"{Puntaje},{Jugador}\n")
    
    text_file.close()


def Empezar_Juego(Diccionario_Preguntas_Respuesta, N_Preguntas):

    """
    
        Descripción:

        Función que se encarga de realizar el juego de Trivia con los valores
        previamente ingresados.

        Entradas:
        - Dict con las preguntas y respuestas.
        - Número de preguntas.
        - N_Jugadores es un número entero que representa el número de jugadores.        

        Salidas:
        - Juego de Trivia.
    
    """


def Jugar_Trivia():

    """
    
        Descripción:

        Función que obtiene todos los datos necesarios para empezar el juego de Trivia.

        Entradas:
        - Jugadores.
        - Diccionario con las preguntas y respuestas.
        - Número de preguntas.

        Salidas:
        - Juego de Trivia.
        
    """
    
    Jugadores = []

    Matriz_Preguntas_Respuesta = Obtener_Preguntas_Respuestas()

    N_Preguntas = Obtener_Numero_Preguntas()

    Diccionario_Jugadores = Obtener_Jugadores()

    Guardar_Puntajes(Jugadores)

    Empezar_Juego(Diccionario_Jugadores, Matriz_Preguntas_Respuesta, N_Preguntas)


def Imprimir_Como_Jugar():

    """
    
        Descripción:

        Función que imprime un mensaje con las instrucciones de cómo jugar.

        Entradas:
        - Ninguna

        Salidas:
        - Instrucciones de cómo jugar.

    """
    print("¿En qué consiste?\n\n")
    print("Consiste en una serie de preguntas y respuestas sobre diversos temas como historia, ciencia, deportes, entretenimiento, geografía, entre otros. Los jugadores compiten para ver quién puede responder correctamente a la mayor cantidad de preguntas.\n\n")

    print("Instrucciones de cómo jugar:\n\n")
    print("1. Primero, deberás ingresar el número de jugadores que participarán en el juego.")
    print("2. Luego, deberás ingresar el número de preguntas que se le harán a cada jugador.")
    print("3. A continuación, deberás ingresar el nombre de cada jugador.")
    print("""4. Luego de ingresar el nombre de cada jugador, se le harán las preguntas a cada 
          uno por turnos.""")
    print("5. Al finalizar, se mostrará el puntaje de cada jugador y el ganador del juego.\n\n")

    print("\n\n Presiona cualquier tecla para continuar \n\n")

    input()


def Imprimir_Puntajes():

    """
    
        Descripción:

        Función que imprime los puntajes de los jugadores y si aún no hay entonces imprime "No hay puntajes".
        
        Entradas:
        - Puntajes de los jugadores.

        Salidas:
        - Puntajes de los jugadores.

    """


def Salir():

    """
    
        Descripción:

        Función que cambia el valor de la variable "Continuar_Jugando" a False.
    
        Entradas:
        - Ninguna

        Salidas:
        - Cambio de la variable "Continuar_Jugando" a False.

    """

    global Continuar_Jugando

    Continuar_Jugando = False


def Ejecutar_Opcion(Opcion):

    """
    
        Descripción:

        Función que ejecuta la opción seleccionada por el usuario.

        Entradas:
        - Opción seleccionada por el usuario, es número entero entre 1 y 4.

        Salidas:
        - Ejecución de la opción seleccionada por el usuario.

    """

    Imprimir_Pantalla_Blanco()

    if Opcion == 1:
        Jugar_Trivia()
    elif Opcion == 2:
        Imprimir_Como_Jugar()
    elif Opcion == 3:
        Imprimir_Puntajes()
    else:
        Salir()


""" Función Principal """
def main():

    """
    
        Descripción: 
        
        Función principal del programa. Este llamará las funciones necesarias 
        para el correcto funcionamiento del proyecto.

        Entradas: 
        - Ninguna

        Salidas:
        - Juego de Trivia.

    """

    try:

        Imprimir_Bienvenida()

        time.sleep(3)

        global Continuar_Jugando

        Continuar_Jugando = True

        while Continuar_Jugando:

            Imprimir_Pantalla_Blanco()

            Imprimir_Menu_Opciones()

            Opcion = Obtener_Opcion_Menu()

            Ejecutar_Opcion(Opcion)

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

    finally:
        print("Gracias por jugar!")
        time.sleep(2)


""" Ejecución del Programa """
if __name__ == "__main__":
    main()