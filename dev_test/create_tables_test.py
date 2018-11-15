#!/usr/bin/python

import psycopg2
from config import config
from create_tables_sql import commands

conn = None

def create_tables():
	try:
		# read the connection parameters
		params = config()

		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		#####################################
		# Execute all tables
		#####################################
		'''
		for command in commands:
			# create table to test
			cur.execute(command)
		'''
		#####################################

		
		#####################################
		# Single table testing
		#####################################		
		
		# Create the table in the postgres database
		cur.execute("""
					CREATE TABLE student_unit_attempt (
					a_ses2006 text,
					aci text,
					administrative_unit_status text,
					age numeric,
					at_school_indicator text,
					atsi text,
					basis_for_admission text,
					basis_for_admission_code text,
					birth_country_code text,
					cancelled_date date,
					chessn text,
					contract text,
					contract_course_unit_code text,
					contract_course_unit_name text,
					contract_team text,
					correspondence_category text,
					country_of_birth text,
					course_admin_team text,
					course_attempt_status text,
					course_code text,
					course_commencement_date date,
					course_delivery_mode text,
					course_industry text,
					course_industry_name text,
					course_name text,
					course_requirements_completed_date date,
					course_requirements_completed_indicator text,
					deceased_indicator text,
					delivery_location_team text,
					delivery_postal_location text,
					delivery_providence text,
					delivery_region text,
					delivery_remoteness text,
					delivery_state_code text,
					disability_flag text,
					disc_date date,
					division text,
					email_address text,
					employment_category text,
					employment_category_description text,
					enrol_date date,
					enrol_week numeric,
					enrolled_ahc numeric,
					enrolment_activity_end_date date,
					entitlement_contract_description text,
					fee_category text,
					grade text,
					grade_keyed text,
					granted_date date,
					hecs_payment_option text,
					hecs_payment_option_code text,
					highest_prior_education_level_completed text,
					highest_prior_education_level_completed_code text,
					highest_school_level_completed text,
					highest_school_level_completed_code text,
					highest_school_level_completed_year text,
					home_language_code text,
					intention_to_complete_course text,
					intention_to_complete_units_only text,
					language text,
					level text,
					mobile_phone_number text,
					no_course_intention text,
					not_approved_date date,
					outcome text,
					override_activity_end_date date,
					override_activity_start_date date,
					postal_postcode text,
					residential_postcode text,
					result_date date,
					result_type text,
					result_week numeric,
					resulted_ahc numeric,
					sca_funding_source text,
					staff_indicator text,
					stream_code text,
					student_first_name text,
					student_gender text,
					student_home_state text,
					student_id text,
					student_last_name text,
					study_reason text,
					study_reason_description text,
					tci text,
					teaching_period text,
					teaching_period_end_date text,
					unit_attempt_status text,
					unit_census_date date,
					unit_code text,
					unit_contact text,
					unit_delivery_description text,
					unit_delivery_location text,
					unit_delivery_type text,
					unit_funding_source text,
					unit_name text,
					unit_student_status text,
					unit_student_status_code text,
					ur_outcome text,
					usi_flag text,
					vet_in_school_indicator text,
					vet_school_name text,
					vfh_arrival_year text,
					vfh_atsi_code text,
					vfh_atsi_description text,
					vfh_birth_country_code text,
					vfh_birth_country_description text,
					vfh_citizenship_code text,
					vfh_citizenship_description text,
					vfh_commencing_geographic_location text,
					vfh_commencing_location_postcode text,
					vfh_highest_attainment_code text,
					vfh_highest_attainment_description text,
					vfh_highest_attainment_year text,
					vfh_home_language_code text,
					vfh_home_language_description text,
					vfh_home_location_country_code text,
					vfh_home_location_country_description text,
					vfh_home_location_postcode text,
					vfh_permanent_resident_code text,
					vfh_permanent_resident_status text,
					vfh_term_location_country_code text,
					vfh_term_location_country_description text,
					vfh_term_location_postcode text,
					unit_delivery_location_description text
					)
					""")

		# table name for data
		#table_name = 'xref_vfh_unit_tp'

		# define the file path for loading the data
		#csv_path = 'C:\\Users\\sreynolds2\\Documents\\dev\\weekly_reports_dev\\data\\xlookup\\' + table_name + '.txt'

		# load the data into the xlookup table
		#copy_sql = 	"""
		#			COPY """ + table_name + """ FROM stdin WITH DELIMITER as ',' CSV QUOTE as '"'
		#			"""

		#with open(csv_path, 'r') as f:
		#	cur.copy_expert(sql=copy_sql, file=f)

		#####################################


		#####################################
		# Code for dropping table
		#####################################

		# drop a created table
		#cur.execute("""DROP TABLE IF EXISTS team_target_summary_2018""")

		#####################################



		# close communication with the PostgreSQL database server
		cur.close()

		# commit the changes
		conn.commit()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

if __name__ == '__main__':
	create_tables()