# parse output from https://qqwing.com/generate.html

import re, sys, argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Parse sudoku file downloaded online to match program')
	parser.add_argument('filename', nargs='*',help='filenames in test')
	args = parser.parse_args()

	for file in args.filename:
		file += ".txt"
		f = None
		try:
			f =  open("../test/"+file,'r')
		except Exception as e:
			print("File {0}: {1}".format(file,str(e)))
			continue
		output = f.read()
		f.close()
		removable = ['|', '-', ' ']
		output = ''.join(c for c in output if (c.isprintable() and not(c in removable)))
		output = re.sub('\.', '0', output)

		if (len(output) != 9*9):
			print("Length:" + str(len(output)))
			print(output)
			sys.exit(1)

		f = open("../test/"+file,'w')
		f.write(output)
		f.close()
	