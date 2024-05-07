"""
Reflector: A
Rotores: I-II-III
Enchufe: A-R, G-K, O-X
Mensaje: A => X
"""

class Enchufe:
	def __init__(self, pairs):
		self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

		for pair in pairs:
			A = pair[0]
			B = pair[1]

			pos_A = self.left.find(A)
			pos_B = self.left.find(B)
			self.left = self.left[:pos_A] + B + self.left[:pos_A + 1:]
			self.left = self.left[:pos_B] + A + self.left[:pos_B + 1:]

p = Enchufe(["AF", "CR"])
print(p.left)
print(p.right)