import pygame 

def dibujar(enigma, path, pantalla, ancho, altura, margenes, gap, fuente):

	w = (ancho - margenes["left"] - margenes["right"] - 5 * gap) / 6
	h = altura - margenes["top"] - margenes["bottom"]


	# dibujar path
	y = [margenes["top"] + (señal + 1) * h / 27 for señal in path]
	x = [(ancho - margenes["right"] - w / 2)]

	for i in [4,3,2,1,0]:
		x.append(margenes["left"] + i * (w + gap) + w * 3/4)
		x.append(margenes["left"] + i * (w + gap) + w * 1/4)


	for i in [1,2,3,4]:
		x.append(margenes["left"] + i * (w + gap- 10) + w * 1/4)
		x.append(margenes["left"] + i * (w + gap - 10) + w * 3/4)
	x.append(ancho-margenes["right"] - w/2)

	if len(path) > 0:
		for i in range(1,20):
			color = "#43aa8b" if i < 10 else "#e63946"
			start = (x[i-1], y[i-1])
			end = (x[i], y[i])
			pygame.draw.line(pantalla, color, start, end, width = 5)

	y = margenes["top"]

	enigma.teclado.dibujar(pantalla, 1200, y, 150, 480, fuente)
	enigma.plugBoard.dibujar(pantalla, 950, y, 180, 480, fuente)
	enigma.r3.dibujar(pantalla, 750, 180, y, 480, fuente)
	enigma.r2.dibujar(pantalla, 550, 180, y, 480, fuente)
	enigma.r1.dibujar(pantalla, 350, 180, y, 480, fuente)
	enigma.reflector.dibujar(pantalla, 150, y, 180, 480, fuente)
