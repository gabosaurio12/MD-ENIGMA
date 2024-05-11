import pygame

class Reflector:
	def __init__ (self, cableado):
		self.izq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.der = cableado

	def reflectar(self, señal):
		letra = self.der[señal]
		señal = self.izq.find(letra)
		return señal

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
