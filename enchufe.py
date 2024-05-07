class Enchufe:
	def __init__(self, pares):
		self.izq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.der = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

		for par in pares:
			A = par[0]
			B = par[1]

			pos_A = self.izq.find(A)
			pos_B = self.izq.find(B)
			self.izq = self.izq[:pos_A] + B + self.izq[pos_A + 1:]
			self.izq = self.izq[:pos_B] + A + self.izq[pos_B + 1:]

	def forward(self, signal):
		letra = self.der[signal]
		signal = self.izq.find(letra)
		return signal

	def backward(self, signal):
		letra = self.izq[signal]
		signal = self.der.find(letra)
		return signal

