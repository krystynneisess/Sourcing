import csv

""" Reading a CSV file """
with open('Spring 2017 BOM.csv', 'rt', encoding = 'ISO-8859-1') as f:
	reader = csv.reader(f)
	col_types = next(reader)
	# find the first blank column
	finalCol = 0;
	for col in col_types:
		if col == "":
			break;
		finalCol += 1;
	print(col_types[:finalCol])
	print(drop)
	# for row in reader:
	# 	print(row)

""" Writing a NEW CSV file """
with open('test.csv', 'a') as x:
	writer = csv.writer(x)
	writer.writerows("hello")