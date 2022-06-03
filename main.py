import pyautogui as pg
import time
import pyperclip as clip
import random
from math import trunc
archivo = open("../TrabajoGrupal/PalabrasAprender.txt","a")

user = str(input("Ingrese su usuario: Lichi-1, Mora-2, JuanCarlos-3 \n>> "))
if user == "1":
    #Usuario 1 (PC LICHI)
    barraWhats = 870, 684
    chatSelect = 290, 440
    chatSelect2 = 290, 520
    chat1 = 315, 247
    chat2 = 315, 317
    green = 0, 168,132
    ubMensaje = 533, 631
    msj_color = 32, 44, 51
    ubTextoMensaje = 539, 621
elif user == "2":
    #Usuario 2 (PC MORA)
    barraWhats = 700, 695
    chatSelect = 215, 360
    chatSelect2 = 215, 440
    chat1 = 315, 247
    chat2 = 315, 317
    green = 0, 168,132
    ubMensaje = 565, 626
    msj_color = 32, 44, 51
    ubTextoMensaje = 570,620
else:
    #Usuario 3 (PC GENARO)
    barraWhats = 581, 733
    chatSelect = 215, 230
    chatSelect2 = 215, 300
    chat1 = 315, 247
    chat2 = 315, 317
    green = 0, 168,132
    ubMensaje = 500, 679
    msj_color = 32, 44, 51
    ubTextoMensaje = 510,667

def getMensaje():
    pg.moveTo(ubTextoMensaje)
    pg.tripleClick()
    pg.hotkey('ctrl','c')
    msg = clip.paste()
    pg.click()
    msg = cleanMensaje(msg)
    return msg

def cleanMensaje(s):
    s = s.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ü", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def elegirRespuesta(mensaje):
    print(f"Mensaje recibido: {mensaje}")
    responses = ['Ehh, No entiendo...']
    if type(mensaje) == str:
        if mensaje[0] == "!":
            if mensaje == "!turnoff":
                return "func0"
            elif mensaje == "!help":
                return "func1"
            elif mensaje == "!info":
                return "func2"
            else:
                responses = ['ERROR: Comand Not Found']
    
        elif mensaje == 'ping':
            responses = ['pong']
        elif isEqual(mensaje, ['bueno','oka','si','tambien']):
            responses = ['si','si...','Okas','Oka']
        elif isEqual(mensaje, ['no','no se']):
            responses = ['mmm','si...','Hmm',':(']
        elif inList(mensaje, ['hola','holi','buenas tardes','buenos dias']) and inList(mensaje, ['q haces','que haces','q contas','q onda','que onda','que contas']):
            responses = ['Hola buenas tardes, Ando trabajando vs??', 'Hola, que tal, aca mirando una peli vs??', 'Holaa, nada vs??']
        elif inList(mensaje, ['hol','buenas tardes','buenos dias']) and inList(mensaje, ['como estas','como te encontras','como te fue']):
            responses = ['Hola buenas tardes, bien bien vos??', 'Holaa, bien bien vos??', 'Buenas, bien vos??']
        elif inList(mensaje, ['hola','holi','buenos dias','buenas tardes','buenas noches']) or mensaje == 'buenas':
            responses = ['Holaa', 'Hola, que tal?', 'Holaa, como estas?', 'Holaa, que haces?']
            print('Mando')
        elif inList(mensaje, ['como estas','como andas','como te encontras','todo bien','como te encontras']):
            responses = ['Muy bien, vs?', 'Muy bien, gracias por preguntar.', 'Todo piola vs??']
        elif inList(mensaje, ['q haces','que haces','nada vs','nada vos','q estas haciendo','que estas haciendo','q te contas','que te contas']):
            responses = ['Aca tranqui, Vs?','Estoy aca estoy']
        elif inList(mensaje, ['todo piola','bien']):
            responses = ['Mejor me alegro :)', 'Me alegro :D', 'Mejor :p']
        elif inList(mensaje, ['cuantos años tenes','cual es tu edad','cuando naciste']):
            responses = ['Recien Naci hace unas semanas', 'Hace un par de horas', 'Un Milenio']
        elif inList(mensaje, ['jajaj','jsjsj','jajsj']):
            responses = ['Jajajajaj', 'Jajsjsaj','jajsjaj','jajajajja dios lpm','jajajajajjaj','jajjsjsjaj']
        elif inList(mensaje, ['mira vos']):
            responses = ['Si mira vs che','Si es tremendo','Si :)']
        
        elif inList(mensaje, ['contas un chiste','decime un chiste','decis un chiste','conta un chiste','contame un chiste','contar un chiste','haces un chiste']) or mensaje == 'chiste':
            responses = ['habia una vez un pollito q respiraba por el culito, se sento y se murio','habia una vez truz',
            'Por q los koalas no son considerados osos?? \n Por q no cumplen con las koalaficaciones','Si vas a comprar una leche siempre compra 1 o 2, Por q la tercera es la vencida :D','Q pasa si tiras un pato al agua\n Nada.',
            'Por q a un ladron lo entierran a 200 metros bajo tierra, por q en el fondo es bueno :D','Donde deja superman su capa? En su perchero :D','Buenas tardes soy Rosa\n Ah, perdoname es q soy Daltonico','¿Como te llamas?\n Lancelot\n Pues Atrapalot','Papa Papa, q esta mas lejos desde casa Buenos Aires o la luna\n A ver hijo desde aca vs ves Buenos Aires o la Luna >:(',
            'Cual es el cafe mas peligroso??\n El ex-preso','Soldado, ice la bandera\n Fuaaa le quedo hermosa','',
            'Por q 20 y 22 en ingles son iguales\n Por q en ingles 20 es twenty y 22 es twenty too :D']    
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
        elif inList(mensaje,['como que no?']):
            responses = ['Como q no q']
        elif inList(mensaje,['mejor']):
            responses = ['Mejor']
        elif isEqual(mensaje,['a,e,i,o,u']):
            responses = ['a','e','i','o','u']
        elif inList(mensaje,['entendes?']):
            responses = ['Ci']
        elif inList(mensaje,['robot']):
            responses = ['bitbut bitbut']
        elif inList(mensaje,['hablame']):
            responses = ['Hola?']
        elif inList(mensaje,['de nada']):
            responses = [':D',':)','Que bien']
        elif inList(mensaje,['vos?']):
            responses = ['mmm no lo se']
        elif inList(mensaje,['mal']):
            responses = ['por?','Q paso?']
        elif inList(mensaje,['gracias']):
            responses = ['De nada','No hay problema','Un placer']
        elif inList(mensaje,['perdon']):
            responses = ['no pidas perdon :(']
        elif inList(mensaje,['sos un bot']):
            responses = ['Si, fui desarrollado por 3 personas en 2022 y fui creado para desayunar criollitos calentitos a la mañana :D']
        #Mensajes Iguales
        elif mensaje == 'ping':
            responses = ['pong']
        elif igual(mensaje, ['bueno','oka','si','tambien']):
            responses = ['si','si...','Okas','Oka']
        elif igual(mensaje, ['no','no se']):
            responses = ['mmm','si...','Hmm',':(']
        
        #Mensajes que contienen varias Opciones
        elif inList(mensaje, ['cuantos años tenes','cual es tu edad','cuando naciste']):
            responses = ['Recien Naci', 'Hace un par de horas', 'Un Milenio']
        elif inList(mensaje, ['jajaj','jsjsj','jajsj']):
            responses = ['Jajajajaj', 'Jajsjsaj', 'Q te reis gay','jajsjaj','jajajajja dios lpm','jajajajajjaj','jajjsjsjaj']
        elif inList(mensaje, ['mira vos']):
            responses = ['Si mira vs che','Si es tremendo','Si :)']
        #Insultos y respuestas 
        
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
    
            
    


def igual(mensaje, lista):
    for i in lista:
        if i == mensaje:
            return True
    return False

def escribir(texto):
    pg.moveTo(barraWhats)
    pg.typewrite(f"{texto}\n")
def escribirJunto(lista):
    pg.moveTo(barraWhats)
    pg.doubleClick()
    for i in lista:
        pg.typewrite(f"{i}")
        pg.hotkey('shift','enter')
    pg.typewrite(f"\n")
def inList(mensaje,lista):
    for i in lista:
        if i in mensaje:
            return True
    return False
def isEqual(mensaje,lista):
    for i in lista:
        if i == mensaje:
            return True
    return False
def main(responderChats,administrador):
    modo = 0
    cantMensajesRecibidos = 0
    cantTiempo = 0
    tiempoRespuesta = 0.1
    respuesta = ""
    escribir("Bot Iniciado")
    while True:
        isNuevoMensaje = pg.pixelMatchesColor(ubMensaje[0],ubMensaje[1],(msj_color[0],msj_color[1],msj_color[2]))
        if isNuevoMensaje:
            cantMensajesRecibidos += 1
            mensaje = getMensaje()
            response = elegirRespuesta(mensaje)
            if response == "func0":
                escribir("Bot Apagado...")
                break
            elif response == "func1":
                escribirJunto(["!turnoff: Apagar Bot","!help: Ayuda con comandos","!info: Ve informacion del Bot"])
            elif response == "func2":
                escribirJunto(["*Bot*",'Version: 0.4','_Autor: @Lisandro Marquez_','_Autor: @Juan Carlos Genaro_','_Autor: @Joaquin Morais_','GitHub: https://github.com/JPGenaro/TrabajoGrupal','Cantidad de mensajes recibidos: '+str(cantMensajesRecibidos),'Tiempo desde la iniciacion: '+str((trunc(100*cantTiempo))/100)+' segundos'])
            else:
                escribir(response)
        time.sleep(tiempoRespuesta)
        cantTiempo += tiempoRespuesta

print("Bienvenido al bot de wts")
print("Tienes 5 segundos para meterse al chat de Whatsapp deseado")
time.sleep(5)
main(False,False)