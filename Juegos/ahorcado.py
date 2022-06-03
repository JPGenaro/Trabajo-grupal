import random

class Ahorcado:
    def __init__(self):
        self.palabras = ['casa','perro','gato','coche','planta','ahorcado','mujer','hombre','pepino','constantinopla','viena','metropoli','dinosaurio','hipopotamo','rinoceronte','aguatero', 'sustantivo','adjetivo','homosapiens','hipopotomonstrosesquipedaliofobia','australopitecus','saturno','ornitorrinco','alcalde','cortina','netherite','asfalto','cuaderno','electricidad','bot','escuela','ejercito','avenida','barrio','guante','cabello','camino','camara','cigarro','mantel','manguera','silencio','capsula','lampara','pistola','pintura','pavimento','ocasion','comida','esternocleidomastoideo','otorrinolaringologo','desoxirribonucleico','paralelepipedo','supercalifragilisticoespialidoso','locura','neurona','pneumonoultramicroscopicsilicovolcanoconiosis','acuatico','acustica','guitarra','tambor', 'ultimo','primer','presencia','consonante','disonante','tension','reposo','repollo','aliviar','ciudad','edificio','silla','mesa','dormir','respiracion','iluminacion','plano','curvatura','tiempo','espacio','pelota','escalera','ventana','puerta','piso','pared','persona','humano','tortuga','venus','marte','urano','mercurio','sol','luna','neptuno','pluton','jupiter','hidrogeno','boca','nariz','brazo','pierna','pie','talon','mano']
        self.palabra = ""
        self.palabraOculta = ""
        self.letras = []
        self.fallos = 0
    
    def elegirPalabra(self):
        self.palabra = random.choice(self.palabras)
        self.palabraOculta = len(self.palabra) * "-"
        self.fallos = 0
        return self.palabraOculta

    def comprobarLetra(self,letra):
        boolean = False
        if letra in self.palabra:
            for i in range(len(self.palabra)):
                if self.palabra[i] == letra:
                    self.palabraOculta = self.palabraOculta[:i] + letra + self.palabraOculta[i+1:]
                    boolean = True
        else:
            self.fallos += 1
            print("La letra no se encuentra en la palabra :(")
        
        print(self.palabra)
        print(self.palabraOculta)
        return boolean, self.palabraOculta, self.fallos
    
    def comprobarGanador(self):
        if self.palabra == self.palabraOculta:
            return True
        else:
            return False
    
    def comprobarPerdedor(self):
        if self.fallos == 6:
            return True
        else:
            return False
    def getPalabra(self):
        return self.palabra