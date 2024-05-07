class Enigma:
	def _init_(self, reflector, r1, r2, r3, plugBoard, teclado)
		self.re = re
		self.r1 = r1
		self.r2 = r2
		self.r3 = r3
		self.plugBoard = plugBoard
		self.teclado = teclado

	def confAnillo(self, anillo):
		self.r1.confAnillo(anillos[0])
		self.r2.confAnillo(anillos[1])
		self.r3.confAnillo(anillos[2])

	def colocarLlave(self, llave):
		self.r1.rotarALetra(llave[0])
		self.r2.rotarALetra(llave[1])
		self.r3.rotarALetra(llave[2])

	def cifrar(self, letra):
		if r2.izq[0] == r2.notch and r3.left[0] == r3.notch:
			self.r1.rotar()
			self.r2.rotar()
			self.r3.rotar()

		elif self.r2.izq[0] == self.r2notch:
			self.r2.rotar()
			self.r3.rotar()

		elif self.r3.izq[0] == self.r3.notch:
			self.r2.rotar()
			self.r3.rotar()
		else:
			self.r3.rotar()

		señal = self.teclado.adelante(letra)
		señal = self.plugBoard.adelante(señal)
		señal = self.r3.adelante(señal)
		señal = self.r2.adelante(señal)
		señal = self.r1.adelante(señal)
		señal = self.reflector.reflectar(señal)
		señal = self.r1.atras(señal)
		señal = self.r2.atras(señal)
		señal = self.r3.atras(señal)
		señal = self.plugBoard.atras(señal)
		señal = self.teclado.atras(letra)
		return letra