class Rotor:
	def _init_(self, cableado, ranura):
		self.izq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.der = cableado
		self.ranura = ranura

	def adelante(self, señal):
		letra = self.der[señal]
		señal = self.izq.find(letra)
		return señal

	def atras(self, señal):
		letra = self.izq[señal]
		señal = self.der.find(letra)
		return señal

	def mostrar(self):
		print(self.izq)
		print(self.der)
		print("")

	def rotar(self, n = 1, adelante = True):
		for i in range(n):
			if adelante:
				self.izq = self.izq[1:] + self.izq[0]
				self.der = self.der[1:] + self.der[0]
			else:
				self.izq = self.izq[25] + self.izq[:25]
				self.der = self.der[25] + self.der[:25]

	def rotarALetra(self, letra):
		n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
		self.rotar(n)

	def confAnillo(self, n):
		self.rotar(n-1, adelante = False)

		n_ranura = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.ranura)
		self.ranura = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_ranura - n) % 26]

