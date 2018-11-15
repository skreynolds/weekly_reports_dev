#!/usr/bin/python

import psycopg2

from config import config

if __name__ == '__main__':
	'''Connect to the PostgreSQL database server'''
	conn = None
	
	try:

		# read connection parameters
		params = config()

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

		csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\xlookup\\xlookup_vfh_student_status.txt'

		copy_sql = 	"""
					COPY xlookup_vfh_student_status FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
					"""

		with open(csv_path, 'r') as f:
			cur.copy_expert(sql=copy_sql, file=f)

		#with open('output.csv', 'r') as f:
		#	cur.copy_from(f, 'weekly_current', sep=',', null='')

		#cur.execute("""
		#			COPY weekly_current
		#			FROM 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\dev_test\\output.csv' DELIMITER ',' CSV
		#			""")

		cur.close()

		# commit the changes
		conn.commit()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')