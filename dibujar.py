import pygame 

def dibujar(enigma, path, pantalla, ancho, altura, margenes, gap, fuente):

	w = (ancho - margenes["left"] - margenes["right"] - 5 * gap) / 6
	h = altura - margenes["top"] - margenes["bottom"]


	# Coordenadas del path
	y = [margenes["top"] + (señal + 1) * h/27 for señal in path]
	x = [ancho - margenes["right"] - w/2] # Teclado

	for i in [4,3,2,1,0]: # Ida
		x.append(margenes["left"] + i * (w + gap) + w * 3/4)
		x.append(margenes["left"] + i * (w + gap) + w * 1/4)
	x.append(margenes["left"] + w * 3/4) #reflector

	for i in [1,2,3,4]: # Vuelta
		x.append(margenes["left"] + i * (w + gap) + w * 1/4)
		x.append(margenes["left"] + i * (w + gap) + w * 3/4)
	x.append(ancho - margenes["right"] - w/2) #lampara

	# Dibujar el path
	if len(path) > 0:
		for i in range(1,21):
			if i < 10:
				color = "#43aa8b"
			elif i < 12:
				color = "#f9c74f"
			else:
				color = "#e63946"

			start = (x[i-1], y[i-1])
			end = (x[i], y[i])
			pygame.draw.line(pantalla, color, start, end, width = 5)


	x = margenes["left"]
	y = margenes["top"]

	# Componentes de enigma

	enigma.reflector.dibujar(pantalla, x, y, w, h, fuente)
	x += w + gap
	enigma.r1.dibujar(pantalla, x, y, w, h, fuente)
	x += w + gap
	enigma.r2.dibujar(pantalla, x, y, w, h, fuente)
	x += w + gap
	enigma.r3.dibujar(pantalla, x, y, w, h, fuente)
	x += w + gap
	enigma.plugBoard.dibujar(pantalla, x, y, w, h, fuente)
	x += w + gap
	enigma.teclado.dibujar(pantalla, x, y, w, h, fuente)
	x += w + gap

	# Nombrar

	nombres = ["Reflector", "Izquierdo", "Central", "Derecho", "Enchufe", "Tec/Lamp"]
	y = margenes["top"] * 0.8
	
	for i in range(6):
		x = margenes["left"] + w/2 + i * (w + gap)
		titulo = fuente.render(nombres[i], True, "white")
		caja_texto = titulo.get_rect(center = (x, margenes["top"] * 3/4))
		pantalla.blit(titulo, caja_texto)