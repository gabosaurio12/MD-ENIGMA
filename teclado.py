class Teclado:

	def forward(self, letra):
		señal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letra)
		return señal

	def backward(self, señal):
		letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[señal]
		return letra
