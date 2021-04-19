
import random
#-----------------------------------------IMAGENES-----------------------------------------

#Imagen titulo
titulo = ("""

░██████╗██████╗░░█████╗░░█████╗░███████╗      ░██████╗░░█████╗░████████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝      ██╔════╝░██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░      ██║░░██╗░███████║░░░██║░░░█████╗░░
░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░      ██║░░╚██╗██╔══██║░░░██║░░░██╔══╝░░  
██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗      ╚██████╔╝██║░░██║░░░██║░░░███████╗
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝      ░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

""")
#Imagen final
final_img = ("""
            
████████╗██╗░░██╗███████╗   ███████╗███╗░░██╗██████╗░
╚══██╔══╝██║░░██║██╔════╝   ██╔════╝████╗░██║██╔══██╗
░░░██║░░░███████║█████╗░░   █████╗░░██╔██╗██║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░   ██╔══╝░░██║╚████║██║░░██║
░░░██║░░░██║░░██║███████╗   ███████╗██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝   ╚══════╝╚═╝░░╚══╝╚═════╝░
            """)

#Caja de guiones
box = 52 *"_"
#imagen de inicio
img_1 = ("""
         _____________
         | | | | | | |     ()
         | | | | []  |    /||\ 
         -------------     ||
""")
#imagen de respuesta puerta
img_2 = ("""
         ()           <()>
        /||\          /||\ 
         ||            ||
""")
#imagen de respuesta puerta/dormir
img_3 = ("""
        \()/          <()>
         ||  ----- <-r/||\ 
         ||            ||
""")
#imagen de respuesta puerta/puerta
img_4 = ("""                        ________
            () ___     |  EXIT  |
          \/\ \        |      ()|
            //\\\//     |        |
            ||         |________|
""")
#imagen de respuesta rendija
img_5 = ("""
             ()           
            /||\          
             ||         /_.()- 
""")
#imagen rata en habitación
img_6 = ("""                    
             ()              <O°         
            /||\            -( \ 
             ||             _( )\___)         
""")
#imagen rata arrancandote la cabeza
img_7 = ("""                    
                        _.<O°._         
                 O¬¬¬()(. )(. )()  
                ()       ()() //
             .  / _      |. | 0  
          /||\  .       / / \ \ 
           ||           ||   ||\____)     
""")
#imagen rata muerta
img_8 = ("""                    
____                  _.<O°._
\  /|  ()           ()(. )(. )()
 \/ | /||`-o        ||  ()()  ||
 /\ |  ||              /_/\_\___ 
""")
#imagen de error
img_error = ("""
                     -__,~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
                             ,.
                            /||\ 
                             || 
""")

#-----------------------------------------DIALOGOS-----------------------------------------

#inicio
inicio = ("\nTe encuentras en una celda junto con tu compañero,\n"
        "este es llevado a ejecucción y por alguna razón tu celda se queda abierta.")

#Primera Opción
primer_opc = ("Tienes dos opciones, irte por una puerta [A] o irte por una rendija [B]"
                "\n Eliges: ")
#Opción puerta
opcion_puerta = "\nEntras por la puerta y segundos depués entra un guardia"

#Opción escape puerta
escape_puerta = ("Tienes dos opciones, hacerte el dormido [A] o correr a otra puerta al otro lado del cuarto [B]"
                  "\n Eliges: ")

#final puerta 1
final_puerta_1 = "\nEl guardia se da cuenta y saca su paralizador"

#final puerta 2
final_puerta_2 = "\nHaz conseguido salir de SPACE GATE"

#sentencia puerta 1
sentencia_final_1 = "PASAS 40 AÑOS EN SPACE GATE HASTA FINALMENTE MORIR"

#sentencia puerta 2
sentencia_final_2 = "ENCUENTRAS UNA NAVE Y TE ESCAPAS AL PLANETA DEMBAO"

#Error
error = "\nTU CABEZA EXPLOTÓ POR NO ELEGIR UNA OPCIÓN VALIDA"
explosión_de_cabeza = box + "\n" + error + "\n" + img_error + "\n" + final_img

#Opción rendija
opcion_rendija = "\nEntras por la rendija y te deslizas hasta salir por otra que da a otro cuarto"

#Opción escape rendija
escape_rendija = ("Al entrar al cuarto, te encuentras con los restos de un androide,\n"
                  "[A] decides tomar un brazo, [B] no decides tomar nada"
                  "\n Eliges: ")
tomaste_brazo = "\nTomas el brazo"
no_tomaste_brazo = "\nNo tomas el brazo"
#Abrir puerta rata
puerta_rata = (" y te encuentras con una puerta, la abres y entras a una habitación.\n" 
              "En la habitación hay una rata antropomorfica leyendo, deja su libro y te voltea ver")

#Problema rata
numero_aleatorio = random.randint(1,9)
resultado = 13*numero_aleatorio
problema_rata = ("La rata te dice que te puede sacar solo si respondes cuánto es 13*{}"
                  "\n Respuesta: ".format(numero_aleatorio))

#Respuesta rata bien
respuesta_rata_bien = ("\nTu respuesta es correcta, la rata abre su boca y te come.\n"
                       "Recuperas la conciencia y te encuentras en un cuarto con una puerta,\n"
                       "te paras y abres la puerta.\n")
#Respuesta rata mal
respuesta_rata_mal = ("\nTu respuesta es incorrecta, la rata se enoja\n"
                      "Y aumenta dos veces su tamaño junto con sus musculos.\n"
                      "Te ruge y te da un manotazo, te estrellas y se dirige hacia ti\n")
#Opción rata enojada
opción_rata_enojada = ("La rata empieza a correr y debes tomar una decisión,\n"
                        "[A] corres hacia la derecha, [B] corres hacia la izquierda"
                            "\n Eliges: ")
#Opción rata enojada A
opción_rata_enojada_a = ("\nLa rata alcanza a tomar tu pie porque es zurda,\n"
                         "te golpea y arranca la cabeza.\n")
#Sentencia rata cabeza
sentencia_final_rata_cabeza = "\nLA RATA SE TERMINA POR COMER TU CUERPO\n"

#Opcion rata enojA B
opción_rata_enojada_b = ("\nEntras a un espacio entre unas cajas, la rata no te puede tomar,\n"
                         "rápido piensas en tomar una herramienta para defenderte, recuerdas\n"
                         "que ")
#Sentencia final de la rata muerta
sentencia_final_rata_muerta = ("\nEL CUERPO DE LA RATA TE DA SUS PODERES, ROMPES LA PARED Y\n" 
                              "TE ESCAPAS, HAZ CONSEGUIDO SALIR DE SPACE GATE\n")
#-----------------------------------------CÓDIGO-----------------------------------------

tomar_brazo = False
brazo = no_tomaste_brazo

print(titulo +78*"-"+ "\n" )

print(box + inicio + "\n" + img_1 + box)

respuesta = input(primer_opc)

if respuesta == "A" or respuesta == "a":
    print(box + opcion_puerta + "\n" + img_2 + box)
    respuesta = input(escape_puerta)

    if respuesta == "A" or respuesta == "a":
        print(box + final_puerta_1 + "\n" + img_3)
        print(sentencia_final_1 + "\n" + final_img)
    elif respuesta == "B" or respuesta == "b":
        print(box + final_puerta_2 + "\n" + img_4)
        print(sentencia_final_2 + "\n" + final_img)
    else:
        print(explosión_de_cabeza)
        exit()

elif respuesta == "B" or respuesta == "b":
    print(box + opcion_rendija + "\n" + img_5 + box)
    respuesta = input(escape_rendija)
    if respuesta == "A" or respuesta == "a":
        tomar_brazo = True
        brazo = tomaste_brazo
    elif respuesta != "A" and respuesta != "a" and respuesta != "B" and respuesta != "b":
        print(explosión_de_cabeza)
        exit()
    print(box + brazo + puerta_rata + "\n" + img_6 + box)
    respuesta = int(input(problema_rata))
    if respuesta == resultado:
        print(box + respuesta_rata_bien + box + final_puerta_2 + "\n" + img_4 + "\n" + sentencia_final_2 + "\n" + final_img)
    else:
        print(box + respuesta_rata_mal + box)
        respuesta = input(opción_rata_enojada)
        if respuesta == "A" or respuesta == "a":
            print(box + opción_rata_enojada_a + img_7 + sentencia_final_rata_cabeza + final_img)
        elif respuesta == "B" or respuesta == "b":
            if tomar_brazo == True:
                sentencia = sentencia_final_rata_muerta
                img_brazo = img_8
                arma = ("tomaste el brazo del androide, este tiene un rayo laser que usas\n"
                        "y le perforas el cerebro a la rata, esta muere.\n")
            else:
                sentencia = sentencia_final_rata_cabeza
                img_brazo = img_7
                arma = ("no tomaste el brazo del androide, entonces la rata rompe las cajas,\n"
                    "te golpea y arranca la cabeza.\n")
            print(box + opción_rata_enojada_b + arma + img_brazo + sentencia + final_img )
else:
    print(explosión_de_cabeza)
    exit()