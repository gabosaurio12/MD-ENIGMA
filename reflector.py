class Reflector:
	def __init__ (self, cableado):
		self.izq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.der = cableado

	def reflectar(self, señal):
		letra = self.der[señal]
		señal = self.izq.find(letra)
		return señal
