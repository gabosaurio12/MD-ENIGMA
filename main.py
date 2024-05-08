from teclado import Teclado
from enchufe import Enchufe
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

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
enchufe = Enchufe(["MI", "LA", "DO"])

# Definir Enigma (Elegir el orden de los rotores -Rotors-)

ENIGMA = Enigma(B, I, V, III, enchufe, teclado)

# Colocar la llave del mensaje (Rotor Start)

ENIGMA.colocarLlave("PAR")

# Configurar Anillos (Rings)

ENIGMA.confAnillo((1, 2, 3))

# Cifrar mensaje

mensaje = "TEAMO" 
cifrarTexto = ""
for letra in mensaje:
	cifrarTexto = cifrarTexto + ENIGMA.cifrar(letra)

print(cifrarTexto)
