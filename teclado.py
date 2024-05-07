class Teclado:

	def forward(propio, letra):
		signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letra)
		return signal

	def backward(propio, signal):
		letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
		return letra
