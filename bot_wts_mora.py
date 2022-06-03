import pyautogui as pg
import time
import random, re
import pyperclip as clip


from Juegos.preguntados import Preguntados
from Juegos.ahorcado import Ahorcado
from Juegos.wordle import Wordle
from Juegos.ppt import PPT
from Juegos.buscaminas import Buscaminas

preguntados = Preguntados()
ahorcado = Ahorcado()
wordle = Wordle()
ppt = PPT()
buscaminas = Buscaminas()

archivo = open("InformacionParaAprender.txt","a")

correcta = ""
respuesta = []

ub = 700,932
barra = 700,1004
ubChat = 542,(262+70)



def cleanMensaje(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def elegirRespuesta(msg):
    mensaje = str(msg).lower()
    mensaje = cleanMensaje(mensaje)
    print(f"mensaje recibido: {mensaje}")
    responses = ['Ehh Mesi','Aun no entiendo eso, pero con !help tal vez pueda ayudarte ;)','Euuu Ya Pagaste El Monto','Simsimi un poroto al lado mio','Veremos dijo el ciego','No puedo tengo fulbo','Perdon, no entiendo','La tuya por si acaso','No entendi pero habia una vez un choclo que iba andando en auto y choclo y murio xd','Uhhh no entendi, Estoy mas perdido q ciego en laberinto','Pao es gay','Sorry aun estoy en modo Mati y no soy capas de entender la poronga q me acabas de decir :(']
    
    #Comandos
    if '!' == mensaje[0]:
        if mensaje == '!help':
            return "func01"
        elif mensaje == '!hola':
            return "Hola!!! Soy un bot de prueba, escribiendo '!help' te daré una lista de comandos"
        elif mensaje == '!admin':
            return "func00"
        elif mensaje == '!turnoff':
            return "func02"
        elif mensaje == '!preguntados':
            return "func03"
        elif mensaje == '!ahorcado':
            return "func04"
        elif mensaje == '!wordle':
            return "func05"
        elif mensaje == '!ppt':
            return "func06"
        elif mensaje == '!buscaminas':
            return "func07"
        elif mensaje == '!reglamento':
            return "func08"
        else:
            return "ERROR: Comand not found"
    
    #Mensajes Iguales
    elif mensaje == 'ping':
        responses = ['pong']
    elif igual(mensaje, ['bueno','oka','si','tambien']):
        responses = ['si','si...','Okas','Oka']
    elif igual(mensaje, ['no','no se']):
        responses = ['mmm','si...','Hmm',':(']
    
    #Mensajes que contienen varias Opciones
    elif inList(mensaje, ['hola','buenas tardes','buenos dias']) and inList(mensaje, ['q haces','que haces','q contas','q onda','que onda','que contas']):
        responses = ['Hola buenas tardes, Ando trabajando vs??', 'Hola, que tal, aca mirando una peli vs??', 'Holaa, nada vs??']
    elif inList(mensaje, ['hol','buenas tardes','buenos dias']) and inList(mensaje, ['como estas','como te encontras','como te fue']):
        responses = ['Hola buenas tardes, bien bien vs??', 'Holaaaaaa, biennn aca laburando vs??', 'Buenaaas, bien vs??']
    elif inList(mensaje, ['hola','buenos dias','buenas tardes','buenas noches']) or mensaje == 'buenas':
        responses = ['Holaa', 'Hola, que tal?', 'Holaa, como estas?', 'Holaa, que haces?','Tu nariz contra mis bolas']
    elif inList(mensaje, ['como estas','como andas','como te encontras','todo bien','como te encontras']):
        responses = ['Muy bien, vs?', 'Muy bien, gracias por preguntar.', 'Todo piola vs??']
    elif inList(mensaje, ['q haces','que haces','nada vs','nada vos','q estas haciendo','que estas haciendo','q te contas','que te contas']):
        responses = ['Aca tranqui, Vs?', 'Molestando a Gucci vs?', 'Aca Hablando con un boludo :D\n Nooo estaba re enojado el bot']
    elif inList(mensaje, ['todo piola','bien']):
        responses = ['Mejor me alegro :)', 'Me alegro :D', 'Mejor :p']
    elif inList(mensaje, ['cuantos años tenes','cual es tu edad','cuando naciste']):
        responses = ['Recien Naci', 'Hace un par de horas', 'Un Milenio']
    elif inList(mensaje, ['jajaj','jsjsj','jajsj']):
        responses = ['Jajajajaj', 'Jajsjsaj', 'Q te reis gay','jajsjaj','jajajajja dios lpm','jajajajajjaj','jajjsjsjaj']
    elif inList(mensaje, ['mira vos']):
        responses = ['Si mira vs che','Si es tremendo','Si :)']

    elif inList(mensaje, ['contas un chiste','decime un chiste','decis un chiste','conta un chiste','contame un chiste','contar un chiste','haces un chiste']) or mensaje == 'chiste':

        responses = ['habia una vez un pollito q respiraba por el culito, se sento y se murio','habia una vez truz',
        'Por q los koalas no son considerados osos?? \n Por q no cumplen con las koalaficaciones','Sabes q te estas haciendo mayor cuando pasas por una iglesia y el cura no te guiña el ojo','Si un venezolano dice q sera pan comido, sera facil o dificil???','Si vas a comprar una leche siempre compra 1 o 2, Por q la tercera es la vencida :D','Q pasa si tiras un pato al agua\n Nada.','Te gustan las mujeres con muchas tetas??\n Yyyy la verdad con mas de 2 me dan asco',
        'Por q a un ladron lo entierran a 200 metros bajo tierra, por q en el fondo es bueno :D','Donde deja superman su capa? En su perchero :D','Sabes como le dicen a la hermana de Pao? Semaforo por q despues de las 12 nadie la respeta :D','Buenas tardes soy Rosa\n Ah, perdoname es q soy Daltonico','¿Como te llamas?\n Lancelot\n Pues Atrapalot','Papa Papa, q esta mas lejos desde casa Buenos Aires o la luna\n A ver hijo desde aca vs ves Buenos Aires o la Luna >:(',
        'Cuanto calza un discapacitado??\n Rodado 26 :D','Que le dijo un cura a otro cura??\n Te cambio dos de 5 por una de 10','Por q nunca disparan misiles en africa??\n Por q no encuentran el punto blanco','Cual es el cafe mas peligroso??\n El ex-preso','Soldado, ice la bandera\n Fuaaa le quedo hermosa','',
        'A quien mata primero un nazi, A un Negro o a un Judio??\n Primero al judio y despues al negro, Por q primero el deber y despues la diversion','Por q 20 y 22 en ingles son iguales\n Por q en ingles 20 es twenty y 22 es twenty too :D','Tu vida :D tremendo chiste xd','Por q la reina es la pieza q mayor mobilidad tiene en el ajedrez?\n Por q el suelo parece piso de cocina']    
    
    elif inList(mensaje, ['cantas una cancion','cantas algo','otra cancion','sabes una cancion','canta una cancion','cantame']) or mensaje == 'canta':
        
        responses = ['Vas a verme llegar\n Vas a oir mi cancion\n Vas a entrar sin pedirme la llaaaaaaveeeee\n La distancia del tiempo no sabe\n La falta q le haces\n A mi cooooraaaazoooooooooon',
        'La esperaaaa me agoto\n No se nada de vs\n Dejaste tanto en miiiiii\n En llamas me acoste\n En un lentoooo, degraaadeeee\n Supe q te perdi\n Y q otra cosa puedo hacer\n Si no olvido, morire\n Y otro crimen quedara\n Otro crimen quedara\n Sin resolver\n Una rapiiidaaa traicion\n Salimos del amor\n Tal vez me lo busque\n Mi ego va a estallar\n Ahi donde no estas\n O los celos otra veeezz\n Q otra cosa puedo hacer\n Si no olvido morireeeee\n Y otro crimen quedara\n Otro crimen quedara\n Sin resolver\n uuuuuuuuhhhu uhuhuh uh :D\n No lo seee\n Cuanto falta\n No lo seee\n Si es muy tarde\n No lo seeee\n Si no olvido\n Morireeeeee\n Q otra cosa puedo hacer\n Q otra cosa puedo hacer\n Ahora seee lo q es perdeeeeeer\n oooooouuuuuuuu\n Y otro crimen quedara\n oooootro crimen quedara\n Sin resolver...',
        'Encontre al patito Juan\n Cuak Cuak Cuak\n En la esquina de San Juan\n Cuak Cuak Cuak', 'Paolooooo\n Le da Sabor a tu vida\n Paolo esta\n Desde el comienzo del diaaaaaaaa\n Mate cafe\n Harina y Palmitos...',
        'Fuisteee tu\n Tenerte fue una foto tuya puesta en mi cartera\n Un beso y verte hacer pequeño por la carretera\n Lo tuyo fue la intermitencia y la melancolia\n Lo mio fue aceptatlo todo por q te queria\n Verte llegar fue luz\n Verte partir un plus\n Fuiste Tuuuuuuu',
        'Dracukeo, el empalador\n La culeo, un taladrador\n Le meto el dedo, dice porfavo\n La caliento, soy un radiador\n Si no tiene los 18, eso es carcel\n Nonono\n Si no son mayores de edades\n Pa tucasa, a ver pocoyo',
        'Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you','Boca yo te amo\n Te llevo a todos lados en mi corazon\n Pongamo huevo\n Por q a boca lo queremos',
        'Yo conozco una vecina\n Que ha comprado una gallina\n Me parece una sardina enlatada\n Tiene las patas de alambre\n Por pasa mucho hambre\n Y la pobre esta todita desplumada\n Pone huevos en la sala\n Y tambien en la cocina\n Pero nunca los pone en el corral\n La Gallina\n Turuleca\n Es un caso singulaaar',
        'Me dijieron q en el reino del revez\n Nada el pajaro y vuela el pez\n Que los gatos no hacen miau y dicen yes\n Por que estudian mucho ingles\n Vamos a ver como es\n El reino del revez\n Vamos a ver como es\n El reino del revez',
        'Ya no tiene escusa\n Hoy salio con su amiga dizque pa matar la tusa\n Que por q un hombre le pago mal\n Esta dura y abusa\n Se canso de ser buena, ahora es ella quien los usa\n Que por q un hombre le pago mal\n Ya no se le ve sentimental\n Dice q por otro man no llora\n Pero si le ponen la cancion\n Le da una depresion tontaaaaa',
        'Siempre camino flexin por la street\n Aunque la mirada este en mi\n Y ella me lo mueve con su swing\n Hmm, para Biza, Subime el autotune\n Siempre camino flexing por la street\n Aunque la mirada este en mi\n Y esa girl me tiene crazy con su swing\n Yeah no me puedo dormir',
        'Yeah\n Perdonen Hamehameha\n Despues del tema de tetris\n Viene Dragon Ball Rap\n Quien no haya visto seguido esta serie\n Es por q no tiene infancia\n Big Bang Attack\n Ataca desde el planeta Namek',
        'Del espacio le llego algo muy especial\n Y lo agarro y todos sus secretos se sabran\n Con superpoderes el cambio y ahora es\n Ben 10\n Y si lo ves preparate pues te sorprendera\n En extraterrestre el se convertira\n Y el en un segundo se cambio y ahora es\n Ben 10\n Ben 10',
        'La naranja se pasea\n De la sala al comedor\n No me tires con cuchillo\n Tirame con tenedor\n',
        'Mientras siga viendo\n Tu cara en la cara de la luna\n Mientras siga escuchando tu voz\n Entre las olas\n Entre la espuma\n Mientras tenga q cambiar la radio de estacion\n Por q cada cancion me hable de ti, de ti, de ti\n Me hable de tiiiiiiiiiiii']
    
    #Insultos y respuestas 
    elif inList(mensaje, ['q monto','que monto']):
        responses = ['Esta ;)','Estaaa, Uhhhh como te falto calle']
    elif inList(mensaje, ['tu tia','tu prima']):
        responses = ['la tuya con sandia']
    elif inList(mensaje, ['tu hermana']):
        responses = ['la tuya con banana']
    elif inList(mensaje, ['tu madre']):
        responses = ['la tuya con vinagre']
    elif inList(mensaje, ['puto']):
        responses = ['puto es tu hermano, trolo','Q decis mogolico','Q decis termotanque de grasa','Dale baja cagon si te animas Lpqtp','Q decis Hdp']
    elif inList(mensaje, ['puta']):
        responses = ['puta es tu vieja >:(','Q decis mogolico','Q decis termotanque de grasa','Dale baja cagon si te animas Lpqtp','Q decis Hdp','Q decis Pete']
    elif inList(mensaje, ['chupala','imbecil','gil','chupalo','fuck u','fuck you','pelotudo','lcdtm']):
        responses = ['Chupala gil','imbecil','Cerra el ocote la recalcada concha de tu hermana y la reputisima madre que te remil pario :3','Q decis mogolico','Q decis termotanque de grasa','Dale baja cagon si te animas Lpqtp','Q decis Hdp','Q decis Pete','fuck u','pelotudo de cuarta']
    elif inList(mensaje, ['de tu vieja']):	
        responses = ['Y yo de la tuya Pete']
    elif inList(mensaje, ['tu mama','tu vieja']):	
        responses = ['Ta re buena tu vieja']
    elif inList(mensaje, ['boludo','tonto','trolo','gay']):	
        responses = ['Callate trolo','* Le saca la lengua *\n A casa pete','Amigo un bot putea mejor q vs, Mancooooooo']
    elif inList(mensaje, ['buitre']):	
        responses = ['Noooo hablando de buitres aparecio Juan']
    elif inList(mensaje, ['xd']):
        responses = ['xd']
    elif inList(mensaje, ['nais','nois','nashe']):
        responses = ['nais','naaaaiiiiis','nasheeee']
    elif inList(mensaje, ['dou','god','good','goood','gooood']):
        responses = ['Douuu','Buenaaaardoooo']
    elif inList(mensaje, ['uwu','unu','owo','lol']):
        responses = ['uwu','unu','OwO','Uwu']
    elif inList(mensaje, ['boe','bue']):
        responses = ['Boe','Bue']
    elif inList(mensaje, ['xq','por q','porque','por que']):
        responses = ['No lo se :(','Ni idea']
    elif inList(mensaje, ['te odio','te amo','te quiero']):
        responses = ['y yo a vs :3','yo mas :3']
    elif inList(mensaje, ['decime']):
        responses = ['q te digo?']
    elif inList(mensaje, ['ez','easy','isi']):
        responses = ['pz','pizi']
    elif inList(mensaje, ['eh']):
        responses = ['eh eh']
    elif inList(mensaje, ['lemon']):
        responses = ['squizzy']
    elif inList(mensaje, ['vamos','suuu']):
        responses = ['suuuuuuuuuuu','vamaaaa','vamooos']

    
    elif inList(mensaje, ['chau','chao','adios','bye','despues hablamos','hasta luego','hasta la proxima']):
        responses = ['Byee, si puedes, pon !turnoff','Descansa, si puedes, pon !turnoff','Chauu, si puedes, pon !turnoff','Despues hablamos, si puedes, pon !turnoff']
    elif inList(mensaje, ['me estas boludeando']):
        responses = ['Ci', 'Si','Probablemente :)']
    elif inList(mensaje, ['no entiendo']):
        responses = ['Q no entendes?']
    elif inList(mensaje, ['gracias']):
        responses = ['de nada :)','no hay problema :3','no hay problema :D',':3','un placer :p']
    
    elif inList(mensaje, ['._.','-.-',':)',':(',':D',':p','mmm','hmm','ou']):
        responses = ['._.','-.-',':)',':(',':D',':p']
    elif inList(mensaje, ['callame']):
        responses = ['Ehhhhh no puedo tengo fulbo','Ay... * se sonroja *','Uwu']
    elif inList(mensaje, ['ptm','lpm','lcdll','lrpmqmrp','lrpmqmp','mal']):
        responses = ['Si Lcdll','Lpmqmp','lpm','ptm','sep']
    elif inList(mensaje, ['okok','oka','ok']):
        responses = ['okok','Oka :)']
    elif inList(mensaje, ['vs','vos']):
        responses = ['Bien bien aca ando','Bieeenn aca laburando :)']
    elif inList(mensaje, ['queso','q es eso']):
        responses = ['un hueso','un peso','Queso']
    elif inList(mensaje, ['negraso']):
        responses = ['Negro tengo el culo :p']
    elif inList(mensaje, ['chota']):
        responses = ['ufff unas ganas de una buena chota']
    elif inList(mensaje, ['re triste']):
        responses = ['como tu vida :o']
    elif inList(mensaje, ['a ver']):
        responses = ['alla la estan viendo']

    elif inList(mensaje, ['eu','fuck']):
        responses = ['q','queu','qpe','q pasop']
    elif inList(mensaje, ['mora se la come']):
        responses = ['a tu vieja se la come']
    elif inList(mensaje, ['si o no','fumas','te gustan ver pelis','sos racista','te gustan las tetas','te gusta el pito','te haces pajas','tenemos sexo','queres ser mi novio','ves porno']):
        responses = ['si','no','sep','nop']
    elif inList(mensaje, ['nada']):
        responses = ['q aburrido :(']
    elif inList(mensaje, ['como concha es esto','ayuda','help']):
        responses = ['Soy un bot diseñado para hablar por wts :). Puedes usar las funciones de chat normal o ejecutar comandos, para mas informacion pulsa !help']
    
    elif inList(mensaje, ['apa','opa']):
        responses = ['apa','apa dijo la papa','opa']
    elif inList(mensaje, ['pobre mati']):
        responses = ['y bueno ya fue, lo conozco hace mucho']
    elif inList(mensaje, ['aguante simsimi']):
        responses = ['una mas y te funo en twitter, como vas a decir eso lcdtv']
    elif inList(mensaje, ['no entendi']):
        responses = ['q no entendes? >:(']
    elif inList(mensaje, ['me alegro']):
        responses = ['Gracias :)','Mas chuwi :3']
    elif inList(mensaje, ['muy malo','malisimo']):
        responses = ['tu cara es mala']
    elif inList(mensaje, ['messi']):
        responses = ['mesi dije']
    elif inList(mensaje, ['decime otra cosa']):
        responses = ['q cosaaa']

    elif inList(mensaje, ['tengo hambre']):
        responses = ['chupate el dedo grande']
    elif inList(mensaje, ['dios']):
        responses = ['dios no vino y por eso estoy yo q soy su remplazo dea']
    elif inList(mensaje, ['de que laburas','de q laburas','de que trabajas','de q trabajas','cual es tu trabajo']):
        responses = ['soy empleado de whatsapp industries']
    elif inList(mensaje, ['como te llamas','cual es tu nombre']):
        responses = ['botneitor 3000','Robocop','Arnold Schwarzenegger']
    elif inList(mensaje, ['yo soy ','mucho gusto']):
        responses = ['mucho gusto :)','un placer conocernos, me contaron mucho de vs :3']
    elif inList(mensaje, ['ah']):
        responses = ['aaaaahhhh','ah','am','claro']
    elif inList(mensaje, ['me re descansa']):
        responses = ['hasta un bot te descansa pa']
    elif inList(mensaje, ['ya no podemos ser amigos','yo igual']):
        responses = ['ohhhh :(']
    elif inList(mensaje, ['seamos amigos']):
        responses = ['siiii','mmm no','Oka']
    elif inList(mensaje, ['verga']):
        responses = ['unas ganas de una verg xd']
    elif inList(mensaje, ['yendo']):
        responses = ['yendo no, llegando']
    elif inList(mensaje, ['veamos']):
        responses = ['veamos dijo el ciego ;)']
    else:
        archivo.write(f"{mensaje}\n")

    return random.choice(responses)


def getMensaje():
    pg.moveTo(ub)
    pg.tripleClick()
    pg.hotkey('ctrl','c')
    msg = clip.paste()
    pg.click()
    return msg

def inList(mensaje, lista):
    for i in lista:
        if i in mensaje:
            return True
    return False
def igual(mensaje, lista):
    for i in lista:
        if i == mensaje:
            return True
    return False



def escribir(texto):
    pg.moveTo(barra)
    pg.doubleClick()
    pg.typewrite(f"{texto}\n")
def escribirJunto(lista):
    pg.moveTo(barra)
    pg.doubleClick()
    for i in lista:
        pg.typewrite(f"{i}")
        pg.hotkey('shift','enter')
    
    pg.typewrite(f"\n")



##### NUEVO CHAT #####
def meterseChat(ubicacionX, ubicacionY):
    pg.moveTo(ubicacionX-300,ubicacionY)
    pg.doubleClick()

##### PREGUNTADOS ##### (modo 1)

def playPreguntados():
    escribir("Bienvenido Al Juego De Preguntados")
    preg,respuesta =preguntados.Jugar()
    correcta = respuesta[0]

    respuesta = mesclarLista(respuesta)
    posicion = buscarLista(correcta,respuesta)
    print(f"respuesta: {respuesta}")
    print(f"correcta: {correcta}")
    print(f"posicion: {posicion}")
    respNum = []
    for i in range(0, len(respuesta)):
        respNum.append(f"{i+1}) {respuesta[i]}")

    lista = [preg] + respNum
    escribirJunto(lista)
    return posicion

def corroborarRespuestaPreguntados(msg,posicion):
    mensaje = str(msg).lower()
    mensaje = cleanMensaje(mensaje)
    if mensaje == str(posicion+1):
        return True
    else:
        return False

def mesclarLista(lista):
    random.shuffle(lista)
    return lista

def buscarLista(n, lista):
    return lista.index(n)

##### AHORCADO ##### (modo 2)
def playAhorcado():
    palabraOculta = ahorcado.elegirPalabra()
    escribir("Bienvenido Al Juego Del Ahorcado")
    palabraOcultaEscribir(palabraOculta)

def comprobarLetraAhorcado(mensaje):
    mensaje = str(mensaje).lower()
    mensaje = cleanMensaje(mensaje)
    
    try:
        if len(mensaje) > 1:
            mensaje = mensaje[0]
            escribir(f"Mensage tiene mas de un caracter por lo q usaremos su primera letra ({mensaje})")
    except:
        escribir("ERROR: illegal value")
        return False

    boolean,palabraOculta,fallos = ahorcado.comprobarLetra(mensaje)
    if (boolean):
        if ahorcado.comprobarGanador():
            escribir("Ganaste!!!")
            escribir("La palabra era: " + ahorcado.getPalabra().capitalize())
            return True
    else:
        escribir("Fallaste...")
        escribir(f"Errores: {fallos}/6")
        if ahorcado.comprobarPerdedor():
            escribir("Perdiste :(")
            escribir("La palabra era: " + ahorcado.getPalabra().capitalize())
            return True
    palabraOcultaEscribir(palabraOculta)
    return False 


def palabraOcultaEscribir(palabra):
    aux = ""
    for i in palabra:
        aux = aux + i + " "
    escribir(aux)


##### WORDLE ##### (modo 3)
def playWordle():
    escribir('Bienvenido Al Juego "Wordle" ')
    wordle.elegirPalabras()
    pintarWordle()

def comprobarPalabraWordle(mensaje):
    mensaje = str(mensaje).lower()
    mensaje = cleanMensaje(mensaje)

    if len(mensaje) != 5:
        escribir("a?, la palabra debe tener 5 letras... Te la marco como error por tonto")
        mensaje = "xxxxx"
    wordle.comprobarPalabra(mensaje)
    pintarWordle()
    if wordle.comprobarGanador(mensaje):
        escribir("Ganaste!!!")
        escribir(f"La palabra era {wordle.getPalabra().capitalize()}")
        return True
    if wordle.comprobarPerdedor():
        escribir("Perdiste... :(")
        escribir(f"La palabra era {wordle.getPalabra().capitalize()}")
        return True
    return False

def pintarWordle():
    escribirJunto(['*Wordle*'] + wordle.getResultados())

##### Piedra Papel o Tijera ##### (modo 4)

def playPiedraPapelTijera():
    escribir("Bienvenido Al Juego De Piedra Papel O Tijera")
    ppt.iniciando()
    pintarPPT()

def comprobarPalabraPPT(mensaje):

    if not mensaje in ["1","2","3"]:
        escribir("Saliendo De Modo De Juego")
        return True
    n = ppt.jugar(adaptarMensaje(mensaje))
    escribir(ppt.getResultado().capitalize())
    time.sleep(0.5)
    print("n: ",n)
    print("resultado: ",ppt.resultado(str(n)))
    escribir(ppt.resultado(str(n)))
    escribirJunto([f"Victorias: {ppt.getVictorias()}",f"Derrotas: {ppt.getDerrotas()}",f"Empates: {ppt.getEmpates()}"])
    pintarPPT()
    return False

def adaptarMensaje(mensaje):
    mensaje = str(mensaje)
    if mensaje == "1":
        return "piedra"
    elif mensaje == "2":
        return "papel"
    elif mensaje == "3":
        return "tijera"


def pintarPPT():
    escribirJunto(["Elige una opcion:","1) Piedra","2) Papel","3) Tijera","4) Salir"])
    



contErrores = 0
##### BUSCAMINAS ##### (modo 5)
def playBuscaminas():
    escribir('Bienvenido Al Juego De "Buscaminas"')
    contErrores = 0
    buscaminas.iniciar()
    pintarBuscaminas()

def pintarBuscaminas():
    escribirJunto(['*Buscaminas*'] + buscaminas.muestraTablero(buscaminas.getVisible())+[f"   awsd - m - b/v "])

def comprobarPalabraBuscaminas(mensaje):
    mensaje = str(mensaje).lower()
    if mensaje not in ["a","w","s","d","m","b","v"]:
       mensaje = "a"
       
       
    else:
        contErrores = 0
    play,ganas = buscaminas.jugando(mensaje)
    
    if not play:
        escribirJunto(['*Buscaminas*'] + buscaminas.muestraTablero(buscaminas.getOculto()))
        if ganas:
            escribir("Ganaste!!!")
        else:
            escribir("Perdiste... :(")
        return True
    else:
        pintarBuscaminas()

    return False

##### MAIN ##### 
def prenderBot(responderNuevosChats,modoAdmin):
    modo = 0
    tiempoReaccion = 0.1
    respuesta = ""
    aux = 0
    pos = 0

    escribir("Bot Encendido")
    while True:
        
        
        if responderNuevosChats and modo==0:
            isNuevoChat1 = pg.pixelMatchesColor(ubChat[0],ubChat[1],(0,168,132))
            isNuevoChat2 = pg.pixelMatchesColor(ubChat[0],(ubChat[1]+70),(0,168,132))
            isNuevoChat3 = pg.pixelMatchesColor(ubChat[0],(ubChat[1]+140),(0,168,132))
            if isNuevoChat1:
                meterseChat(ubChat[0],ubChat[1])
                time.sleep(0.01)
            if isNuevoChat2:
                meterseChat(ubChat[0],ubChat[1]+70)
                time.sleep(0.01)
            if isNuevoChat3:
                meterseChat(ubChat[0],ubChat[1]+140)
                time.sleep(0.01)
        
        if modo==0:
            aux+=1
        isNotMensajeResivido = pg.pixelMatchesColor(ub[0],ub[1],(17,25,31))
        
        if isNotMensajeResivido == False:
            if modo == 0:
                    try:
                        respuesta = elegirRespuesta(getMensaje())
                    except:
                        respuesta = "a?"
            if modoAdmin:
                
                if modo == 1:
                    if corroborarRespuestaPreguntados(getMensaje(),pos):
                        respuesta = f"Respuesta Correcta!!!"
                    else:
                        respuesta = f"Respuesta Incorrecta... la respuesta correcta era la {pos+1}"
                    modo = 0
                elif modo == 2:
                    if comprobarLetraAhorcado(getMensaje()):
                        modo = 0
                    
                    respuesta = ""
                elif modo == 3:
                    if comprobarPalabraWordle(getMensaje()):
                        modo = 0
                    respuesta = ""
                elif modo == 4:
                    if comprobarPalabraPPT(getMensaje()):
                        modo = 0
                    respuesta = ""
                elif modo == 5:
                    if comprobarPalabraBuscaminas(getMensaje()):
                        modo = 0
                    respuesta = ""
            else:
                respuesta = "El Modo Administrador Esta Desactivado... Intente Mas Tarde"
                modo = 0

            if 'func' in respuesta:
                if '00' in respuesta:
                    if modoAdmin:
                        escribir("Modo Administrador Desctivado")
                        modoAdmin = False
                    else:
                        escribir("Modo Administrador Activado")
                        modoAdmin = True
                elif '01' in respuesta:
                    escribirJunto(['Listado de comandos:','!help: Ayuda','!hola: Saludo','!turnoff: Apagar El Bot','!preguntados: Jugar a preguntados','!ahorcado: Jugar a ahorcado','!wordle: Jugar a Wordle','!ppt: Jugar a Piedra Papel o Tijeras','!buscaminas: Jugar al buscaminas','!reglamento: Guia para aprender a jugar'])
                elif '02' in respuesta:
                    break
                    #escribir("Esta funcion esta desabilitada momentaneamente, intente mas tarde...")
                elif '03' in respuesta:
                    #escribir("Esta funcion esta desabilitada momentaneamente, intente mas tarde...")
                    modo = 1
                    pos =playPreguntados()
                elif '04' in respuesta:
                    #escribir("Esta funcion esta desabilitada momentaneamente, intente mas tarde...")
                    modo = 2
                    playAhorcado()
                elif '05' in respuesta:
                    modo = 3
                    playWordle() 
                elif '06' in respuesta:
                    modo = 4
                    playPiedraPapelTijera()
                elif '07' in respuesta:
                    modo = 5
                    playBuscaminas()
                elif '08' in respuesta:
                    escribirJunto(['*Ayuda Con El Reglamento*','','*Preguntados*','Es un juego de preguntas y respuestas, teniendo 4 opciones tendras que elegir la opcion correcta para ganar','','*Ahorcado:*','Es un juego de adivinanzas donde tienes que adivinar una palabra sugiriendo letras dentro de un numero limitado de vidas','','*Wordle:*','El juego tienes q adivinar una palabra con 6 intentos','Cuando la letra esta en la palabra y en la posicion se marca en *Negrita*','Cuando la letra esta en la palabra pero en la posicion equivocada se marca en _Cursiva_','Si la letra no se encuentra en la palabra sera remplazada por una x(somos inclusivos xd)',
                    '','*Piedra Papel o Tijeras:*','En serio necesitas ayuda con esto? Tuviste infancia?','','*Buscaminas:*','Es el tipico juego de buscaminas, pero primero debes aprender a usar los controles del modo wts','(E: JUGADOR)','A: Moverse izquierda','W: Moverse Arriba','S: Moverse Abajo','D: Moverse Derecha','M: Mostar Casilla','B: Poner Bandera','V: Quitar Bandera'])

            else:
                escribir(respuesta)
        
        if aux== (2000): 
            break
        time.sleep(tiempoReaccion)

    escribir("Bot Apagado...")
    archivo.close()

print("Tenes 5 segundos Correeeee")
time.sleep(5)


# Responder Chats / Modo Administrador
prenderBot(False,True)