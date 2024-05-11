import pygame

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

	def dibujar(propio, pantalla, x,y,w,h,fuente):
         #rectángulo
		r = pygame.Rect(x,y,w,h)
		pygame.draw.rect(pantalla, "white", r, width = 2, border_radius =15)

		#letras
		for i in range(26):
			
			letra = propio.izq[i]
			letra = fuente.render(letra, True, "grey")
			caja_texto = letra.get_rect(center = (x+w/4, y+(i+1)*h/27))
			pantalla.blit(letra, caja_texto)

			letra = propio.der[i]
			letra = fuente.render(letra, True, "grey")
			caja_texto = letra.get_rect(center = (x+w*3/4, y+(i+1)*h/27))
			pantalla.blit(letra, caja_texto)

