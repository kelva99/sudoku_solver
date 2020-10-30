from .solver import Sudoku_Solver 

class Sudoku_Solver_1(Sudoku_Solver):
	def __init__(self):
		super(Sudoku_Solver_1, self).__init__()
		self._log = False

	def start_posn_of_box(self, x):
		return (x // 3) * 3 

	def is_okay(self, code, row, col, candidate):
		# check row and column
		for i in range(9):
			self.log("row: {0}, col: {1}, i:{2}, candidate {3}".format(row, col, i, candidate))
			if str(candidate) in [code[row * 9 + i], code[i * 9 + col]]:
				self.log("existed in row/col")
				return False

		# check 3*3 square
		row_start = self.start_posn_of_box(row)
		col_start = self.start_posn_of_box(col)

		for r in range(row_start, row_start + 3):
			if r == row:
				# we have checked the row
				continue
			for c in range(col_start, col_start + 3):
				if c == col: 
					# we have checked the column
					continue  
				self.log("row: {0}, col: {1}, r:{2}, c:{3}, candidate {4}".format(row, col, r, c, candidate))
				if str(candidate) == code[r * 9 + c]:
					self.log("existed in box")
					return False

		return True

	def find_all(self, code, row, col):
		for i in range(1, 10):
			if self.is_okay(code, row, col, i):
				posn = row * 9 + col
				code = code[:posn] + str(i) + code[posn + 1:]
				next_posn = code.find('0')
				if (next_posn == -1):
					self._result.append(code)
					return
				new_row = next_posn // 9
				new_col = next_posn % 9
				self.find_all(code, new_row, new_col)


	def solve(self, code, silent = False):
		next_posn = code.find('0')
		if (next_posn == -1):
			print("The puzzle is complete")
			return
		row = next_posn // 9
		col = next_posn % 9
		
		self.find_all(code, row, col)
		for r in self._result:
			self.pretty_print(r, silent) + "\n"
		return self._result
