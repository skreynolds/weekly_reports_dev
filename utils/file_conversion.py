#!/usr/bin/python

import csv

# The file conversion function for VET_weekly_AHC_YYYY.txt
# and can also be used for VET_weekly_AHC_[YYYY-1].txt
def convert_fw_to_csv_AHC(file_name, slices):

	# Specify a list of lists to store csv converted lines
	list_of_list = []

	# Read in all lines from the fixed width text file
	with open(file_name) as f:
		lines_list = f.readlines()
		
	# Create a list of lists which comprise the comma delimited
	# data sets
	for line in lines_list:

		if (line[0:10] == '----------'
			or line[0:8] == 'CAL_TYPE'):
			continue
		
		csv_line = [line[slice].strip() for slice in slices]
		list_of_list.append(csv_line)

	# Write the csv file output
	with open(file_name[:-4] + '.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(list_of_list)


# The file conversion function for VET_Course_Completions_YYYY.txt
def convert_fw_to_csv_completions(file_name, slices):
	
	# Specify a list of lists to store csv converted lines
	list_of_list = []

	# Read in all lines from the fixed width text file
	with open(file_name) as f:
		lines_list = f.readlines()
		
	# Create a list of lists which comprise the comma delimited
	# data sets
	for line in lines_list:

		if (line[0:10] == '----------'
			or line[1:10] == 'PERSON_ID'):
			continue

		csv_line = [line[slice].strip() for slice in slices]
		list_of_list.append(csv_line)

	# Write the csv file output
	with open(file_name[:-4] + '.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(list_of_list)


# The file conversion function for VET_YYYY_Apprentice.txt
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