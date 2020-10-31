import argparse, sys

lst_test = list(map(str, list(range(1, 10))))

def compare(s):
	# returns the invalid position
	data = list(s)
	data.sort()
	if data != lst_test:
		if data[0] == '0':
			return '0'
		for i in range(1, 8):
			if data[i] == data[i + 1]:
				return data[i]
	return ""

def check_all_idx(s, value):
	idx = []
	for i in range(9):
		if s[i] == value:
			idx.append(i)
	return idx

def validate(filename):
	with open("../test/" + args.filename + ".txt") as f:
		vinput = None
		try:
			vinput = f.read()
		except Exception as e:
			print("Error reading " + args.filename)
			f.close()
			raise Exception(e)

		f.close()

		err_posn = []
		for i in range(9):
			#ith row
			s = vinput[i*9:(i+1)*9]
			result = compare(s)
			if result != "":
				err_posn = check_all_idx(s, result)
				err_posn = list(map(lambda x: (i, x),err_posn))
				print(s, result, err_posn)
				return err_posn
			
			#ith column
			s = vinput[i::9] 
			result = compare(s)
			if result != "":
				err_posn = check_all_idx(s, result)
				err_posn = list(map(lambda x: (x, i), err_posn))
				print(s, result, err_posn)
				return err_posn

			# check box
			whichrow = i//3 * 3
			whichcol = i % 3 * 3
			s = vinput[whichrow * 9:whichrow * 9 + 9*3]
			s = s[whichcol:whichcol + 3] + \
				s[9 + whichcol:12 + whichcol] + \
				s[18 + whichcol:21 + whichcol]
			result = compare(s)

			# check box
			if result != "":
				def to_row_col(idx):
					row = idx // 3 + whichrow
					col = idx % 3 + whichcol
					return (row, col)
				err_posn = check_all_idx(s, result)
				err_posn = list(map(to_row_col, err_posn))
				print(s, result, err_posn)
				return err_posn
	return []




