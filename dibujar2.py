import pygame

def dibujar(enigma, path, pantalla, ancho, altura, margenes, gap, fuente):

	# ancho y alto de los componentes
	w = (ancho - margenes["left"] - margenes["right"] - 5 * gap) / 6
	h = altura - margenes["top"] - margenes["bottom"]

	# dibujar path

	y = [margenes["top"] + (señal + 1) * h / 27 for señal in path]
	x = [(ancho - margenes["right"] - w / 2)]

	for i in [4,3,2,1,0]:
		x.append(margenes["left"] + i * (w + gap) + w * 3/4)
		x.append(margenes["left"] + i * (w + gap) + w * 1/4)
	x.append(margenes["left"] + w * 3/4) #reflector

	for i in [1,2,3,4]:
		x.append(margenes["left"] + i * (w + gap) + w * 1/4)
		x.append(margenes["left"] + i * (w + gap) + w * 3/4)
	x.append(ancho - margenes["right"] - w/2) #lampara

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

	# coordenadas base
	x = margenes["left"]
	y = margenes["top"]

	# Componentes de enigma

	for componente in [enigma.reflector, enigma.r1, enigma.r2, enigma.r3, enigma.plugBoard, enigma.teclado]:
		componente.dibujar(pantalla, x, y, w, h, fuente)

		x += w + gap

	# nombrar

	nombres = ["Reflector", "Izquierdo", "Central", "Derecho", "Enchufe", "Teclado/Lampara"]
	y = margenes["top"] * 0.8
	
	for i in range(6):
		x = margenes["left"] + w/2 + i * (w + gap)
		titulo = fuente.render(nombres[i], True, "white")
		caja_texto = titulo.get_rect(center = (x, margenes["top"] * 3/4))
		pantalla.blit(titulo, caja_texto)
