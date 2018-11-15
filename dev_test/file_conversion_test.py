#!/usr/bin/python

import csv

# Slices used to convert fixed width data to csv format ready for postres import
# for the VET_Course_Completions
apprentices_slices = 	[slice(0, 13, None),			# person id
						slice(13, 34, None),			# api id
						slice(34, 45, None),			# api type
						slice(45, 66, None),			# course code
						slice(66, 76, None),			# apt start date
						slice(76, 86, None),			# api end date
						slice(86, 97, None),			# funding source
						slice(97, 118, None),			# unit cd
						slice(118, 128, None),			# unit act end date
						slice(128, 138, None),			# enr act end dte
						slice(138, 149, None),			# addr type
						slice(149, 159, None),			# addr start date
						slice(159, 169, None),			# addr end date
						slice(169, 210, None),			# addr line1
						slice(210, 251, None),			# addr line2
						slice(251, 292, None),			# addr line3
						slice(292, 333, None),			# addr line4
						slice(333, 374, None),			# addr line5
						slice(374, 387, None),			# addr aust postcode
						#slice(387, 399, None),			# addr os postcode
						slice(399, 440, None),			# other details
						slice(440, 461, None),			# phone 3
						slice(461, 482, None),			# phone 2
						slice(482, 503, None)			# phone 1
						]


# The file conversion function for VET_Course_Completions_YYYY
def convert_fw_to_csv_apprentices(file_name, slices):
	# Specify a list of lists to store csv converted lines
	list_of_list = []

	# Read in all lines from the fixed width text file
	with open(file_name) as f:
		lines_list = f.readlines()
		
	# Create a list of lists which comprise the comma delimited
	# data sets
	for line in lines_list:
		
		if (line[0:12] == '------------'
			or line[0:12] == 'PE_PERSON_ID'):
			continue

		csv_line = [line[slice].strip() for slice in slices]
		list_of_list.append(csv_line)

	# Write the csv file output
	with open(file_name[:-4] + '.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(list_of_list)


# Main test function
if __name__ == '__main__':

	file = '../data/VET_2018_Apprentice.txt'

	convert_fw_to_csv_apprentices(file, apprentices_slices)