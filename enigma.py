class Enigma:
	def __init__(self, reflector, r1, r2, r3, plugBoard, teclado):
		self.reflector = reflector
		self.r1 = r1
		self.r2 = r2
		self.r3 = r3
		self.plugBoard = plugBoard
		self.teclado = teclado

	def confAnillo(self, anillos):
		self.r1.confAnillo(anillos[0])
		self.r2.confAnillo(anillos[1])
		self.r3.confAnillo(anillos[2])

	def colocarLlave(self, llave):
		self.r1.rotarALetra(llave[0])
		self.r2.rotarALetra(llave[1])
		self.r3.rotarALetra(llave[2])

	def cifrar(self, letra):
		# Rotar rotores

		if self.r2.izq[0] == self.r2.ranura and self.r3.izq[0] == self.r3.ranura:
			self.r1.rotar()
			self.r2.rotar()
			self.r3.rotar()

		elif self.r2.izq[0] == self.r2.ranura:
			self.r1.rotar()
			self.r2.rotar()
			self.r3.rotar()

		elif self.r3.izq[0] == self.r3.ranura:
			self.r2.rotar()
			self.r3.rotar()
		else:
			self.r3.rotar()

		# Pasa señal por la máquina

		señal = self.teclado.forward(letra)
		path = [señal, señal]
		path.append(señal)
		path.append(señal)
		señal = self.plugBoard.forward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.r3.forward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.r2.forward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.r1.forward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.reflector.reflectar(señal)
		path.append(señal)
		path.append(señal)
		path.append(señal)
		señal = self.r1.backward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.r2.backward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.r3.backward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.plugBoard.backward(señal)
		path.append(señal)
		path.append(señal)
		señal = self.teclado.backward(señal)

		return path, señal