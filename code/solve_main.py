import Solver, argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='')
	parser.add_argument('filename',help='filename that contains the sudoku code (without extension)')
	# parser.add_argument('solver',help='which solver', choices=[1, 2], type=int)
	parser.add_argument('-s', '--silent',help='silent', action='store_true')
	args = parser.parse_args()
	result = None
	with open("../test/" + args.filename + ".txt") as f:
		out = None
		try:
			out = f.read()
		except Exception:
			print("Error reading " + args.filename)
			f.close()
			sys.exit(1)

		f.close()
		s = Solver.Sudoku_Solver_1()
		"""
		if (args.solver == 1):
			s = Solver.Sudoku_Solver_1()
		else:
			s = Solver.Sudoku_Solver_2()
		"""
		result = s.solve(out, args.silent)
	with open ("../test/" + args.filename + "_out.txt", 'w') as f:
		f.writelines('\n'.join(result))
		f.close()
