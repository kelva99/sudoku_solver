# reference Creating a Sudoku Puzzle in https://www.sudokuwiki.org/Sudoku_Creation_and_Grading.pdf
import random
from validate import validate
from Solver import Sudoku_Solver, Sudoku_Solver_1

class Level(object):
	EASY = 0		# 35-40
	MIDDLE = 1		# 30-36
	HARD = 2 		# 25-33 
	EXPERT = 3 		# 20-28

class Generator(object):

	def __init__(self):
		self.lst_test = list(list(range(1, 10)))
		self.len_lst = len(self.lst_test)

		# data of popping numbers from complete board
		self.NUM_TO_POP = [(41, 46),(45,51),(48,56),(53,61)] 

		self.MAX_NUM_PER_LINE = [6, 5, 4, 3]



	def index_of_not_filled(self, lst):
		out = []
		for i in range(self.len_lst):
			if lst[i] == 0: out.append(i)
		return out

	def check_row_col(self, g, row, col, candidate):
		for i in range(self.len_lst):
			if g[row][i] == candidate or g[i][col] == candidate:
				return False
		return True

	def check_box(self, g, row, col, candidate):
		row_start = row // 3 * 3
		col_start = col // 3 * 3
		for r in range(row_start, row_start + 3):
			for c in range(col_start, col_start + 3):
				if g[r][c] == candidate:
					return False
		return True

	def pretty_print_wrap(self, g, pretty_print=True):
		out = ""
		for r in g:
			out += ''.join(list(map(str, r)))
		if pretty_print:
			Sudoku_Solver.pretty_print(out)
		return out



	def remove_node(self, g):
		mini, maxi = self.NUM_TO_POP[self.level]
		iteration = random.randint(mini, maxi)
		print(iteration)

		def count(r, c):
			counter = 0
			for i in range(9):
				if g[r*9 + i] != '0':
					counter += 1
				if g[i*9 + c] != '0':
					counter += 1
			return counter

		lst_all_pos = list(range(81))

		for i in range(iteration):
			whichbox = i%9
			num = -1
			if (i//9)* 9 + 9 >= iteration:
				# make last few bits random
				num = random.sample(lst_all_pos, 1)[0]

			else:
				min_pair = []
				min_sum = -1
				r0 = whichbox // 3 * 3
				c0 =  whichbox % 3 * 3
				for r in range(r0, r0 + 3):
					for c in range(c0, c0 + 3):
						if g[r*9+c]=='0':
							continue
						res = count(r, c)
						if (res < min_sum):
							continue
						elif res == min_sum:
							min_pair.append((r, c))
						else: # res < min_sum
							min_pair = [(r, c)]
							min_sum = res

				r, c = random.sample(min_pair, 1)[0]
				num = r*9 + c

			g = g[:num] + "0" + g[num+1:]
			lst_all_pos.remove(num)

		self.pretty_print_wrap(g)

		




	# generate full valid board
	def generate(self, level, outfile=None):
		out = []
		self.level = level

		# ten tries
		for attempt in range(10):
			g = []
			# init grid
			for i in range(self.len_lst):
				g.append([])
				for j in range(self.len_lst):
					g[i].append(0)

			fail = False
			for r in range(3):
				num_rand = random.sample(self.lst_test, self.len_lst)
				for c in range(self.len_lst):
					for num in num_rand:
						if self.check_row_col(g, r, c, num) and self.check_box(g, r, c, num):
							g[r][c] = num
							num_rand.remove(num)
							break
				if 0 in g[r]:
					fail = True
					break
			if not fail:
				out = g
				break

		if out == []:
			print("Cannot generate base board")
			return []

		for c in range(3):
			rand_order = random.sample(list(range(3)), 2)
			rand_dest = random.sample(list(range(1, 3)), 2)
			for r in range(2):
				which_col = rand_order[r] + 3 * c
				dest_row = rand_dest[r] * 3
				out[dest_row][which_col] = out[0][which_col]
				out[dest_row + 1][which_col] = out[1][which_col]
				out[dest_row + 2][which_col] = out[2][which_col]
				out[0][which_col] = 0
				out[1][which_col] = 0
				out[2][which_col] = 0

		str_incomplete_board = self.pretty_print_wrap(out, pretty_print=False)
		lst_baords = Sudoku_Solver_1().solve(str_incomplete_board, silent=True)
		is_good_result = False

		# randomly pop one
		candidate_idx = random.randint(0, len(lst_baords) - 1)
		candidate = lst_baords.pop(candidate_idx)

		while (not is_good_result) and lst_baords != []:
			invalid_board, err_posn = validate(lst_inputboard=lst_baords)
			if invalid_board == "" and err_posn == []:
				is_good_result = True
				break
			candidate_idx = random.randint(0, len(lst_baords))
			candidate = lst_baords.pop(candidate_idx)

		if not is_good_result:
			print("Failed to fill the board")
			return []

		# a valid board is obtained by now
		# self.pretty_print_wrap(candidate)
		board_to_play = self.remove_node(candidate)
		if outfile != None:
			f = open("../test/"+outfile + "_soln.txt",'w')
			f.write(candidate)
			f.close()

			f = open("../test/"+outfile + ".txt",'w')
			f.write(board_to_play)
			f.close()

		return board_to_play


if __name__ == '__main__':
	g = Generator()
	grid = g.generate(Level.EXPERT)



