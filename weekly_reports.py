#!/usr/bin/python

import psycopg2

from utils.config import config
from utils.file_conversion import *
from xref.tables import *
from xref.fixed_widths import *

# Specify the current year the routine is running
DATE = 2018

if __name__ == '__main__':
	
	#############################################################
	# RUN VALIDATION TO ENSURE SUCCESSFUL EXECUTION
	#############################################################
	# SECTION OF CODE SHOULD CHECK FOR ESSENTIAL FILES AND ESSENTIAL
	# CONDITIONS TO ENSURE THAT THE SCRIPT WILL SUCCESSFULLY EXECUTE

	# Connect to the PostgreSQL database server
	conn = None
	
	try:
		

	#############################################################
	# PROCESS FIXED WIDTH FILES OUTPUT FROM CALLISTA
	#############################################################
		# File path for VET_weekly_AHC_YYYY.txt
		file = './data/VET_weekly_AHC_' + str(DATE) + '.txt'
		
		# Execute file conversion script
		convert_fw_to_csv_AHC(file, weekly_ahc_slices)

		# File path for VET_weekly_AHC_[YYYY-1].txt
		file = './data/VET_weekly_AHC_' + str(DATE-1) + '.txt'

		# Execute file conversion script
		convert_fw_to_csv_AHC(file, weekly_ahc_slices)

		# File path for VET_Course_Completions_2018.txt
		file = './data/VET_Course_Completions_' + str(DATE) + '.txt'

		# Execute file conversion script
		convert_fw_to_csv_completions(file, completions_slices)

		# File path for VET_2018_Apprentice.txt
		file = './data/VET_2018_Apprentice.txt'

		# Execute file conversion script
		convert_fw_to_csv_apprentices(file, apprentices_slices)


	#############################################################
	# CONNECT TO THE WEEKLY REPORTS DATABASE
	#############################################################
		# read connection parameters
		params = config()

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

	#############################################################
	# BUILD XLOOKUP
	#############################################################
		# create all of the xlookup tables
		for table_name in xlookup_tables.keys():

			# create table
			cur.execute(xlookup_tables[table_name])

			# define the file path for loading the data
			csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\xlookup\\' + table_name + '.txt'

			# load the data into the xlookup table
			copy_sql = 	"""
						COPY """ + table_name + """ FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
						"""

			with open(csv_path, 'r') as f:
				cur.copy_expert(sql=copy_sql, file=f)

	#############################################################
	# BUILD TABLES
	#############################################################
		# create errors_for_correction_by_vet_teams table
		cur.execute(tables['xref_error_for_correction_template'].format('errors_for_correction_by_vet_teams'))
		
		# create errors_for_correction_by_vet_stats_officer table
		cur.execute(tables['xref_error_for_correction_template'].format('errors_for_correction_by_vet_stats_officer'))

		# create errors_for_correction_by_vet_stats_officer table
		cur.execute(tables['xref_error_for_correction_template'].format('errors_for_correction_by_vet_teams_course_intention'))
		
		# create vet_course_completion_YYYY table
		cur.execute(tables['xref_vet_course_completions_YYYY_template'].format('vet_course_completions_' + str(DATE)))

		# create weekly_current table - (VET_weekly_AHC_YYYY is imported later)
		cur.execute(tables['xref_weekly_template'].format('current'))

		# create weekly_current table - (VET_weekly_AHC_[YYYY-1] is imported later)
		cur.execute(tables['xref_weekly_template'].format(str(DATE-1)))

		# create vet_course_completions table - (VET_Course_Completions_YYYY imported later)
		cur.execute(tables['xref_course_completions'])

		# create vet_apprentices table - (VET_YYYY_Apprentice is imported later)
		cur.execute(tables['xref_vet_apprentice_template'])

		# create student table
		cur.execute(tables['xref_student_template'])

		# create student_course_attempt table
		cur.execute(tables['xref_student_course_attempt_template'])

		# create student_unit_attempt table
		cur.execute(tables['xref_student_unit_attempt_template'])

		# create activity_pattern_trend table
		cur.execute(tables['xref_activity_pattern_trend_template'])

		# create unresulted_sua_2017 table
		cur.execute(tables['xref_unresulted_sua_template'].format(str(DATE-1)))

		# create team_activity table
		cur.execute(tables['xref_team_activity_template'])

		# create apprentice_sua table
		cur.execute(tables['xref_apprentice_sua_template'])

		# create apprentice_course table
		cur.execute(tables['xref_apprentice_course_template'])

		# create xref_vfh_unit_tp table
		cur.execute(tables['xref_vfh_unit_tp_template'])


	#############################################################
	# IMPORT DATA TO TABLES
	#############################################################
		
		############################################################
		# Import the VET_weekly_AHC_YYYY.csv
		csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\VET_weekly_AHC_' + str(DATE) + '.csv'

		copy_sql = 	"""
					COPY weekly_current FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
					"""

		with open(csv_path, 'r') as f:
			cur.copy_expert(sql=copy_sql, file=f)
		
		############################################################
		# Import the VET_weekly_AHC_[YYYY-1].csv
		csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\VET_weekly_AHC_' + str(DATE-1) + '.csv'

		copy_sql = 	"""
					COPY weekly_""" + str(DATE-1) + """ FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
					"""

		with open(csv_path, 'r') as f:
			cur.copy_expert(sql=copy_sql, file=f)

		############################################################
		# Import the VET_Course_Completions_YYYY.csv
		csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\VET_Course_Completions_' + str(DATE) + '.csv'

		copy_sql = 	"""
					COPY vet_course_completions FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
					"""

		with open(csv_path, 'r') as f:
			cur.copy_expert(sql=copy_sql, file=f)

		############################################################
		# Import the VET_2018_Apprentice.csv
		csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\VET_' + str(DATE) + '_Apprentice.csv'

		copy_sql = 	"""
					COPY vet_apprentice FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
					"""

		with open(csv_path, 'r') as f:
			cur.copy_expert(sql=copy_sql, file=f)

		############################################################
		# Import the xref_vfh_unit_tp.csv
		csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\xlookup\\xref_vfh_unit_tp.txt'

		copy_sql =  """
					COPY xref_vfh_unit_tp FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
					"""

		with open(csv_path, 'r') as f:
			cur.copy_expert(sql=copy_sql, file=f)

		

	#############################################################
	# RUN QUERIES TO BUILD REPORTS AND ERROR TABLES
	#############################################################


	#############################################################
	# EXPORT DATA 
	#############################################################


	#############################################################
	# CLOSE THE DATABASE
	#############################################################
		# close the communication with the PostgreSQL
		cur.close()

		# commit the changes
		conn.commit()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')