import random

class Preguntados:
    def __init__(self):
        self.preguntas = ['¿Cuantas zonas horarias tiene en Rusia?',
        '¿Cual es el animal nacional de Australia?',
        'En un Anio viciesto, ¿Cuantos dias le toma a la tierra dar una vuelta a la orbita del sol?',
        '¿Cual de los siguientes imperios no tenia un idioma escrito?',
        '¿Como se llamaba Istanbul antes de 1923?',
        '¿Que pais tiene la mayor cantidad de islas en el mundo? (Mas de 220.000!!!)',
        '¿Cual es el pais mas pequenio del mundo?',
        '¿Cual es la capital de Canada?',
        'Cual es la cordillera mas larga (no mas alta) del mundo?',
        '¿Cual es la fosa mas profunda del mundo?',
        '¿Cual es el rio mas largo del mundo?',
        '¿Cual es la serie de libros mejor vendida del siglo 21?',
        '¿Cual es el idioma que tiene mas palabras (segun su diccionario)?',
        '¿Cual es la obra mas famosa de Edvard Munch?',
        '¿Que artista pinto el techo de la Capilla Sixtina en Roma?',
        '¿Cuando se inauguro el metro de Londres?',
        '¿Cual fue el primer pais de America en lograr su independencia?',
        '¿De donde es Billie Eilish?',
        '¿De que ciudad son originarios los Beatles?',
        '¿Cual es la cancion mas reproducida en Spotify hasta el momento?',
        '¿Cuantas teclas tiene un piano?',
        '¿Que banda americana se llamaba originalmente, “Kara’s Flowers”?',
        '¿Que equipo de futbol se le conoce como ‘The Red Devils’?',
        '¿Que conductor de la Formula 1 ha ganado mas campeonatos?',
        '¿Originalmente como se llamaba la marca Nike?',
        '¿Cuando se fundo Netflix?',
        '¿Cual fue la serie mas vista en Netflix en el 2019?',
        '¿Como se llama la iconica cafeteria de Friends?',
        '¿Cual fue la primer pelicula de Disney?',
        '¿Cual es la primera pelicula de la saga de “El Hobbit”?',
        '¿Cual es la capital de Austria?',
        '¿De que pais se independizo Eslovenia?',
        '¿Que pais africano fue fundado por esclavos americanos liberados en 1847?'
        '¿Cual es el pais mas grande del mundo?',
        '¿cual fue el primer imperio que existio en el mundo?',
        ]
        self.respuestas = [
        ['11','12','9','10'],
        ['El Canguro','El Koala','El Wombat','El Cocodrilo Poroso'],
        ['366','365','364','367'],
        ['Inca','Aztecas','Griego','Egipcio'],
        ['Constantinopla','Benjin','Marchisal','Aragon'],
        ['Suecia','Japon','Indonesia','Nueva Zelanda'],
        ['El Vaticano','Monaco','San Marino','Andorra'],
        ['Ottawa','Vancouver','Toronto','Montreal'],
        ['Los Andes','Cordillera de Alaska ','Los Alpes','Sierra Madre'],
        ['Fosa De Las Marinas','Fosa de Kermadec','Fosa de las Kuriles','Fosa de Filipinas'],
        ['Amazonas ','Nilo','Yangtsé','Misisipi'],
        ['Harry Potter','El Senior De Los Anillos','El Principito','Crepusculo'],
        ['Ingles','Espaniol','Chino','Portugues'],
        ['El Grito','La Gioconda (La Mona Lisa)','La Noche Estrellada','El Nacimiento De Venus'],
        ['Miguel Angel','Diego Velazquez','Leonardo Da Vinci','Pablo Picasso'],
        ['1863','1845','1893','1874'],
        ['Haiti','Estados Unidos','Mexico','Colombia'],
        ['Los Angeles','New York','Misisipi','Miami'],
        ['Liverpool','Manchester','Nevada','Seattle'],
        ['The Shape of You','Believer','Despacito','Marolio'],
        ['88','92','96','102'],
        ['Maroon 5','The Rolling Stones','The Beatles','ACBC'],
        ['Manchester United','Madrid','Sevilla','Valencia'],
        ['Michael Schumacher','Jackie Stewart','Ayrton Senna','Didier Pironi'],
        ['Blue Ribbon Sports','Tnks','Strakers','Nykaas'],
        ['1997','2001','2009','2005'],
        ['Stranger Things','The Office','The Walking Dead','The Simpsons'],
        ['Central Perk','Little Collins','Frisson Espresso','Brooklyn Roasting Company'],
        ['Blanca Nieves','Cenicienta','Babylon','Dumbo'],
        ['Un Viaje Inesperado','La Desolacion De Smaug','La Batalla De Los Cinco Ejercitos','La Comunidad Del Anillo'],
        ['Viena','Varsovia','Berlin','Budapest'],
        ['Yugoslavia','Del Imperio Austriaco','Croacia','Italia'],
        ['Liberia','Ghana','Sokoto','Benin'],
        ['Rusia', 'Australia', 'China', 'India'],
        ['Acadio', 'Egipto', 'Grecia', 'Persia']
        ]

    #Funcion que devuelve una pregunta aleatoria
    def Jugar(self):
        n = random.randint(0, len(self.preguntas)-1)
        print(n)
        return self.preguntas[n], self.respuestas[n]

    #Pytest :D
    def Contar(self):
        print(len(self.preguntas))
        print(len(self.respuestas))