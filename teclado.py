import pygame

class Teclado:

	def forward(propio, letra):
		signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letra)
		return signal

	def backward(propio, signal):
		letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
		return letra

	def dibujar(propio, pantalla, x,y,w,h,fuente):
         #rectángulo
		r = pygame.Rect(x,y,w,h)
		pygame.draw.rect(pantalla, "white", r, width = 2, border_radius =15)

		#letras
		for i in range(26):
			letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
			letra = fuente.render(letra, True, "grey")
			caja_texto = letra.get_rect(center = (x+w/2, y+(i+1)*h/27))
			pantalla.blit(letra, caja_texto)



