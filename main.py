import pygame

from teclado import Teclado
from enchufe import Enchufe
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from dibujar import dibujar

pygame.init()
pygame.font.init()
pygame.display.set_caption("Simulador Enigma")

#crear fonts
MONO = pygame.font.SysFont("American Typewriter", 20)
BOLD = pygame.font.SysFont("American Typewriter", 20, bold = True)


#variables globales
ANCHO = 1300
ALTURA = 700
PANTALLA = pygame.display.set_mode((ANCHO, ALTURA))
MARGENES = {"top":150, "bottom":50, "left":100, "right":100}
GAP = 100;

ENTRADA = ""
SALIDA = ""
PATH = []

# Componentes de enigma

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# Teclado y Enchufe (Plugboard)

teclado = Teclado()


# --- CONFIGURACIÓN DE ENIGMA --- #

# Escribir las letras a intercambiar
enchufe = Enchufe(["AB", "CD", "EF"])

# Elegir el orden de los rotores (I, II, III, IV)
ENIGMA = Enigma(B, I, III, II, enchufe, teclado)

# Colocar la llave del mensaje
ENIGMA.colocarLlave("ABC")

# Configurar Anillos
ENIGMA.confAnillo((1, 2, 3))

# --- FIN CONFIGURACIÓN DE ENIGMA --- #

animacion = True
while animacion:

	#fondo
	PANTALLA.fill("#26252d")

	# Entrada de texto

	texto = BOLD.render(ENTRADA, True, "white")
	caja_texto = texto.get_rect(center = (ANCHO/2, MARGENES["top"]/3))
	PANTALLA.blit(texto, caja_texto)

	# Salida de texto

	texto = MONO.render(SALIDA, True, "white")
	caja_texto = texto.get_rect(center = (ANCHO/2, MARGENES["top"]/3+25))
	PANTALLA.blit(texto, caja_texto)


	#dibujar la maquina enigma
	dibujar(ENIGMA, PATH, PANTALLA, ANCHO, ALTURA, MARGENES, GAP, MONO)


	#actualizarPantalla
	pygame.display.flip()

	#seguir entrada de usuario
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			animacion = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				II.rotar()

			elif event.key == pygame.K_SPACE:
				ENTRADA = ENTRADA + " "
				SALIDA = SALIDA + " "
 
			else:
				key = event.unicode
				if key in "abcdefghijklmnopqrstuvwxyz":
					letra = key.upper()
					ENTRADA = ENTRADA + letra
					PATH, cifrado = ENIGMA.cifrar(letra)
					SALIDA = SALIDA + cifrado
