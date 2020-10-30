"""
Parse sudoku table from https://www.sudokuweb.org/
"""
import re, sys, argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Parse sudoku file downloaded online to match program')
	parser.add_argument('filename', nargs='*',help='filenames in test')
	args = parser.parse_args()

	for file in args.filename:
		f = None
		file += ".txt"
		try:
			f =  open("../test/"+file,'r')
		except Exception as e:
			print("File {0}: {1}".format(file,str(e)))
			continue
		output = f.read()
		f.close()
		output = ''.join(c for c in output if c.isprintable())
		output = re.sub('\s', '0', output)

		if (len(output) != 9*9):
			print("Length:" + str(len(output)))
			print(output)
			sys.exit(1)

		f = open("../test/"+file,'w')
		f.write(output)
		f.close()
	