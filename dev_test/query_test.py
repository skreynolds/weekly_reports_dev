#!/usr/bin/python

import psycopg2

from config import config

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
	# CONNECT TO THE WEEKLY REPORTS DATABASE
	#############################################################
		# read connection parameters
		params = config()

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)

		# create a cursor
		cur = conn.cursor()

		##################################################
		# q201 - tested OK
		'''
		cur.execute("""
					DELETE FROM weekly_current
					WHERE enrolled_ahc is NULL
					""")
		'''
		# q202 - tested OK
		'''
		cur.execute("""
					DELETE FROM weekly_2017
					WHERE enrolled_ahc is NULL
					""")
		'''
		# q205 - tested OK
		'''
		cur.execute("""
					DELETE FROM vet_course_completions
					WHERE course_requirements_completed_date is NULL
					""")
		'''
		# q211 - tested OK
		'''
		cur.execute("""
					DELETE FROM vet_apprentice
					WHERE (person_id NOT SIMILAR TO '[0-9]*'
					OR person_id is Null)
					""")
		'''
		# q301 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Funding Source is Redundant or Absent' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE unit_funding_source is NULL
					OR unit_funding_source LIKE '0%'
					OR unit_funding_source = '11P'
					""")
		'''
		# q302 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Contract Team Missing or Invalid' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE (delivery_location_team is NULL AND outcome <> 'CT')
					OR (delivery_location_team not SIMILAR TO '###' AND outcome <> 'CT')
					""")
		'''
		# q303 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Enrol Date Typo' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE enrol_date > '2017-12-31' 
					AND outcome NOT in ('RPL-UR','RPL','RPL-CAN','RPL-NOT')
					""")
		'''
		# q304 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Enrol Date Typo' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE student_gender = 'U'
					""")
		'''
		# q305a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					WHERE unit_funding_source = '30A'
					""")
		'''
		# q305b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET student_home_state = 'Overseas'
					WHERE contract_team = 'Y'
					""")
		'''
		# q305c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q305d - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Invalid State' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE student_home_state <> 'NT'
					AND student_home_state <> 'QLD'
					AND student_home_state <> 'NSW'
					AND student_home_state <> 'VIC'
					AND student_home_state <> 'TAS'
					AND student_home_state <> 'SA'
					AND student_home_state <> 'WA'
					AND student_home_state <> 'ACT'
					AND student_home_state <> 'UNK'
					AND student_home_state <> 'UNKNOWN'
					AND student_home_state <> 'Overseas'
					""")
		'''
		# q306 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Missing DOB' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE student_dob is NULL
					""")
		'''
		# q307 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET highest_prior_education_level_completed_code = '@@@'
					WHERE highest_prior_education_level_completed_code is NULL
					""")
		'''
		# q307a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					FROM xlookup_prior_education_level					
					WHERE weekly_current.highest_prior_education_level_completed_code = xlookup_prior_education_level.level_code
					OR weekly_current.highest_prior_education_level_completed_code is NULL
					""")
		'''
		# q307b - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Invalid Prior Education Identifier' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE contract_team is NULL
					""")
		'''
		# q307c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q308 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Invalid Highest School Level Completed Year' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE (Right(highest_school_level_completed_year,4)>'2018'
					AND Right(highest_school_level_completed_year,4) Not LIKE '@@@@') 
					OR (Right(highest_school_level_completed_year,4)<'1918'
					AND Right(highest_school_level_completed_year,4) Not LIKE '@@@@')
					""")
		'''
		# q309 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Never went to school so invalid Highest School Level Completed Year' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE highest_school_level_completed_code='02'
					AND (highest_school_level_completed_year is not NULL
					AND highest_school_level_completed_year<>'@@@@')
					""")
		'''
		# q310a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					FROM xlookup_language
					WHERE weekly_current.home_language_code = xlookup_language.identifier
					AND weekly_current.home_language_code is not NULL
					""")
		'''
		# q310b - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Invalid Home Language Code' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE home_language_code is not NULL
					AND contract_team is NULL
					""")
		'''
		# q310c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q311a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					FROM xlookup_country
					WHERE weekly_current.birth_country_code = xlookup_Country.identifier
					""")
		'''
		# q311b - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Invalid Birth Country Code' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.birth_country_code is not NULL
					AND weekly_current.contract_team is NULL
					""")
		'''
		# q311c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q312a - tested OK
		'''
		cur.execute("""
					UPDATE WEEKLY_CURRENT
					SET contract_team = 'Y'
					FROM xlookup_course
					WHERE TRIM(weekly_current.course_code) = TRIM(xlookup_course.code)
					""")
		'''
		# q312b - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Missing Course in xlookup_Course table' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE contract_team is NULL
					""")
		'''
		# q312c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q314a - tested OK (no data needs further testing)
		'''
		cur.execute("""
					SELECT delivery_location_team, student_id, student_first_name, student_last_name,
					course_code, unit_code, teaching_period, grade, unit_delivery_location, enrol_date,
					enrolment_activity_end_date
					INTO errors_wf_graded_sua_douglas_to_check
					FROM weekly_current
					WHERE weekly_current.grade='WF'
					""")
		'''
		# q314b - tested OK
		'''
		cur.execute("""
					SELECT delivery_location_team, student_id, student_first_name, student_last_name,
					course_code, unit_code, teaching_period, grade, unit_delivery_location, enrol_date,
					enrolment_activity_end_date
					INTO errors_w_graded_vfh_sua_douglas_to_check
					FROM weekly_current
					WHERE (weekly_current.teaching_period LIKE 'VFH%' AND weekly_current.grade='W')
					OR (weekly_current.teaching_period LIKE 'VFH%' AND weekly_current.grade='WW')
					""")
		'''
		# q315a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					FROM xlookup_team
					WHERE weekly_current.course_admin_team = xlookup_team.code
					AND xlookup_team.current_2018='Y'
					""")
		'''
		# q315b - tested OK	(no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Missing or invalid Course Admin Team' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE contract_team is NULL
					""")
		'''
		# q315c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q316a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					FROM xlookup_study_reason
					WHERE weekly_current.study_reason = xlookup_study_reason.study_reason_id
					AND xlookup_study_reason.current_2018='Y'
					""")
		'''
		# q316b - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Missing or invalid Study Reason ID' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE contract_team is NULL
					""")
		'''
		# q316c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q317a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = 'Y'
					FROM xlookup_location
					WHERE weekly_current.unit_delivery_location = xlookup_location.code
					""")
		'''
		# q317b - tested OK (no data needs further testing)
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Missing or invalid Location Code in xlookup_location table' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE contract_team is NULL
					""")
		'''
		# q317c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = NULL
					WHERE contract_team is not NULL
					""")
		'''
		# q318 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					SELECT weekly_current.delivery_location_team AS delivery_location_team_2018,
					weekly_current.student_id, weekly_current.student_first_name, weekly_current.student_last_name,
					weekly_2017.course_code AS course_code_2017, weekly_2017.unit_code AS unit_code_2017,
					weekly_2017.grade AS grade_2017, weekly_2017.result_date AS result_date_2017,
					weekly_2017.unit_funding_source AS unit_funding_source_2017,
					weekly_current.course_code AS course_code_2018, weekly_current.unit_code AS unit_code_2018,
					weekly_current.grade AS grade_2018, weekly_current.result_date AS result_date_2018,
					weekly_current.unit_funding_source AS unit_funding_source_2018
					INTO errors_2017_comp_or_ur_ce_2018_reenrolled_douglas_to_check
					FROM weekly_2017
					INNER JOIN weekly_current
					ON weekly_2017.unit_code = weekly_current.unit_code
					AND weekly_2017.student_id = weekly_current.student_id
					WHERE weekly_2017.grade in ('CT','CA','CU','C','RPL')
					AND weekly_current.grade not in ('CT','SW','NS')
					AND weekly_2017.unit_delivery_type<>'RPL'
					""")
		'''
		# q320 - tested OK (no data needs further testing)
		'''
		cur.execute("""
					UPDATE weekly_current
					SET vet_in_school_indicator = '@'
					WHERE vet_in_school_indicator is NULL
					""")
		'''
		# q321 - tested NOT OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student has 30A funding code but born in Australia. Please check' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.birth_country_code='1100'
					AND weekly_current.unit_funding_source='30A'
					""")
		'''
		# q322 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student has 30A funding code but a home postcode different to OSPC. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.residential_postcode<>'OSPC'
					AND weekly_current.unit_funding_source='30A'
					""")
		'''
		# q323 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'ATSI student born overseas. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.atsi='Y'
					AND weekly_current.birth_country_code NOT IN ('@@@@','0000','1100','1101','1102','1199')
					""")
		'''
		# q324 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'ATSI student with language other than English or Indigenous. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.atsi='Y'
					AND (weekly_current.home_language_code NOT IN ('1201','1','@@@@','0000')
					AND weekly_current.home_language_code NOT LIKE '8%'
					AND weekly_current.home_language_code NOT Like '97%')
					""")
		'''
		# q325 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student Home Language is Australian Indigenous but student birth country not Australia. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.home_language_code LIKE '8%' 
					AND weekly_current.birth_country_code NOT IN ('@@@@','0000','1100','1101','1102','1199')
					""")
		'''
		# q326a - tested OK
		'''
		cur.execute("""
					SELECT 	course_admin_team, delivery_location_team, teaching_period, student_id,
							deceased_indicator, atsi, student_last_name, student_first_name, student_gender,
							student_dob, highest_school_level_completed_code, highest_school_level_completed_year,
							disability_flag, home_language_code, birth_country_code, residential_postcode,
							student_home_state, highest_prior_education_level_completed_code, employment_category,
							(CASE
								WHEN extract(YEAR FROM student_dob::date) >= extract(YEAR FROM now()::date) THEN
									highest_school_level_completed_year::numeric - extract(YEAR FROM student_dob::date) + 100
								ELSE 
									highest_school_level_completed_year::numeric - extract(YEAR FROM student_dob::date)
							END) AS age_highest_school_completed,
							at_school_indicator, course_code, unit_code, unit_funding_source, enrol_date, study_reason
					INTO age_highest_school_completed
					FROM weekly_current
					WHERE student_dob is not NULL
					AND highest_school_level_completed_code not in ('@@','02')
					AND weekly_current.highest_school_level_completed_year <> '@@@@'
					ORDER BY 	(CASE
									WHEN extract(YEAR FROM student_dob::date) >= extract(YEAR FROM now()::date) THEN
										highest_school_level_completed_year::numeric - extract(YEAR FROM student_dob::date) + 100
									ELSE
										highest_school_level_completed_year::numeric - extract(YEAR FROM student_dob::date)
								END)
					""")
		'''
		# q326b - tested NOT OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 	CONCAT('Student was ', age_highest_school_completed, ' when they completed Year ', highest_school_level_completed_code, '. Please check.') AS error_message,
							course_admin_team, delivery_location_team, teaching_period, student_id, deceased_indicator, atsi,
							student_last_name, student_first_name, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code,
							employment_category, age_highest_school_completed, at_school_indicator, highest_school_level_completed_code,
							highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date, study_reason
					FROM age_highest_school_completed
					WHERE (age_highest_school_completed.age_highest_school_completed < 11
					AND age_highest_school_completed.age_highest_school_completed is not NULL
					AND age_highest_school_completed.highest_school_level_completed_code = '09')
					OR (age_highest_school_completed.age_highest_school_completed < 12
					AND age_highest_school_completed.age_highest_school_completed Is Not Null
					AND age_highest_school_completed.highest_school_level_completed_code = '10')
					OR (age_highest_school_completed.age_highest_school_completed < 13
					AND age_highest_school_completed.age_highest_school_completed Is Not Null
					AND age_highest_school_completed.highest_school_level_completed_code = '11')
					OR (age_highest_school_completed.age_highest_school_completed < 14
					AND age_highest_school_completed.age_highest_school_completed Is Not Null
					AND age_highest_school_completed.highest_school_level_completed_code = '12')
					OR (age_highest_school_completed.age_highest_school_completed < 10
					AND age_highest_school_completed.age_highest_school_completed Is Not Null
					AND age_highest_school_completed.highest_school_level_completed_code = '08')
					ORDER BY age_highest_school_completed.student_id
					""")
		'''
		# q327 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Students name starts with a space or contains numbers. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.student_last_name LIKE ' %'
					OR weekly_current.student_first_name LIKE ' %'
					OR weekly_current.student_last_name SIMILAR TO '%[0-9]%'
					OR weekly_current.student_first_name SIMILAR TO '%[0-9]%'
					OR weekly_current.student_last_name LIKE '% '
					OR weekly_current.student_first_name LIKE '% '
					ORDER BY weekly_current.student_id
					""")
		'''
		# q328 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student is ATSI but Home Postcode is OSPC. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.atsi='Y'
					AND weekly_current.residential_postcode='OSPC'
					ORDER BY weekly_current.student_id
					""")
		'''
		# q329 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student is employed full time but also has an At School flag of Y. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.employment_category='01'
					AND weekly_current.at_school_indicator='Y'
					AND weekly_current.unit_funding_source NOT LIKE '%K'
					ORDER BY weekly_current.student_id
					""")
		'''
		# q330 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student has At School Flag Y but is older than usual. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE at_school_indicator='Y'
					AND ((CASE
							WHEN student_dob IS NOT NULL
								THEN EXTRACT(YEAR FROM AGE(student_dob::date))
							ELSE
								NULL
						END) > 20)
					ORDER BY weekly_current.student_id
					""")
		'''
		# q331 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Student has At School Flag Y but is older than usual. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE EXTRACT(YEAR FROM AGE(student_dob::date)) < 11
					ORDER BY weekly_current.student_id
					""")
		'''
		# q332 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams_course_intention (error_type, course_admin_team, student_id,
																					student_last_name, student_first_name, course_code,
																					intention_to_complete_course, intention_to_complete_units_only,
																					no_course_intention)
					SELECT DISTINCT 'Student has a course intention conflict. Cannot say yes to more than one. Please check.' AS error_message,
									course_admin_team, student_id, student_last_name, student_first_name, course_code, intention_to_complete_course,
									intention_to_complete_unit_only, no_course_intention
					FROM weekly_current
					WHERE (intention_to_complete_course='Y' AND intention_to_complete_unit_only='Y')
					OR (intention_to_complete_unit_only='Y' AND no_course_intention='Y')
					OR (intention_to_complete_course='Y' AND no_course_intention='Y')
					OR (intention_to_complete_course='Y' AND intention_to_complete_unit_only='Y' AND no_course_intention='Y')
					ORDER BY student_id
					""")
		'''
		# q333 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams_course_intention (error_type, course_admin_team, student_id,
																					student_last_name, student_first_name, course_code, 
																					intention_to_complete_course, intention_to_complete_units_only,
																					no_course_intention)
					SELECT DISTINCT 'Course intention details are missing. Please check.' AS error_message,
									course_admin_team, student_id, student_last_name, student_first_name, course_code, intention_to_complete_course,
									intention_to_complete_unit_only, no_course_intention
					FROM weekly_current
					WHERE intention_to_complete_course is NULL
					AND intention_to_Complete_Unit_Only is NULL
					AND no_course_intention is NULL
					ORDER BY course_admin_team, student_id
					""")
		'''
		# q334 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Apprentice SCA cannot have a UNIT ONLY COURSE COMPLETION INTENTION. Please correct.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name, 
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE course_code <> 'LRNSUPP'
					AND sca_funding_source LIKE '%K'
					AND intention_to_complete_unit_only='Y'
					""")
		'''
		# q335 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'ASSESSING is not a valid Unit Attempt Status where the Outcome is Credit Transfer. Please correct.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE teaching_period='CRDT-TRANS'
					AND unit_attempt_status='ASSESSING'
					""")
		'''
		# q336 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Not an eligible ETP Course. Please check.' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, weekly_current.course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current LEFT JOIN xlookup_etp_eligible_course_list
					ON weekly_current.course_code = xlookup_etp_eligible_course_list.course_code
					WHERE weekly_current.course_code<>'LRNSUPP'
					AND weekly_current.unit_funding_source='ETP'
					AND xlookup_etp_eligible_course_list.course_code is NULL
					""")
		'''
		# q337 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, student_id, student_last_name,
																	student_first_name, dob, residential_post_code, home_state, at_school_indicator,
																	course_code, unit_funding_source, no_course_intention,
																	intention_to_complete_units_only)
					SELECT DISTINCT 'Does not meet ETP eligibility criteria - too young, at school, or non-NT resident. Please check.' AS error_message,
									course_admin_team, student_id, student_last_name, student_first_name, student_dob, residential_postcode, student_home_state,
									at_school_indicator, course_code, unit_funding_source, no_course_intention, intention_to_complete_unit_only
					FROM weekly_current
					WHERE (unit_funding_source='ETP'
					AND (EXTRACT(YEAR FROM AGE(student_dob::date)) < 17))
					OR ((at_school_indicator='Y' Or at_school_indicator='@')
					AND unit_funding_source='ETP')
					OR ((residential_postcode NOT LIKE '8%' AND residential_postcode NOT LIKE '9%' AND residential_postcode NOT IN ('@@@@','0000'))
					AND unit_funding_source='ETP')
					OR (course_code <> 'LRNSUPP'
					AND unit_funding_source='ETP'
					AND intention_to_complete_unit_only='Y')
					OR (course_code <> 'LRNSUPP'
					AND unit_funding_source = 'ETP'
					AND no_course_intention = 'Y')
					ORDER BY student_id
					""")
		'''
		# q342 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, delivery_location_team, teaching_period,
																	student_id, atsi, deceased_indicator, student_last_name, student_first_name,
																	gender, dob, disability, home_language_code, birth_country_code, residential_post_code,
																	home_state, prior_education, employment_category, at_school_indicator,
																	highest_school_level_completed_code, highest_school_level_completed_year,
																	course_code, unit_code, unit_funding_source, enrol_date, study_reason, unit_attempt_status,
																	outcome, granted_date, cancelled_date, not_approved_date)
					SELECT 'Advanced Standing missing Basis Details. Please check.' AS error_message, course_admin_team, delivery_location_team,
							teaching_period, student_id, atsi, deceased_indicator, student_last_name, student_first_name, student_gender,
							student_dob, disability_flag, home_language_code, birth_country_code, residential_postcode, student_home_state,
							highest_prior_education_level_completed_code, employment_category, at_school_indicator, highest_school_level_completed_code,
							highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date, study_reason,
							unit_attempt_status, outcome, granted_date, cancelled_date, not_approved_date
					FROM weekly_current
					WHERE (teaching_period is NULL AND unit_attempt_status='GRANTED')
					OR (teaching_period is NULL AND unit_attempt_status='NOT-APPRVD')
					ORDER BY student_id
					""")
		'''
		# q343 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, delivery_location_team, teaching_period,
																	student_id, atsi, deceased_indicator, student_last_name, student_first_name,
																	gender, dob, disability, home_language_code, birth_country_code, residential_post_code,
																	home_state, prior_education, employment_category, at_school_indicator,
																	highest_school_level_completed_code, highest_school_level_completed_year,
																	course_code, unit_code, unit_funding_source, enrol_date, study_reason, unit_attempt_status,
																	outcome, granted_date, cancelled_date, not_approved_date)
					SELECT 'Diploma and above course enrolment but not in VFH Teaching period. Please check.' AS error_message, course_admin_team, delivery_location_team,
							teaching_period, student_id, atsi, deceased_indicator, student_last_name, student_first_name, student_gender,
							student_dob, disability_flag, home_language_code, birth_country_code, residential_postcode, student_home_state,
							highest_prior_education_level_completed_code, employment_category, at_school_indicator, highest_school_level_completed_code,
							highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date, study_reason,
							unit_attempt_status, outcome, granted_date, cancelled_date, not_approved_date
					FROM weekly_current
					WHERE (teaching_period NOT LIKE 'VFH%'
					AND teaching_period <> 'CRDT-TRANS'
					AND unit_funding_source <> '30A'
					AND outcome NOT IN ('SW','W')
					AND (course_name LIKE 'Diploma%'
					OR course_name LIKE 'DIPLOMA%'
					OR course_name LIKE 'Grad%'
					OR course_name LIKE 'GRAD%'))
					OR (teaching_period NOT LIKE 'VFH%'
					AND teaching_period <> 'CRDT-TRANS'
					AND unit_funding_source <> '30A'
					AND outcome IS NULL
					AND (course_name LIKE 'Diploma%' 
					OR course_name LIKE 'DIPLOMA%'
					OR course_name LIKE 'Grad%'
					OR course_name LIKE 'GRAD%'))
					ORDER BY student_id
					""")
		'''
		# q345 - tested OK
		'''
		cur.execute("""
					SELECT weekly_current.teaching_period, weekly_current.student_id, weekly_current.course_admin_team,
					weekly_current.unit_delivery_location, xlookup_location.remoteness AS unit_delivery_remoteness,
					weekly_current.delivery_location_team, weekly_current.unit_funding_source, weekly_current.course_delivery_mode,
					weekly_current.course_code, weekly_current.fee_category, weekly_current.course_name, weekly_current.unit_code,
					weekly_current.unit_name, weekly_current.enrolled_ahc, weekly_current.resulted_ahc, weekly_current.grade,
					weekly_current.atsi, weekly_current.course_industry, weekly_current.student_last_name, weekly_current.student_first_name,
					weekly_current.aci, weekly_current.tci, weekly_current.student_dob, weekly_current.override_activity_end_date,
					weekly_current.unit_attempt_status, weekly_current.correspondence_category, weekly_current.student_gender,
					weekly_current.student_home_state, weekly_current.grade_keyed, weekly_current.deceased_indicator, weekly_current.vet_school_name,
					weekly_current.unit_delivery_type, weekly_current.enrol_date, weekly_current.disc_date, weekly_current.result_date,
					weekly_current.staff_indicator, weekly_current.stream_code, weekly_current.study_reason, weekly_current.granted_date,
					weekly_current.vet_in_school_indicator, weekly_current.at_school_indicator, weekly_current.highest_prior_education_level_completed_code,
					weekly_current.home_language_code, weekly_current.birth_country_code, weekly_current.highest_school_level_completed_code,
					weekly_current.highest_school_level_completed_year, weekly_current.residential_postcode, weekly_current.employment_category,
					weekly_current.disability_flag, weekly_current.course_attempt_status, weekly_current.course_commencement_date,
					weekly_current.sca_funding_source, weekly_current.enrolment_activity_end_date, weekly_current.postal_postcode,
					weekly_current.override_activity_start_date, weekly_current.intention_to_complete_course,
					weekly_current.intention_to_complete_unit_only, weekly_current.no_course_intention, weekly_current.course_requirements_completed_indicator,
					weekly_current.course_requirements_completed_date, weekly_current.result_type, weekly_current.unit_contact,
					weekly_current.cancelled_date, weekly_current.not_approved_date, weekly_current.administrative_unit_status, weekly_current.chessn,
					weekly_current.vfh_atsi_code, weekly_current.vfh_citizenship_code, weekly_current.vfh_birth_country_code, weekly_current.vfh_home_language_code,
					weekly_current.vfh_term_location_postcode, weekly_current.vfh_term_location_country_code, weekly_current.vfh_home_location_postcode,
					weekly_current.vfh_home_location_country_code, weekly_current.vfh_arrival_year, weekly_current.vfh_permanent_resident_code,
					weekly_current.vfh_commencing_location_postcode, weekly_current.vfh_commencing_geographic_location, weekly_current.vfh_highest_attainment_code,
					weekly_current.vfh_highest_attainment_year, weekly_current.basis_for_admission_code, weekly_current.hecs_payment_option_code,
					weekly_current.unit_student_status_code, weekly_current.unit_census_date, weekly_current.contract_course_unit_name,
					weekly_current.contract_course_unit_code, weekly_current.contract, weekly_current.outcome, weekly_current.age,
					weekly_current.teaching_period_end_date, weekly_current.enrol_week, weekly_current.result_week, weekly_current.contract_team,
					weekly_current.ur_outcome
					INTO vfh_unit_attempts
					FROM weekly_current
					INNER JOIN xlookup_location
					ON unit_delivery_location = xlookup_location.code
					WHERE (weekly_current.teaching_period LIKE 'VFH%'
					AND weekly_current.grade NOT IN ('SW','W'))
					OR (weekly_current.teaching_period LIKE 'VFH%'
					AND weekly_current.grade IS NULL)
					""")
		'''
		# q346 - tested OK
		'''
		cur.execute("""
					SELECT 'Course, Unit and/or Teaching period does not correspond to the VFH Unit schedule'::text AS error_type,
					vfh_unit_attempts.course_admin_team, vfh_unit_attempts.teaching_period, vfh_unit_attempts.student_id,
					vfh_unit_attempts.course_code, vfh_unit_attempts.unit_code, vfh_unit_attempts.unit_delivery_location,
					vfh_unit_attempts.unit_delivery_remoteness, vfh_unit_attempts.unit_funding_source, vfh_unit_attempts.fee_category,
					vfh_unit_attempts.grade, vfh_unit_attempts.administrative_unit_status, vfh_unit_attempts.chessn,
					vfh_unit_attempts.atsi AS vet_stats_atsi, vfh_unit_attempts.vfh_atsi_code, vfh_unit_attempts.vfh_citizenship_code,
					vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code, vfh_unit_attempts.vfh_term_location_postcode,
					vfh_unit_attempts.vfh_term_location_country_code, vfh_unit_attempts.vfh_home_location_postcode,
					vfh_unit_attempts.vfh_home_location_country_code, vfh_unit_attempts.vfh_arrival_year,
					vfh_unit_attempts.vfh_permanent_resident_code, vfh_unit_attempts.vfh_commencing_location_postcode,
					vfh_unit_attempts.vfh_commencing_geographic_location, vfh_unit_attempts.vfh_highest_attainment_code,
					vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
					vfh_unit_attempts.hecs_payment_option_code, vfh_unit_attempts.unit_student_status_code, vfh_unit_attempts.enrol_date,
					vfh_unit_attempts.unit_census_date
					INTO error_vfh_enrolments_by_vet_teams
					FROM vfh_unit_attempts
					LEFT JOIN xref_vfh_unit_tp
					ON vfh_unit_attempts.course_code = xref_vfh_unit_tp.Course
					AND vfh_unit_attempts.teaching_period = xref_vfh_unit_tp.teaching_period
					AND vfh_unit_attempts.unit_code = xref_vfh_unit_tp.unit
					WHERE xref_vfh_unit_tp.teaching_period IS NULL
					AND xref_vfh_unit_tp.unit IS NULL
					AND xref_vfh_unit_tp.course IS NULL
					""")
		'''
		# q347a - tested OK
		'''
		cur.execute("""
					SELECT 'Course, Unit or Teaching period does not correspond to the VFH Unit schedule'::text AS error_type,
					vfh_unit_attempts.course_admin_team, vfh_unit_attempts.teaching_period, vfh_unit_attempts.student_id,
					vfh_unit_attempts.course_code, vfh_unit_attempts.unit_code, vfh_unit_attempts.unit_delivery_location,
					vfh_unit_attempts.unit_delivery_remoteness, vfh_unit_attempts.unit_funding_source, vfh_unit_attempts.fee_category,
					vfh_unit_attempts.grade, vfh_unit_attempts.administrative_unit_status, vfh_unit_attempts.chessn,
					vfh_unit_attempts.atsi AS vet_stats_atsi, vfh_unit_attempts.vfh_atsi_code, vfh_unit_attempts.vfh_citizenship_code,
					vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code, vfh_unit_attempts.vfh_term_location_postcode,
					vfh_unit_attempts.vfh_term_location_country_code, vfh_unit_attempts.vfh_home_location_postcode,
					vfh_unit_attempts.vfh_home_location_country_code, vfh_unit_attempts.vfh_arrival_year,
					vfh_unit_attempts.vfh_permanent_resident_code, vfh_unit_attempts.vfh_commencing_location_postcode,
					vfh_unit_attempts.vfh_commencing_geographic_location, vfh_unit_attempts.vfh_highest_attainment_code,
					vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
					vfh_unit_attempts.hecs_payment_option_code, vfh_unit_attempts.unit_student_status_code, vfh_unit_attempts.enrol_date,
					vfh_unit_attempts.unit_census_date
					INTO q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule
					FROM vfh_unit_attempts
					LEFT JOIN xref_vfh_unit_tp
					ON vfh_unit_attempts.teaching_period = xref_vfh_unit_tp.teaching_period
					AND vfh_unit_attempts.unit_code = xref_vfh_unit_tp.unit
					AND vfh_unit_attempts.course_code = xref_vfh_unit_tp.course
					AND vfh_unit_attempts.unit_delivery_location = xref_vfh_unit_tp.location
					WHERE xref_vfh_unit_tp.Location IS NULL
					AND xref_vfh_unit_tp.teaching_period IS NULL
					AND xref_vfh_unit_tp.unit IS NULL
					AND xref_vfh_unit_tp.course IS NULL
					ORDER BY vfh_unit_attempts.course_code, vfh_unit_attempts.unit_code
					""")
		'''
		# q347b - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, teaching_period, student_id,
																	course_code, unit_code, unit_delivery_location, unit_delivery_remoteness,
																	unit_funding_source, fee_category, grade, administrative_unit_status,
																	chessn, vet_stats_atsi, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code, unit_student_status_code, enrol_date, unit_census_date )
					SELECT DISTINCT 'Course, Unit, Teaching period and Location does not correspond to the VFH Unit schedule' AS error_type,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.course_admin_team,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.teaching_period,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.student_id,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.course_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_delivery_location,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_delivery_remoteness,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_funding_source,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.fee_category,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.grade,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.administrative_unit_status,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.chessn,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vet_stats_atsi,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_atsi_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_citizenship_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_birth_country_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_home_language_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_term_location_postcode,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_term_location_country_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_home_location_postcode,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_home_location_country_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_arrival_year,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_permanent_resident_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_commencing_location_postcode,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_commencing_geographic_location,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_highest_attainment_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.vfh_highest_attainment_year,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.basis_for_admission_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.hecs_payment_option_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_student_status_code,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.enrol_date,
					q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_census_date
					FROM xref_vfh_unit_tp
					INNER JOIN q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule
								LEFT JOIN error_vfh_enrolments_by_vet_teams
								ON q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.teaching_period = error_vfh_enrolments_by_vet_teams.teaching_period
								AND q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_code = error_vfh_enrolments_by_vet_teams.unit_code
								AND q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.course_code = error_vfh_enrolments_by_vet_teams.course_code
								AND q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.student_id = error_vfh_enrolments_by_vet_teams.student_id
					ON xref_vfh_unit_tp.teaching_period = q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.teaching_period
					AND xref_vfh_unit_tp.course = q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.course_code
					AND xref_vfh_unit_tp.unit = q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_code
					WHERE error_vfh_enrolments_by_vet_teams.teaching_period IS NULL
					AND error_vfh_enrolments_by_vet_teams.student_id IS NULL
					AND error_vfh_enrolments_by_vet_teams.course_code IS NULL
					AND error_vfh_enrolments_by_vet_teams.unit_code IS NULL
					AND ((q347a_append_error_vfh_course_unit_tp_loc_not_in_schedule.unit_delivery_location='EXT') And (xref_vfh_unit_tp.delivery NOT LIKE '_O_')) = False
					""")
		'''
		# q348 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	chessn, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing CHESSN' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.chessn,
									vfh_unit_attempts.vfh_atsi_code, vfh_unit_attempts.vfh_citizenship_code,
									vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code,
									vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code,
									vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code,
									vfh_unit_attempts.vfh_commencing_location_postcode, vfh_unit_attempts.vfh_commencing_geographic_location,
									vfh_unit_attempts.vfh_highest_attainment_code, vfh_unit_attempts.vfh_highest_attainment_year,
									vfh_unit_attempts.basis_for_admission_code, vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					WHERE vfh_unit_attempts.chessn IS NULL
					""")
		'''
		# q349 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code, chessn,
																	vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code, vfh_home_language_code,
																	vfh_term_location_postcode, vfh_term_location_country_code, vfh_home_location_postcode,
																	vfh_home_location_country_code, vfh_arrival_year, vfh_permanent_resident_code,
																	vfh_commencing_location_postcode, vfh_commencing_geographic_location, vfh_highest_attainment_code,
																	vfh_highest_attainment_year, basis_for_admission_code, hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing OR invalid VFH Language Code' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
									vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code,
									vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code,
									vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code, vfh_unit_attempts.vfh_commencing_location_postcode,
									vfh_unit_attempts.vfh_commencing_geographic_location, vfh_unit_attempts.vfh_highest_attainment_code,
									vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
									vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					LEFT JOIN xlookup_vfh_language
					ON vfh_unit_attempts.vfh_home_language_code = xlookup_vfh_language.vfh_home_language_cd
					WHERE xlookup_VFH_Language.VFH_Home_Language_Cd IS NULL
					""")
		'''
		# q350 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, teaching_period, student_id, course_code,
																	unit_delivery_remoteness, unit_code, unit_delivery_location, unit_funding_source, grade,
																	administrative_unit_status, chessn, vfh_atsi_code, vfh_citizenship_code,
																	vfh_birth_country_code, vfh_home_language_code, vfh_term_location_postcode,
																	vfh_term_location_country_code, vfh_home_location_postcode, vfh_home_location_country_code,
																	vfh_arrival_year, vfh_permanent_resident_code, vfh_commencing_location_postcode,
																	vfh_commencing_geographic_location, vfh_highest_attainment_code,
																	vfh_highest_attainment_year, basis_for_admission_code, hecs_payment_option_code,
																	unit_student_status_code, unit_census_date )
					SELECT 'VFH enrolment but missing OR invalid Unit Student Status' AS error_type, vfh_unit_attempts.course_admin_team,
							vfh_unit_attempts.teaching_period, vfh_unit_attempts.student_id, vfh_unit_attempts.course_code,
							vfh_unit_attempts.unit_delivery_remoteness, vfh_unit_attempts.unit_code,
							vfh_unit_attempts.unit_delivery_location, vfh_unit_attempts.unit_funding_source, vfh_unit_attempts.grade,
							vfh_unit_attempts.administrative_unit_status, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
							vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code,
							vfh_unit_attempts.vfh_home_language_code, vfh_unit_attempts.vfh_term_location_postcode,
							vfh_unit_attempts.vfh_term_location_country_code, vfh_unit_attempts.vfh_home_location_postcode,
							vfh_unit_attempts.vfh_home_location_country_code, vfh_unit_attempts.vfh_arrival_year,
							vfh_unit_attempts.vfh_permanent_resident_code, vfh_unit_attempts.vfh_commencing_location_postcode,
							vfh_unit_attempts.vfh_commencing_geographic_location, vfh_unit_attempts.vfh_highest_attainment_code,
							vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
							vfh_unit_attempts.hecs_payment_option_code, vfh_unit_attempts.unit_student_status_code,
							vfh_unit_attempts.unit_census_date
					FROM vfh_unit_attempts
					LEFT JOIN xlookup_vfh_student_status
					ON vfh_unit_attempts.unit_student_status_code = xlookup_vfh_student_status.vfh_student_status_cd
					WHERE xlookup_vfh_student_status.vfh_student_status_cd IS NULL
					""")
		'''
		# q351 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code, chessn,
																	vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing OR invalid Citizenship Status' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
									vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code,
									vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code,
									vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code,
									vfh_unit_attempts.vfh_commencing_location_postcode, vfh_unit_attempts.vfh_commencing_geographic_location,
									vfh_unit_attempts.vfh_highest_attainment_code, vfh_unit_attempts.vfh_highest_attainment_year,
									vfh_unit_attempts.basis_for_admission_code, vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					LEFT JOIN xlookup_vfh_citizenship
					ON vfh_unit_attempts.vfh_citizenship_code = xlookup_vfh_citizenship.vfh_citizenship_cd
					WHERE xlookup_vfh_citizenship.vfh_citizenship_cd IS NULL
					OR vfh_unit_attempts.vfh_citizenship_code NOT IN ('1','8','2')
					""")
		'''
		# q352 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	chessn, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing OR invalid Birth Country Code' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
									vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code,
									vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code,
									vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code, vfh_unit_attempts.vfh_commencing_location_postcode,
									vfh_unit_attempts.vfh_commencing_geographic_location, vfh_unit_attempts.vfh_highest_attainment_code,
									vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
									vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					LEFT JOIN xlookup_vfh_birth_country
					ON vfh_unit_attempts.vfh_birth_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					WHERE xlookup_vfh_birth_country.vfh_birth_country_cd IS NULL
					""")
		'''
		# q353 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	chessn, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing OR invalid Highest Attainment Code' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
									vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code, vfh_unit_attempts.vfh_home_location_postcode,
									vfh_unit_attempts.vfh_home_location_country_code, vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code,
									vfh_unit_attempts.vfh_commencing_location_postcode, vfh_unit_attempts.vfh_commencing_geographic_location,
									vfh_unit_attempts.vfh_highest_attainment_code, vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
									vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					LEFT JOIN xlookup_vfh_highest_attainment
					ON vfh_unit_attempts.vfh_highest_attainment_code = xlookup_vfh_highest_attainment.vfh_highest_participation_cd
					WHERE xlookup_vfh_highest_attainment.vfh_highest_participation_cd IS NULL
					""")
		'''
		# q354 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	chessn, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year,
																	basis_for_admission_code, hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing OR invalid Highest Attainment Yr' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
									vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code, vfh_unit_attempts.vfh_home_location_postcode,
									vfh_unit_attempts.vfh_home_location_country_code, vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code,
									vfh_unit_attempts.vfh_commencing_location_postcode, vfh_unit_attempts.vfh_commencing_geographic_location,
									vfh_unit_attempts.vfh_highest_attainment_code, vfh_unit_attempts.vfh_highest_attainment_year,
									vfh_unit_attempts.basis_for_admission_code, vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					WHERE ((vfh_unit_attempts.vfh_highest_attainment_year NOT IN ('0000','9999')) And (vfh_unit_attempts.vfh_highest_attainment_year > '2018'))
					OR vfh_unit_attempts.vfh_highest_attainment_year IS NULL
					""")
		'''
		# q355 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code, vfh_atsi_code,
																	vfh_citizenship_code, vfh_birth_country_code, vfh_home_language_code,
																	vfh_term_location_postcode, vfh_term_location_country_code, vfh_home_location_postcode,
																	vfh_home_location_country_code, vfh_arrival_year, vfh_permanent_resident_code,
																	vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code )
					SELECT DISTINCT 'VFH enrolment but missing OR invalid ATSI Code' AS error_type, vfh_unit_attempts.course_admin_team,
									vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.vfh_atsi_code,
									vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code,
									vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code,
									vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code,
									vfh_unit_attempts.vfh_commencing_location_postcode, vfh_unit_attempts.vfh_commencing_geographic_location,
									vfh_unit_attempts.vfh_highest_attainment_code, vfh_unit_attempts.vfh_highest_attainment_year,
									vfh_unit_attempts.basis_for_admission_code, vfh_unit_attempts.hecs_payment_option_code
					FROM vfh_unit_attempts
					LEFT JOIN xlookup_vfh_atsi
					ON vfh_unit_attempts.vfh_atsi_code = xlookup_vfh_atsi.vfh_atsi_code
					WHERE xlookup_vfh_atsi.vfh_atsi_code IS NULL
					""")
		'''
		# q356 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, vet_stats_atsi, vfh_atsi_code, course_admin_team,
																	teaching_period, student_id, course_code, unit_delivery_remoteness,
																	unit_code, unit_delivery_location, unit_funding_source, grade,
																	administrative_unit_status, chessn, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode,
																	vfh_commencing_geographic_location, vfh_highest_attainment_code,
																	vfh_highest_attainment_year, basis_for_admission_code, hecs_payment_option_code,
																	unit_student_status_code, unit_census_date )
					SELECT 'VFH enrolment but conflicting ATSI Codes' AS error_type, vfh_unit_attempts.atsi,
							vfh_unit_attempts.vfh_atsi_code, vfh_unit_attempts.course_admin_team, vfh_unit_attempts.teaching_period,
							vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.unit_delivery_remoteness,
							vfh_unit_attempts.unit_code, vfh_unit_attempts.unit_delivery_location, vfh_unit_attempts.unit_funding_source,
							vfh_unit_attempts.grade, vfh_unit_attempts.administrative_unit_status, vfh_unit_attempts.chessn,
							vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code,
							vfh_unit_attempts.vfh_home_language_code, vfh_unit_attempts.vfh_term_location_postcode,
							vfh_unit_attempts.vfh_term_location_country_code, vfh_unit_attempts.vfh_home_location_postcode,
							vfh_unit_attempts.vfh_home_location_country_code, vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code,
							vfh_unit_attempts.vfh_commencing_location_postcode, vfh_unit_attempts.vfh_commencing_geographic_location,
							vfh_unit_attempts.vfh_highest_attainment_code, vfh_unit_attempts.vfh_highest_attainment_year,
							vfh_unit_attempts.basis_for_admission_code, vfh_unit_attempts.hecs_payment_option_code,
							vfh_unit_attempts.unit_student_status_code, vfh_unit_attempts.unit_census_date
					FROM vfh_unit_attempts
					WHERE (vfh_unit_attempts.atsi <> 'N' AND vfh_unit_attempts.vfh_atsi_code = '2')
					OR (vfh_unit_attempts.atsi = 'N' AND vfh_unit_attempts.vfh_atsi_code <> '2')
					""")
		'''
		# q357 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, teaching_period, course_admin_team, student_id, course_code,
																	unit_code, unit_delivery_location, unit_delivery_remoteness, unit_funding_source,
																	grade, administrative_unit_status, chessn, vfh_atsi_code, vfh_citizenship_code,
																	vfh_birth_country_code, vfh_home_language_code, vfh_term_location_postcode,
																	vfh_term_location_country_code, vfh_home_location_postcode, vfh_home_location_country_code,
																	vfh_arrival_year, vfh_permanent_resident_code, vfh_commencing_location_postcode,
																	vfh_commencing_geographic_location, vfh_highest_attainment_code, vfh_highest_attainment_year,
																	basis_for_admission_code, hecs_payment_option_code, unit_student_status_code,
																	enrol_date, unit_census_date )
					SELECT 'Unit enrolment date is after census' AS error_message, vfh_unit_attempts.teaching_period, vfh_unit_attempts.course_admin_team,
							vfh_unit_attempts.student_id, vfh_unit_attempts.course_code, vfh_unit_attempts.unit_code, vfh_unit_attempts.unit_delivery_location,
							vfh_unit_attempts.unit_delivery_remoteness, vfh_unit_attempts.unit_funding_source, vfh_unit_attempts.grade,
							vfh_unit_attempts.administrative_unit_status, vfh_unit_attempts.chessn, vfh_unit_attempts.vfh_atsi_code,
							vfh_unit_attempts.vfh_citizenship_code, vfh_unit_attempts.vfh_birth_country_code, vfh_unit_attempts.vfh_home_language_code,
							vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code,
							vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code,
							vfh_unit_attempts.vfh_arrival_year, vfh_unit_attempts.vfh_permanent_resident_code, vfh_unit_attempts.vfh_commencing_location_postcode,
							vfh_unit_attempts.vfh_commencing_geographic_location, vfh_unit_attempts.vfh_highest_attainment_code,
							vfh_unit_attempts.vfh_highest_attainment_year, vfh_unit_attempts.basis_for_admission_code,
							vfh_unit_attempts.hecs_payment_option_code, vfh_unit_attempts.unit_student_status_code, vfh_unit_attempts.enrol_date,
							vfh_unit_attempts.unit_census_date
					FROM vfh_unit_attempts
					WHERE vfh_unit_attempts.enrol_date > unit_census_date
					""")
		'''
		# q358 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	vfh_home_location_postcode, vfh_home_location_country_code )
					SELECT DISTINCT 'Both Home Location Postcode and Home Location Country Code in HE Stats cannot be null' AS error_message,
									vfh_unit_attempts.course_admin_team, vfh_unit_attempts.student_id, vfh_unit_attempts.course_code,
									vfh_unit_attempts.vfh_home_location_postcode, vfh_unit_attempts.vfh_home_location_country_code
					FROM vfh_unit_attempts
					WHERE (vfh_unit_attempts.vfh_home_location_postcode IS NULL
					AND vfh_unit_attempts.vfh_home_location_country_code IS NULL)
					OR vfh_unit_attempts.vfh_home_location_postcode='0000'
					""")
		'''
		# q359 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	vfh_term_location_postcode, vfh_term_location_country_code )
					SELECT DISTINCT 'Both Term Location Postcode and Term Location Country Code in HE Stats cannot be null' AS error_message,
									vfh_unit_attempts.course_admin_team, vfh_unit_attempts.student_id, vfh_unit_attempts.course_code,
									vfh_unit_attempts.vfh_term_location_postcode, vfh_unit_attempts.vfh_term_location_country_code
					FROM vfh_unit_attempts
					WHERE (vfh_unit_attempts.vfh_term_location_postcode IS NULL
					AND vfh_unit_attempts.vfh_term_location_country_code IS NULL)
					OR vfh_unit_attempts.vfh_term_location_postcode='0000'
					""")
		'''
		# q360 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, teaching_period, student_id,
																	unit_delivery_location, unit_funding_source, course_code,
																	unit_code, grade, administrative_unit_status, chessn,
																	vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode,
																	vfh_term_location_country_code, vfh_home_location_postcode,
																	vfh_home_location_country_code, vfh_arrival_year, vfh_permanent_resident_code,
																	vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year,
																	basis_for_admission_code, hecs_payment_option_code, unit_student_status_code,
																	unit_census_date )
					SELECT 'Unit has been Discontinued but has an RPL Grade' AS error_msg, course_admin_team, teaching_period, student_id, unit_delivery_location,
							unit_funding_source, course_code, unit_code, grade, administrative_unit_status, chessn, vfh_atsi_code,
							vfh_citizenship_code, vfh_birth_country_code, vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
							vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year, vfh_permanent_resident_code, vfh_commencing_location_postcode,
							vfh_commencing_geographic_location, vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
							hecs_payment_option_code, unit_student_status_code, unit_census_date
					FROM weekly_current
					WHERE weekly_current.teaching_period LIKE 'VFH%'
					AND weekly_current.grade = 'RPL'
					AND weekly_current.administrative_unit_status = 'WDN-EARLY'
					""")
		'''
		# q360a - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, teaching_period, student_id, course_admin_team,
																	unit_funding_source, course_code, fee_category, unit_code,
																	grade )
					SELECT 'VFH Fee Category but not a VFH Teaching Period' AS error_message, teaching_period, student_id,
							course_admin_team, unit_funding_source, course_code, fee_category, unit_code, grade
					FROM weekly_current
					WHERE weekly_current.teaching_period NOT LIKE 'VFH%'
					AND weekly_current.teaching_period NOT IN ('RPl','RPl-CAN','RPl-NOT','CRDT-TRANS')
					AND weekly_current.fee_category In ('VET-FFSHLP','VET-FHELP')
					AND weekly_current.grade <> 'SW'
					""")
		'''
		# q360b - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, teaching_period, course_admin_team, student_id, course_code,
																	unit_code, grade, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
																	vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
																	vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
																	vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
																	vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
																	hecs_payment_option_code, unit_student_status_code, unit_census_date )
					SELECT 'Enrolment appears to be a VFH enrolment but is not enrolled in a VFH Teaching Period. Please check.' AS error_message,
							teaching_period, course_admin_team, student_id, course_code, unit_code, grade, vfh_atsi_code,
							vfh_citizenship_code, vfh_birth_country_code, vfh_home_language_code, vfh_term_location_postcode,
							vfh_term_location_country_code, vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
							vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
							vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code, hecs_payment_option_code,
							unit_student_status_code, unit_census_date
					FROM weekly_current
					WHERE (weekly_current.teaching_period NOT LIKE 'VFH%'
					AND weekly_current.teaching_period <> 'CRDT-TRANS'
					AND weekly_current.grade IS NULL
					AND weekly_current.unit_student_status_code IS NOT NULL)
					OR (weekly_current.teaching_period NOT LIKE 'VFH%'
					AND weekly_current.teaching_period <> 'CRDT-TRANS'
					AND weekly_current.Grade NOT IN ('SW','W')
					AND weekly_current.unit_student_status_code IS NOT NULL)
					""")
		'''
		# q363 - tested OK
		'''
		cur.execute("""
					INSERT INTO error_vfh_enrolments_by_vet_teams ( error_type, course_admin_team, student_id, course_code,
																	vfh_birth_country_code, vfh_arrival_year )
					SELECT 'The VFH Birth Country Code and Arrival Years do not match' AS error_message, course_admin_team,
							student_id, course_code, vfh_birth_country_code, vfh_arrival_year
					FROM vfh_unit_attempts
					WHERE (vfh_unit_attempts.vfh_birth_country_code <> '1100'
					AND vfh_unit_attempts.vfh_arrival_year IN ('A999','0000','0001'))
					OR (vfh_unit_attempts.vfh_birth_country_code = '1100'
					AND vfh_unit_attempts.vfh_arrival_year NOT IN ('0001'))
					""")
		'''
		# q365 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, teaching_period, student_id,
																	course_code, unit_code, enrol_date, student_last_name, student_first_name, unit_funding_source,
																	residential_post_code, outcome, unit_attempt_status)
					SELECT 'Not an eligible TL course. Must be either Diploma or Advanced Diploma level.' AS error, weekly_current.course_admin_team,
							weekly_current.teaching_period, weekly_current.student_id, weekly_current.course_code, weekly_current.unit_code,
							weekly_current.enrol_date, weekly_current.student_last_name, weekly_current.student_first_name,
							weekly_current.unit_funding_source, weekly_current.residential_postcode, weekly_current.outcome,
							weekly_current.unit_attempt_status
					FROM weekly_current
					INNER JOIN xlookup_course
					ON weekly_current.course_code = xlookup_course.code
					WHERE weekly_current.unit_funding_source LIKE 'TL%'
					AND xlookup_course.Level NOT IN ('421','411')
					""")
		'''
		# q366 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, student_id, atsi,
																	student_last_name, student_first_name, gender, dob,
																	deceased_indicator, disability, home_language_code,
																	birth_country_code, residential_post_code, home_state, prior_education,
																	employment_category, at_school_indicator, vet_in_school_indicator,
																	highest_school_level_completed_code, highest_school_level_completed_year,
																	usi_flag)
					SELECT DISTINCT 'Student is missing a verified USI. Please correct.' AS error_message, course_admin_team,
									student_id, atsi, student_last_name, student_first_name, student_gender, student_dob,
									deceased_indicator, disability_flag, home_language_code, birth_country_code, residential_postcode,
									student_home_state, highest_prior_education_level_completed_code, employment_category,
									at_school_indicator, vet_in_school_indicator, highest_school_level_completed_code,
									highest_school_level_completed_year, usi_flag
					FROM weekly_current
					WHERE weekly_current.usi_flag = 'N'
					AND weekly_current.grade NOT IN ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED'
					""")
		'''
		# q367 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, student_id, course_code,
																	atsi, student_last_name, student_first_name, gender, dob,
																	deceased_indicator, disability, home_language_code,
																	birth_country_code, residential_post_code, home_state, prior_education,
																	employment_category, at_school_indicator, vet_in_school_indicator,
																	highest_school_level_completed_code, highest_school_level_completed_year,
																	entitlement_contract_description, unit_code,
																	unit_funding_source)
					SELECT DISTINCT 'Student is ETP and missing Entitlement Contract Description or vice versa. Please correct.' AS error_message,
									course_admin_team, student_id, course_code, atsi, student_last_name, student_first_name, student_gender,
									student_dob, deceased_indicator, disability_flag, home_language_code, birth_country_code, residential_postcode,
									student_home_state, highest_prior_education_level_completed_code, employment_category, at_school_indicator,
									vet_in_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year,
									entitlement_contract_description, unit_code, unit_funding_source
					FROM weekly_current
					WHERE (weekly_current.course_code <> 'LRNSUPP'
					AND weekly_current.entitlement_contract_description is not NULL
					AND weekly_current.unit_funding_source <> 'ETP'
					AND weekly_current.grade NOT in ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED')
					OR (weekly_current.course_code <> 'LRNSUPP'
					AND weekly_current.entitlement_contract_description is NULL
					AND weekly_current.unit_funding_source = 'ETP'
					AND weekly_current.grade NOT in ('SW','NS')
					AND weekly_current.unit_attempt_status<>'CANCELLED')
					""")
		'''
		# q368a - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, student_id, atsi,
																	student_last_name, student_first_name, gender, dob,
																	deceased_indicator, disability, home_language_code,
																	birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category, at_school_indicator,
																	vet_in_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, entitlement_contract_description,
																	course_code, unit_funding_source, course_commencement_date )
					SELECT DISTINCT 'ETP Course Commencement outside first contract start and end dates. Please check.' AS error_message,
									course_admin_team, student_id, atsi, student_last_name, student_first_name, student_gender, student_dob,
									deceased_indicator, disability_flag, home_language_code, birth_country_code, residential_postcode,
									student_home_state, highest_prior_education_level_completed_code, employment_category,
									at_school_indicator, vet_in_school_indicator, highest_school_level_completed_code,
									highest_school_level_completed_year, entitlement_contract_description, course_code, unit_funding_source,
									course_commencement_date
					FROM weekly_current
					WHERE (weekly_current.entitlement_contract_description = '2016-MOA-3'
					AND weekly_current.unit_funding_source = 'ETP'
					AND weekly_current.course_commencement_date < '2016-04-01'::date
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%'
					AND weekly_current.grade NOT IN ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED')
					OR (weekly_current.entitlement_contract_description = '2016-MOA-3'
					AND weekly_current.unit_funding_source = 'ETP'
					AND weekly_current.course_commencement_date > '2017-06-30'::date
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP'
					AND weekly_current.grade NOT IN ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED')
					""")
		'''
		# q368b - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, student_id, atsi,
																	student_last_name, student_first_name, gender, dob,
																	deceased_indicator, disability, home_language_code,
																	birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category, at_school_indicator,
																	vet_in_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, entitlement_contract_description,
																	unit_funding_source, course_commencement_date )
					SELECT DISTINCT 'ETP Course Commencement outside first contract start and end dates. Please check.' AS error_message,
									course_admin_team, student_id, atsi, student_last_name, student_first_name, student_gender,
									student_dob, deceased_indicator, disability_flag, home_language_code, birth_country_code,
									residential_postcode, student_home_state, highest_prior_education_level_completed_code,
									employment_category, at_school_indicator, vet_in_school_indicator, highest_school_level_completed_code,
									highest_school_level_completed_year, entitlement_contract_description, unit_funding_source,
									course_commencement_date
					FROM weekly_current
					WHERE (weekly_current.entitlement_contract_description = '2017-MOA-4'
					AND weekly_current.unit_funding_source = 'ETP'
					AND weekly_current.course_commencement_date < '2017-04-01'::date
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%'
					AND weekly_current.grade NOT IN ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED')
					OR (weekly_current.entitlement_contract_description = '2017-MOA-4'
					AND weekly_current.unit_funding_source = 'ETP'
					AND weekly_current.course_commencement_date > '2018-06-30'::date
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%'
					AND weekly_current.grade NOT IN ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED')
					""")
		'''
		# q370 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, course_admin_team, student_id, course_code,
																	atsi, student_last_name, student_first_name, gender, dob,
																	deceased_indicator, disability, home_language_code,
																	birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category, at_school_indicator,
																	vet_in_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, entitlement_contract_description,
																	unit_funding_source, course_commencement_date, course_attempt_status )
					SELECT DISTINCT 'ETP Course commencing this year but now LAPSED or DISCONTIN. Should this still be under ETP?' AS error_message,
									course_admin_team, student_id, course_code, atsi, student_last_name, student_first_name, student_gender,
									student_dob, deceased_indicator, disability_flag, home_language_code, birth_country_code, residential_postcode,
									student_home_state, highest_prior_education_level_completed_code, employment_category, at_school_indicator,
									vet_in_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year,
									entitlement_contract_description, unit_funding_source, course_commencement_date, course_attempt_status
					FROM weekly_current
					WHERE weekly_current.entitlement_contract_description IS NOT NULL
					AND weekly_current.unit_funding_source = 'ETP'
					AND weekly_current.course_commencement_date > '2018-01-01'::date
					AND weekly_current.course_attempt_status IN ('LAPSED','DISCONTIN')
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%'
					AND weekly_current.grade NOT IN ('SW','NS')
					AND weekly_current.unit_attempt_status <> 'CANCELLED'
					""")
		'''
		# q401a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = NULL, grade_keyed = 'N/A',
					unit_attempt_status = 'ASSESSING', unit_delivery_type = '90'
					WHERE teaching_period like 'VFH%'
					AND grade_keyed='N'
					AND unit_attempt_status='ENROLLED'
					AND unit_delivery_type='RPL'
					""")
		'''
		# q401b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'RPL-NOT', grade_keyed = 'N/A',
					unit_attempt_status = 'NOT-APPRVD', not_approved_date = enrolment_activity_end_date,
					unit_delivery_type = '90'
					WHERE (teaching_period like 'VFH%'
					AND grade_keyed = 'Y'
					AND unit_attempt_status = 'COMPLETED'
					AND unit_delivery_type = 'RPL'
					AND grade = 'RPL-N')
					OR (teaching_period like 'VFH%'
					AND grade_keyed = 'Y'
					AND unit_attempt_status = 'DISCONTIN'
					AND unit_delivery_type = 'RPL'
					AND grade = 'WW')
					""")
		'''
		# q401c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'RPL', grade_keyed = 'N/A', unit_attempt_status = 'GRANTED',
					granted_date = enrolment_activity_end_date, unit_delivery_type = '90'
					WHERE teaching_period like 'VFH%'
					AND grade_keyed='Y'
					AND unit_attempt_status='COMPLETED'
					AND unit_delivery_type='RPL'
					AND grade in ('RPL')
					""")
		'''
		# q401d - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'RPL-CAN', grade_keyed = 'N/A', unit_attempt_status = 'CANCELLED',
						cancelled_date = enrolment_activity_end_date, unit_delivery_type = '90'
					WHERE teaching_period like 'VFH*'
					AND grade_keyed='Y'
					AND unit_attempt_status='DISCONTIN'
					AND unit_delivery_type='RPL'
					AND grade In ('SW','W','NS')
					""")
		'''
		# q402 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET highest_school_level_completed_year = Right(highest_school_level_completed_year,4)
					WHERE highest_school_level_completed_year IS NOT NULL
					""")
		'''
		# q403 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET highest_school_level_completed_year = '@@@@'
					WHERE (highest_school_level_completed_year < '1918' OR highest_school_level_completed_year > '2018')
					AND highest_school_level_completed_year NOT LIKE '@@@@'
					OR (highest_school_level_completed_year NOT SIMILAR TO '[0-9]{1,4}' AND highest_school_level_completed_year NOT like '@@@@')
					OR highest_school_level_completed_year IS NULL
					""")
		'''
		# q404 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET highest_school_level_completed_code = '@@'
					WHERE highest_school_level_completed_code IS NULL
					""")
		'''
		# q405 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET home_language_code = '@@@@'
					WHERE home_language_code IS NULL
		 			""")
		'''
		# q406 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET birth_country_code = '@@@@'
					WHERE birth_country_code IS NULL
					""")
		'''
		# q407 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET residential_postcode = lpad(residential_postcode,4,'0')
					WHERE residential_postcode <> '@@@@'
					OR residential_postcode <> 'OSPC'
					""")
		'''
		# q407a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET residential_postcode = '@@@@'
					WHERE residential_postcode IS NULL
					OR residential_postcode=''
					""")
		'''
		# q407b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET postal_postcode = lpad(postal_postcode,4,'0')
					WHERE postal_postcode <> '@@@@'
					OR postal_postcode <> 'OSPC'
					""")
		'''
		# q407c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET postal_postcode = '@@@@'
					WHERE postal_postcode IS NULL
					OR postal_postcode=''
					""")
		'''
		# q408 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET disability_flag = '@'
					WHERE disability_flag IS NULL
					""")
		'''
		# q409 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET employment_category = '@@'
					WHERE employment_category IS NULL
					""")
		'''
		# q410 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET at_school_indicator = '@'
					WHERE at_school_indicator IS NULL
					""")
		'''
		# q411 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET student_home_state = 'UNK'
					WHERE student_home_state IS Null
					OR student_home_state = 'ADDRESS UNKNOWN'
					OR student_home_state = 'UNKNOWN'
					""")
		'''
		# q412 - tested NOT OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET unit_funding_source = 	(CASE
													WHEN unit_funding_source = '01J' THEN '11J'
													WHEN unit_funding_source = '01K' THEN '11K'
													WHEN unit_funding_source = '01N' THEN '11N'
													WHEN unit_funding_source = '01V' THEN '11V'
													WHEN unit_funding_source = '03A' THEN '20A'
													WHEN unit_funding_source = '03K' THEN '20K'
													WHEN unit_funding_source = '04A' THEN '30A'
													WHEN unit_funding_source = '11P' THEN '11V'
													WHEN unit_funding_source = '01B' THEN '11B'
													WHEN unit_funding_source = '02Z' THEN '13Z'
													WHEN course_code LIKE 'O%' THEN 'OFF'
													ELSE '01J'
												END)
					""")
		'''
		# q413a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'RPL'
					WHERE teaching_period IS NULL
					AND unit_attempt_status='ASSESSING'
					""")
		'''
		# q413b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'RPL-NOT'
					WHERE teaching_period IS NULL
					AND unit_attempt_status='NOT-APPRVD'
					""")
		'''
		# q413c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'RPL-CAN'
					WHERE weekly_current.teaching_period IS NULL
					AND weekly_current.unit_attempt_status = 'CANCELLED'
					""")
		'''
		# q413d - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period = 'CRDT-TRANS'
					WHERE weekly_current.teaching_period IS NULL
					""")
		'''
		# q414 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET grade = (CASE
									WHEN teaching_period = 'CRDT-TRANS' THEN 'CT'
									WHEN teaching_period IS NULL THEN 'CT'
									WHEN teaching_period = 'RPL-NOT' THEN 'RPL-NOT APPROVED'
									WHEN teaching_period = 'RPL' THEN 	(CASE 
																			WHEN unit_attempt_status='ASSESSING' THEN 'RPL-UR' 
																			ELSE 'RPL'
																		END)												
								END)
					""")
		'''
		# q415 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET outcome = 	(CASE
										WHEN grade IN ('IP', 'WW') THEN 'W'
										WHEN grade = 'CS' THEN 'CE'
										WHEN grade IN ('B','CA','CH','CM','CP','CU','D','HD','P','PC','PS','PT','PU','S') THEN 'C'
										WHEN grade IN ('CF','F','WF') THEN 'NC'
										ELSE grade
									END)
					""")
		'''
		# q416 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET age = EXTRACT(YEAR FROM AGE(student_dob::date))
					""")
		'''
		# q417 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET age = 	(CASE
									WHEN age IS NULL THEN 999
									ELSE age
								END)								
					""")
		'''
		# q418a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET result_date = granted_date
					WHERE (result_date IS NULL
					AND unit_attempt_status = 'GRANTED'
					AND teaching_period = 'CRDT-TRANS')
					OR (result_date IS NULL
					AND unit_attempt_status = 'GRANTED'
					AND teaching_period = 'RPL')
					""")
		'''
		# q418b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET result_date = not_approved_date
					WHERE (result_date IS NULL
					AND unit_attempt_status = 'NOT-APPRVD'
					AND teaching_period = 'RPL-NOT')

					OR (result_date IS NULL
					AND unit_attempt_status = 'NOT-APPRVD'
					AND teaching_period IS NULL)

					OR (result_date IS NULL
					AND unit_attempt_status = 'NOT-APPRVD'
					AND teaching_period = 'CRDT-TRANS')
					""")
		'''
		# q418c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET result_date = cancelled_date
					WHERE (result_date IS NULL
					AND unit_attempt_status = 'CANCELLED'
					AND teaching_period IS NULL)
					OR (result_date IS NULL
					AND unit_attempt_status = 'CANCELLED'
					AND teaching_period = 'RPL-CAN')
					OR (result_date IS NULL
					AND unit_attempt_status = 'CANCELLED'
					AND teaching_period = 'CRDT-TRANS')
					""")
		'''
		# q419a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET enrol_date = override_activity_start_date
					WHERE enrol_date IS NULL
					AND override_activity_start_date IS NOT NULL
					""")
		'''
		# q419b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET enrol_date = granted_date
					WHERE enrol_date Is NULL
					AND granted_date is not NULL
					AND override_activity_start_date is NULL
					""")
		'''
		# q419c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET enrol_date = cancelled_date
					WHERE enrol_date is NULL
					AND granted_date is NULL
					AND override_activity_start_date is NULL
					AND cancelled_date is not NULL
		 			""")
		'''
		# q419d - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET enrol_date = not_approved_date
					WHERE enrol_date is NULL
					AND granted_date is NULL
					AND override_activity_start_date is NULL
					AND not_approved_date is not NULL
					""")
		'''
		# q419e - tested NOT OK - syntax issues
		'''
		cur.execute("""
					UPDATE WEEKLY_CURRENT
					SET enrol_week = 	(CASE
											WHEN enrol_date IS NULL THEN '0'
											WHEN EXTRACT(YEAR FROM enrol_date) < 2018 THEN '0'
											WHEN EXTRACT(YEAR FROM enrol_date) > 2018 THEN '53'
											ELSE (EXTRACT(DAY FROM enrol_date - '2018-01-01'::timestamp)/7)::int
										END),
						result_week = 	(CASE
											WHEN enrol_date IS NULL THEN '0'
											WHEN EXTRACT(YEAR FROM result_date) < 2018 THEN '0'
											WHEN EXTRACT(YEAR FROM result_date) > 2018 THEN '53'
											ELSE (EXTRACT(DAY FROM result_date - '2018-01-01'::timestamp)/7)::int
										END)
					""")
		'''
		# q420 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET course_admin_team = delivery_location_team
					WHERE course_admin_team SIMILAR TO '[a-z]*'
					AND delivery_location_team IS NOT NULL
					""")
		'''
		# q421 - tested OK
		'''
		cur.execute("""
					DELETE FROM weekly_2017
					WHERE teaching_period='CRDT-TRANS'
					OR teaching_period='RPL'
					OR teaching_period='RPL-NOT'
					OR teaching_period='RPL-CAN'
					OR teaching_period is NULL
					""")
		'''
		# q422 - tested NOT OK
		'''
		cur.execute("""
					UPDATE weekly_2017
					SET grade = 'UR'
					WHERE grade is NULL
					""")
		'''
		# q423 - tested NOT OK - needs more testing
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = xlookup_team.description
					FROM xlookup_team
					WHERE weekly_current.course_admin_team = xlookup_team.code

					""")
		'''
		# q425 - tested NOT OK - needs additional testing due to incorrect q412 results
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_course_unit_code = xlookup_target.contract_course_unit,
						contract_course_unit_name = xlookup_course.description_reference,
						contract = 'RA/NOV TARGET'
					FROM xlookup_target, xlookup_course
					WHERE xlookup_target.contract_course_unit = xlookup_course.code_reference
					AND weekly_current.course_code = xlookup_course.code
					AND weekly_current.unit_funding_source = xlookup_target.funding
					AND weekly_current.unit_delivery_location = xlookup_target.location
					AND (weekly_current.unit_funding_source='11N'
					OR weekly_current.unit_funding_source='11V'
					OR weekly_current.unit_funding_source='11H')
					""")
		'''
		# q426 - tested NOT OK - needs additional testing due to incorrect q412 results
		'''
		cur.execute("""
					UPDATE xlookup_location
					SET weekly_current.contract_course_unit_code = xlookup_target.contract_course_Unit,
					weekly_current.contract_course_unit_name = xlookup_course.description_reference,
					weekly_current.contract = 'RA/NOV TARGET'
					FROM (weekly_current
									INNER JOIN (xlookup_target
													INNER JOIN xlookup_course
													ON xlookup_target.contract_course_unit = xlookup_course.code_reference)
									ON weekly_current.course_code = xlookup_course.code
									AND weekly_current.unit_funding_source = xlookup_target.funding)
					WHERE (xlookup_LOCATION.Code = WEEKLY_CURRENT.[Unit Delivery Location])
					AND (xlookup_LOCATION.Remoteness = xlookup_TARGET.Remoteness)	
					AND (((WEEKLY_CURRENT.[Unit Funding Source])<>"11N"
					And (WEEKLY_CURRENT.[Unit Funding Source])<>"11V"
					And (WEEKLY_CURRENT.[Unit Funding Source])<>"11H"))
					""")
		'''
		# q427 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_course_unit_code = xlookup_course.code_reference,
						contract_course_unit_name = xlookup_course.description_reference,
						contract = 'NO TARGET'
					FROM xlookup_team, xlookup_course
					WHERE weekly_current.course_code = TRIM(xlookup_course.code)
					AND weekly_current.course_admin_team = TRIM(xlookup_team.code)
					AND weekly_current.contract IS NULL
					""")
		'''
		# q428 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET course_admin_team = xlookup_team.code,
					delivery_location_team = xlookup_team.code
					FROM xlookup_team
					WHERE weekly_current.contract_team = xlookup_TEAM.Description
					AND weekly_current.course_admin_team SIMILAR TO '[a-z]*'
					AND weekly_current.delivery_location_team IS NULL
					""")
		'''
		# q429 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET contract_team = '@@@ UNKNOWN TEAM', course_admin_team = '@@@'
					WHERE contract_team is NULL
					""")
		'''
		# q430 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_2017
					SET contract_team = TRIM(xlookup_team.description)
					FROM xlookup_team
					WHERE weekly_2017.course_admin_team = TRIM(xlookup_team.code)
					""")
		'''
		# q431 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET unit_delivery_type = 'RPLCT'
					WHERE teaching_period = 'RPL'
					OR teaching_period = 'CRDT-TRANS'
					OR teaching_period = 'RPL-NOT'
					OR teaching_period = 'RPL-CAN'
					OR teaching_period is NULL
					""")
		'''
		# q432 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET course_industry = '@@'
					WHERE course_industry is NULL
					""")
		'''
		# q433 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET study_reason = '@@'
					WHERE study_reason is NULL
					""")
		'''
		# q434 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_2017_comp_or_ur_ce_2018_reenrolled_douglas_to_check ( 	delivery_location_team_2018,
																								student_id, student_first_name,
																								student_last_name, course_code_2017,
																								grade_2017, weekly_2017_unit_code,
																								weekly_2017_unit_funding_source,
																								course_code_2018, grade_2018,
																								weekly_current_unit_funding_source,
																								weekly_current_unit_code )
					SELECT 	weekly_current.delivery_location_team AS delivery_location_team_2018, weekly_current.student_id,
							weekly_current.student_first_name, weekly_current.student_last_name,
							weekly_2017.course_code AS course_code_2017, weekly_2017.grade AS Grade_2017,
							weekly_2017.unit_code, weekly_2017.unit_funding_source, weekly_current.course_code AS course_code_2018,
							weekly_current.grade AS grade_2018, weekly_current.unit_funding_source, weekly_current.unit_code
					FROM weekly_2017
					INNER JOIN weekly_current
					ON weekly_2017.unit_code = weekly_current.unit_code
					AND weekly_2017.student_id = weekly_current.student_id
					WHERE (weekly_2017.grade IN ('UR','CE','OWA')
					AND weekly_current.Grade NOT IN ('SW','NS')
					AND weekly_current.unit_census_date IS NULL
					AND weekly_2017.unit_census_date IS NULL)
					OR (weekly_2017.course_code = 'LRNSUPP'
					AND weekly_current.course_code <> 'LRNSUPP')
					OR (weekly_2017.grade IN ('UR')
					AND weekly_current.grade NOT IN ('RPL')
					AND weekly_current.unit_census_date IS NOT NULL
					AND weekly_2017.unit_census_date IS NOT NULL
					AND weekly_current.teaching_period <> 'RPL'
					AND weekly_2017.teaching_period LIKE 'VFH%')
					""")
		'''
		# q435 - tested NOT OK - dependent on q412
		'''
		cur.execute("""
					SELECT DISTINCT teaching_period, delivery_location_team, unit_delivery_location, xlookup_location.remoteness,
									student_id, vet_school_name, course_code, unit_funding_source, fee_category,
									correspondence_category, vet_in_school_indicator, at_school_indicator, staff_indicator,
									postal_postcode, student_home_state
					INTO errors_inconsistent_fees_and_funding_sources_douglas
					FROM weekly_current
					INNER JOIN xlookup_location
					ON weekly_current.unit_delivery_location = xlookup_location.code
					WHERE weekly_current.course_code = 'LRNSUPP'
					AND weekly_current.fee_category = 'DOM-VET'
					OR (weekly_current.unit_funding_source = '30A'
					AND weekly_current.fee_category NOT LIKE 'INTL%')
					OR (weekly_current.unit_funding_source IN ('11J','11K','ETJ','ETK')
					AND weekly_current.fee_category NOT IN ('DOM-VET','VET-NOFEE','VET-FHELP'))
					OR (weekly_current.vet_school_name IS NOT NULL
					AND weekly_current.unit_funding_source IN ('11N','11V','11H')
					AND weekly_current.fee_category <> 'DOM-VET')
					OR (weekly_current.delivery_location_team IN ('110','109')
					AND weekly_current.unit_funding_source = '50S'
					AND weekly_current.fee_category NOT IN ('VET-APP-SA'))
					OR (weekly_current.unit_funding_source = '11C'
					AND weekly_current.fee_category <> 'VET-CTRACT')
					OR (weekly_current.unit_funding_source = '20K'
					AND weekly_current.fee_category NOT IN ('VET-FFEE','VET-FFS-FL','VET-CTRACT','VET-MANUAL','VET-FF-01','VET-FF-02','VET-FF-03','VET-FFSHLP'))
					OR (weekly_current.course_code IN ('TAE40110','AUR31112','AUR31212','AUR30612','AUR30312')
					AND weekly_current.unit_funding_source = '20A'
					AND weekly_current.unit_funding_source = '20A'
					AND weekly_current.fee_category NOT IN ('VET-FFSHLP','VET-FFEE','VET-FFS-FL','VET-CTRACT','VET-MANUAL','VET-FF-01','VET-FF-02','VET-FF-03')
					AND weekly_current.fee_category = 'VET-NOFEE'
					AND weekly_current.staff_indicator <> 'Y')
					OR (weekly_current.unit_funding_source IN ('11B','11S','13Z')
					AND weekly_current.fee_category <> 'VET-NOFEE')
					OR (weekly_current.unit_funding_source = 'LMR'
					AND weekly_current.fee_category <> 'VET-NOFEE')
					""")
		'''
		# q436 - tested NOT OK - dependent on q412
		'''
		cur.execute("""
					INSERT INTO errors_inconsistent_fees_and_funding_sources_douglas ( 	teaching_period, delivery_location_team,
																						unit_delivery_location, remoteness, student_id,
																						vet_school_name, course_code, unit_funding_source,
																						fee_category, correspondence_category, vet_in_school_indicator,
																						at_school_indicator, staff_indicator, postal_postcode,
																						student_home_state )
					SELECT DISTINCT teaching_period, delivery_location_team, unit_delivery_location, xlookup_location.remoteness,
									student_id, vet_school_name, course_code, unit_funding_source, fee_category, correspondence_category,
									vet_in_school_indicator, at_school_indicator, staff_indicator, postal_postcode, student_home_state
					FROM weekly_current
					INNER JOIN xlookup_location
					ON weekly_current.unit_delivery_location = xlookup_location.code
					WHERE (weekly_current.delivery_location_team NOT IN ('110','109')
					AND weekly_current.unit_funding_source = '20K'
					AND weekly_current.fee_category = 'VET-Manual')

					OR (weekly_current.unit_delivery_location = 'DON'
					AND weekly_current.vet_school_name IS NOT NULL
					AND weekly_current.unit_funding_source <> '11H'
					AND weekly_current.fee_category = 'DOM-VET')

					OR (weekly_current.fee_category NOT IN ('VET-FFEE','VET-FF-01','VET-FF-02','VET-FF-03','VET-MANUAL','VET-FFS-FL','VET-CTRACT','VET-APP-SA','VET-NOFEE','VET-FFSHLP')
					AND weekly_current.fee_category NOT LIKE 'INTL%'
					AND weekly_current.postal_postcode NOT LIKE '08%'
					AND weekly_current.postal_postcode NOT LIKE '09%'
					AND weekly_current.postal_postcode NOT IN ('@@@@','0000','OSPC'))

					OR weekly_current.unit_funding_source IN ('11D','11E','11L','11P','11Q','11U','13E','11M','50W','80A')

					OR (weekly_current.delivery_location_team IN ('325','327')
					AND weekly_current.unit_funding_source = '20A'
					AND weekly_current.fee_category = 'VET-FFS-FL'
					AND weekly_current.postal_postcode LIKE '08%'
					AND weekly_current.postal_postcode LIKE '09%'
					AND weekly_current.postal_postcode IN ('@@@@','0000','OSPC')
					AND weekly_current.unit_code <> 'SITHFAB009A')

					OR (weekly_current.delivery_location_team = '219'
					AND weekly_current.delivery_location_team = '217'
					AND weekly_current.delivery_location_team <> '028'
					AND xlookup_location.remoteness <> 'Remote'
					AND weekly_current.course_code NOT IN ('LRNSUPP','CHC30402','CHC30708','CHC50908','CHC50302')
					AND weekly_current.course_code NOT IN ('LRNSUPP','CHC40302','CHC40308','CHC30102','CHC30208')
					AND weekly_current.unit_funding_source IN ('11J','11K','11C','ETJ','ETK')
					AND weekly_current.unit_funding_source IN ('11J','11K','ETJ','ETK')
					AND weekly_current.unit_funding_source IN ('11K','ETK')
					AND weekly_current.unit_funding_source = '20A'
					AND weekly_current.fee_category = 'VET-NOFEE'
					AND weekly_current.fee_category = 'VET-NOFEE'
					AND weekly_current.fee_category ='VET-NOFEE'
					AND weekly_current.fee_category = 'VET-NOFEE'
					AND weekly_current.at_school_indicator <> 'VET-SCHOOL')

					OR (weekly_current.course_code = 'VTP173'
					AND weekly_current.unit_funding_source = '11W'
					AND weekly_current.unit_funding_source = '11W'
					AND weekly_current.fee_category <> 'DOM-VET'
					AND weekly_current.fee_category <> 'VET-NOFEE')

					OR (weekly_current.unit_delivery_location = 'DON'
					AND weekly_current.vet_school_name IS NOT NULL
					AND weekly_current.unit_funding_source = '11H'
					AND weekly_current.fee_category <> 'DOM-VET')

					OR (weekly_current.teaching_period LIKE 'VFH%'
					AND weekly_current.unit_funding_source NOT IN ('11J','11K','ETJ','ETK','LMT','TLS','TL0','ETP')
					AND weekly_current.fee_category = 'VET-FHELP')

					OR (weekly_current.unit_funding_source IN ('TLS','LMT')
					AND weekly_current.fee_category NOT IN ('VET-FHELP','VET-FFEE'))

					OR (weekly_current.teaching_period LIKE 'VFH%'
					AND weekly_current.fee_category NOT IN ('VET-FHELP','VET-FFSHLP'))

					OR (weekly_current.teaching_period NOT LIKE 'VFH%'
					AND weekly_current.teaching_period NOT IN ('CRDT-TRANS','RPL')
					AND weekly_current.fee_category IN ('VET-FHELP','VET-FFSHLP'))
					""")
		'''
		# q437 - tested NOT OK - dependent on q412
		'''
		cur.execute("""
					SELECT DISTINCT delivery_location_team, student_id, course_code, course_attempt_status, fee_category,
									unit_funding_source, tci AS current_tci, aci AS current_aci, '' AS previous_tci_code,
									'' AS previous_tci_start_dte, '' AS previous_tci_end_dte
					INTO errors_k_no_current_or_missing_aci_tci_margaret_to_check
					FROM weekly_current
					WHERE (weekly_current.course_code <> 'LRNSUPP'
					AND weekly_current.unit_funding_source Like '%K'
					AND weekly_current.tci IS NULL
					AND weekly_current.unit_delivery_location <> 'ADE')

					OR (weekly_current.course_code <> 'LRNSUPP'
					AND weekly_current.unit_funding_source Like '%K'
					AND weekly_current.aci IS NULL
					AND weekly_current.unit_delivery_location <> 'ADE')
					
					ORDER BY weekly_current.student_id
					""")
		'''
		# q438 - tested NOT OK - dependent on q412
		'''
		cur.execute("""
					UPDATE errors_k_no_current_or_missing_aci_tci_margaret_to_check
					SET previous_tci_code = api_id,
						previous_tci_start_dte = api_start_date,
						previous_tci_end_dte = api_end_date;
					FROM vet_apprentice
					WHERE errors_k_no_current_or_missing_aci_tci_margaret_to_check.course_code = vet_apprentice.course_code
					AND errors_k_no_current_or_missing_aci_tci_margaret_to_check.student_id = vet_apprentice.person_id
					""")
		'''
		# q439 - tested NOT OK - dependent on q412
		'''
		cur.execute("""
					SELECT DISTINCT delivery_location_team, student_id, course_code, fee_category, unit_funding_source, aci, tci
					INTO errors_aci_tci_not_k_margaret_to_check
					FROM weekly_current
					WHERE (weekly_current.delivery_location_team <> 'ADE'
					AND weekly_current.unit_funding_source NOT LIKE '%K'
					AND weekly_current.aci IS NOT NULL)
					OR (weekly_current.delivery_location_team <> 'ADE'
					AND weekly_current.unit_funding_source NOT LIKE '%K'
					AND weekly_current.tci IS NOT NULL)
					""")
		'''
		# q440 - tested NOT OK - returned NULL which is not correct
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'LRNSUPP Student with At School Flag Y. Please confirm if they are still at school' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE at_school_indicator = 'Y'
					AND course_code = 'LRNSUPP'
					AND outcome <> 'SW'
					""")
		'''
		# q441 - tested NOT OK - dependent on q412
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'VETIS funding code but VETIS Flag N' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason
					FROM weekly_current
					WHERE weekly_current.vet_in_school_indicator = 'N'
					AND weekly_current.unit_funding_source IN ('11N','11H','11V')
					""")
		'''
		# q442 - tested OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'At School Flag N but VETIS Flag Y' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason					
					FROM weekly_current
					WHERE weekly_current.vet_in_school_indicator = 'Y'
					AND weekly_current.at_school_indicator = 'N'
					""")
		'''
		# q443 - tested NOT OK
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, delivery_location_team, teaching_period, student_id, student_last_name,
																	student_first_name, deceased_indicator, atsi, vet_in_school_indicator, gender, dob,
																	disability, home_language_code, birth_country_code, residential_post_code, home_state,
																	prior_education, employment_category,at_school_indicator, highest_school_level_completed_code,
																	highest_school_level_completed_year, course_code, unit_code, unit_funding_source, enrol_date,
																	outcome, study_reason)
					SELECT 'Invalid Residential Postcode. Cannot have a post box postcode' AS error_message, delivery_Location_team, teaching_period, student_id, student_last_name,
							student_first_name, deceased_indicator, atsi, vet_in_school_indicator, student_gender, student_dob, disability_flag, home_language_code,
							birth_country_code, residential_postcode, student_home_state, highest_prior_education_level_completed_code, employment_category,
							at_school_indicator, highest_school_level_completed_code, highest_school_level_completed_year, course_code, unit_code, unit_funding_source,
							enrol_date, outcome, study_reason					
					FROM weekly_current
					WHERE weekly_current.residential_postcode in ('0801','0804','0811','0813','0814','0815','0821','0831','0851','0861','0871','0881','3552')
					""")
		'''
		# q444 - tested OK - could use some additional testing
		'''
		cur.execute("""
					UPDATE weekly_current
					SET teaching_period_end_date = 	(CASE
														WHEN teaching_period='TERM-1' THEN to_date('2018-03-31', 'YYYY-MM-DD')
														WHEN teaching_period='TERM-2' THEN to_date('2018-06-30', 'YYYY-MM-DD')
														WHEN teaching_period='TERM-3' THEN to_date('2018-09-30', 'YYYY-MM-DD')
														WHEN teaching_period='TERM-4' THEN to_date('2018-12-31', 'YYYY-MM-DD')
														WHEN teaching_period='VFH-T1' THEN to_date('2018-03-31', 'YYYY-MM-DD')
														WHEN teaching_period='VFH-T2' THEN to_date('2018-06-30', 'YYYY-MM-DD')
														WHEN teaching_period='VFH-T3' THEN to_date('2018-09-30', 'YYYY-MM-DD')
													END)
					""")
		'''
		# q445a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET enrolment_activity_end_date = 	(CASE
															WHEN teaching_period in ('TERM-1', 'VFH-T1') THEN to_date('2018-03-31', 'YYYY-MM-DD')
															WHEN teaching_period in ('TERM-2', 'VFH-T2') THEN to_date('2018-06-30', 'YYYY-MM-DD')
															WHEN teaching_period in ('TERM-3', 'VFH-T3') THEN to_date('2018-09-30', 'YYYY-MM-DD')
															WHEN teaching_period in ('TERM-4', 'VFH-T4') THEN to_date('2018-12-31', 'YYYY-MM-DD')
														END)
					WHERE weekly_current.enrolment_activity_end_date is NULL
					""")
		'''
		# q445b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET enrolment_activity_end_date = 	(CASE
															WHEN (teaching_period in ('CRDT-TRANS', 'RPL') AND granted_date IS NOT NULL) THEN granted_date
															WHEN teaching_period = 'RPL-NOT' THEN not_approved_date
															WHEN teaching_period = 'RPL-CAN' THEN cancelled_date
															ELSE NULL
														END)																		
					WHERE weekly_current.enrolment_activity_end_date is NULL
					AND weekly_current.unit_attempt_status in ('NOT-APPRVD','CANCELLED','GRANTED')
					""")
		'''
		# q446a - tested NOT OK - the select statement returns only NULL (sometime wring with this)
		'''
		cur.execute("""
					UPDATE weekly_current
					SET ur_outcome = 	(CASE
											WHEN (now()::date - enrolment_activity_end_date::date) <= 28 THEN 'UR'
											WHEN (now()::date - enrolment_activity_end_date::date) > 28 THEN 'NA'
											ELSE NULL
										END)
					WHERE outcome='UR'
					""")
		'''
		# q446b - tested NOT OK - the select statement returns only NULL (sometime wring with this)
		'''
		cur.execute("""
					UPDATE weekly_current
					SET ur_outcome = 	(CASE
											WHEN (now()::date - override_activity_start_date::date)<=90 THEN 'RPL-UR'
											WHEN (now()::date - override_activity_start_date::date)>90 THEN 'NA'
											ELSE NULL
										END)
					WHERE (weekly_current.outcome='RPL'
					AND weekly_current.unit_attempt_status='ASSESSING')
					OR (weekly_current.outcome='RPL-UR'
					AND weekly_current.unit_attempt_status='ASSESSING')
					""")
		'''
		# q447 - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET sca_funding_source = unit_funding_source
					WHERE teaching_period in ('RPL','RPL-NOT','RPL-CAN','CRDT-TRANS')
					""")
		'''
		# q449a - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET cancelled_date = NULL, granted_date = NULL
					WHERE (cancelled_date is not NULL
					AND unit_attempt_status='NOT-APPRVD')
					OR (granted_date is not NULL
					AND unit_attempt_status='NOT-APPRVD')
					""")
		'''
		# q449b - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET not_approved_date = NULL, granted_date = NULL
					WHERE (not_approved_date is not NULL
					AND unit_attempt_status='CANCELLED')
					OR (granted_date is not NULL
					AND unit_attempt_status='CANCELLED')
					""")
		'''
		# q449c - tested OK
		'''
		cur.execute("""
					UPDATE weekly_current
					SET not_approved_date = NULL, cancelled_date = NULL
					WHERE (not_approved_Date is not NULL
					AND unit_attempt_status='GRANTED')
					OR (cancelled_date is not NULL
					AND unit_attempt_status='GRANTED')
					""")
		'''
		# q450 - tested NOT OK - returning additional lines that will need to be checked
		'''
		cur.execute("""
					SELECT *
					INTO q450_weekly_current_exc_sw_ct_ns
					FROM weekly_current
					WHERE (weekly_current.grade NOT IN ('SW','NS','RPL-CA')
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%')
					OR (weekly_current.grade IS NULL
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%')
					OR (weekly_current.grade = ''
					AND weekly_current.unit_code NOT LIKE 'LRNSUPP%')
					""")
		'''
		# q450a - tested NOT OK - not implemented properly
		'''
		cur.execute("""
					SELECT 	delivery_location_team, student_id, unit_code, unit_attempt_status, teaching_period,
							grade, enrol_date, override_activity_start_date, result_date, enrolment_activity_end_date,
							course_code, unit_funding_source
					INTO errors_sua_duplicates_exc_sw_ct_ns_douglas_to_check
					FROM q450_weekly_current_exc_sw_ct_ns
					WHERE q450_weekly_current_exc_sw_ct_ns.student_id IN 	(
																			SELECT student_id
																			FROM q450_weekly_current_exc_sw_ct_ns AS tmp
																			GROUP BY student_id, unit_code HAVING Count(*) > 1 
																			AND unit_code = q450_weekly_current_exc_sw_ct_ns.unit_code
																			)
					ORDER BY q450_weekly_current_exc_sw_ct_ns.student_id,
					q450_weekly_current_exc_sw_ct_ns.unit_code,
					q450_weekly_current_exc_sw_ct_ns.enrol_date
					""")
		'''
		# q450b - tested NOT OK
		'''
		cur.execute("""
					SELECT 	delivery_location_team, student_id, unit_code, unit_attempt_status, teaching_period, grade,
							enrol_date, override_activity_start_date, result_date, enrolment_activity_end_date, course_code,
							unit_funding_source
					INTO errors_sua_result_before_start_dt_exc_sw_ct_ns_douglas
					FROM q450_weekly_current_exc_sw_ct_ns
					WHERE q450_weekly_current_exc_sw_ct_ns.grade NOT IN ('CE','OWA')
					AND q450_weekly_current_exc_sw_ct_ns.result_date < override_activity_start_date
					ORDER BY q450_weekly_current_exc_sw_ct_ns.student_id,
					q450_weekly_current_exc_sw_ct_ns.unit_code,
					q450_weekly_current_exc_sw_ct_ns.enrol_date
					""")
		'''
		# q451a - tested NOT OK
		'''
		cur.execute("""
					SELECT 	student_id, course_code, unit_code, xlookup_ntis_superseded_unit.identifier,
							xlookup_ntis_superseded_unit.superseding_identifier, xlookup_ntis_superseded_unit.description,
							override_activity_start_date, result_date, override_activity_end_date,
							course_admin_team, teaching_period, grade
					FROM weekly_current
					INNER JOIN xlookup_ntis_superseded_unit
					ON weekly_current.unit_code = xlookup_ntis_superseded_unit.identifier
					WHERE xlookup_ntis_superseded_unit.superseding_identifier IS NOT NULL
					AND xlookup_ntis_superseded_unit.description = 'CURRENT'
					ORDER BY weekly_current.student_id
					""")
		'''
		# q451b - tested NOT OK (query will not work because the q451a table needs to be created)
		'''
		cur.execute("""
					SELECT 	course_admin_team, student_id, unit_code, q451a_superseded_units.unit_code_as_related_unit,
							course_code, override_activity_start_date, result_date, override_activity_end_date,
							grade, teaching_period, q451a_superseded_units.description_as_unit_code_description
					INTO errors_superseded_units_douglas
					FROM weekly_current
					INNER JOIN q451a_superseded_units
					ON weekly_current.unit_code = q451a_superseded_units.superseding_identifier
					AND weekly_current.student_id = q451a_superseded_units.student_id
					ORDER BY weekly_current.student_id,
					weekly_current.unit_code
					""")
		'''
		# q451c - tested NOT OK (query will not work because the q451a table needs to be created)
		'''
		cur.execute("""
					INSERT INTO errors_superseded_units_douglas (	course_admin_team, student_id, course_code, unit_code,
																	related_unit, override_activity_start_date, result_date,
																	override_activity_end_date, grade, teaching_period,
																	unit_code_description )
					SELECT 	course_admin_team, student_id, course_code, qunit code, superseding_identifier, override_activity_start_date,
							result_date, override_activity_end_date, grade, teaching_period, "superseded" as description
					FROM q451a_superseded_units
					INNER JOIN errors_superseded_units_douglas
					ON q451a_superseded_units.student_id = errors_superseded_units_douglas.student_id
					AND q451a_superseded_units.superseding_identifier = errors_superseded_units_douglas.unit_code
					ORDER BY q451a_superseded_units.student_id, q451a_superseded_units.unit_code
					""")
		'''
		# q460 - tested NOT OK - not implemented properly
		'''
		cur.execute("""
					SELECT 	course_admin_team, student_id, student_first_name, student_last_name, course_code, unit_code, teaching_period,
							grade, enrolment_activity_end_date, cancelled_date, granted_date, result_date, disc_date, unit_census_date
					INTO error_possible_act_end_dt_errors_douglas
					FROM weekly_current
					WHERE (weekly_current.result_date >= '1/1/2019'::date Or weekly_current.result_date < '1/1/2018'::date)
					OR (weekly_current.grade NOT IN ('CE','OWA') AND weekly_current.grade NOT LIKE 'RPL%')
					AND (weekly_current.enrolment activity end date >= '1/1/2019'::date OR weekly_current.enrolment activity end date < '1/1/2018'::date)
					""")
		'''
		# q461 - tested NOT OK - not implemented properly (incorrect syntax)
		'''
		cur.execute("""
					SELECT course_admin_team, student_id, course_code, unit_code, teaching_period, enrol_date, override_activity_start_date, unit_census_date
					INTO error_possible_act_st_dt_errors_douglas
					FROM weekly_current
					WHERE (weekly_current.teaching_period NOT IN ('RPL','RPL-CAN','RPL-NOT','CRDT-TRANS')
					AND weekly_current.override activity_start_date < '1/1/2018'::date Or override_activity_start_date > '12/31/2018'::date)
					OR ((weekly_current.Teaching Period NOT LIKE "VFH*" And weekly_current.teaching_period NOT IN ('RPL','RPL-CAN','RPL-NOT','CRDT-TRANS')
					AND (weekly_current.override activity start date < '1/1/2018'::date Or weekly_current.override activity_start_date >'12/31/2018'::date)
					AND Year(override_activity_start_date) = Year(unit census date))
					""")
		'''
		# q501 - tested NOT OK - returned different results (query may need altering)
		'''
		cur.execute("""
					INSERT INTO student ( student_id, student_first_name, student_last_name, atsi, highest_prior_education_level_completed,
										  student_gender, student_home_state, deceased_indicator, language, country_of_birth,
										  highest_school_level_completed, highest_school_level_completed_year, residential_postcode,
										  employment_category, disability_flag, age, age_range, postal_postcode, chessn, vfh_atsi_code,
										  vfh_citizenship_code, vfh_birth_country_code, vfh_home_language_code, vfh_term_location_postcode,
										  vfh_term_location_country_code, vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
										  vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_commencing_geographic_location,
										  vfh_highest_attainment_code, vfh_highest_attainment_year, usi_flag, dob, email_address, mobile_phone_number )
					SELECT DISTINCT weekly_current.student_id, weekly_current.student_first_name, weekly_current.student_last_name, weekly_current.ATSI,
									xlookup_prior_education_level.description, weekly_current.student_gender, weekly_current.student_home_state,
									weekly_current.deceased_indicator, xlookup_language.full_name AS language,
									xlookup_country.full_name AS country_of_birth, xlookup_school_level.school_level_description,
									weekly_current.highest_school_level_completed_year, weekly_current.residential_postcode,
									xlookup_employment_status.employment_status_description, weekly_current.disability_flag,
									weekly_current.age, xlookup_age_group.age_range, weekly_current.postal_postcode,
									weekly_current.chessn, weekly_current.vfh_atsi_code, weekly_current.vfh_citizenship_code,
									weekly_current.vfh_birth_country_code, weekly_current.vfh_home_language_code,
									weekly_current.vfh_term_location_postcode, weekly_current.vfh_term_location_country_code,
									weekly_current.vfh_home_location_postcode, weekly_current.vfh_home_location_country_code,
									weekly_current.vfh_arrival_year, weekly_current.vfh_permanent_resident_code,
									weekly_current.vfh_commencing_location_postcode,
									weekly_current.vfh_commencing_geographic_location, weekly_current.vfh_highest_attainment_code,
									weekly_current.vfh_highest_attainment_year, weekly_current.usi_flag, weekly_current.student_dob,
									weekly_current.email_address, weekly_current.mobile_phone_number
					FROM weekly_current
					INNER JOIN xlookup_country ON weekly_current.birth_country_code = xlookup_country.identifier
					INNER JOIN xlookup_Language ON weekly_current.home_language_code = xlookup_language.identifier
					INNER JOIN xlookup_age_group ON weekly_current.age = xlookup_age_group.age
					INNER JOIN xlookup_prior_education_level ON weekly_current.highest_prior_education_level_completed_code = xlookup_prior_education_level.level_code
					INNER JOIN xlookup_school_level ON weekly_current.highest_school_level_completed_code = xlookup_school_level.school_level_code
					INNER JOIN xlookup_employment_status ON weekly_current.employment_category = xlookup_employment_status.employment_status_code
					""")
		'''
		# q501a - tested OK - needs more testing (data did not match)
		'''
		cur.execute("""
					UPDATE student
					SET a_ses2006 = xlookup_mceetya_ses.a_ses2006
					FROM xlookup_mceetya_ses
					WHERE student.residential_postcode = xlookup_mceetya_ses.postcode
					""")
		'''
		# q501b - tested OK - needs more testing (data did not match)
		'''
		cur.execute("""
					SELECT weekly_current.student_id, SUM(weekly_current.enrolled_ahc) AS sum_of_enrolled_ahc
					INTO student_enrolled_ahc_ex_sw_ct_ns_calculation
					FROM weekly_current
					WHERE (weekly_current.outcome NOT IN ('SW', 'NS', 'CT', 'RPL-CA') OR weekly_current.outcome IS NULL)				
					AND weekly_current.unit_attempt_status <> 'CANCELLED'
					GROUP BY weekly_current.student_id
					""")
		'''
		# q501c - tested OK - needs more testing (data did not match)
		'''
		cur.execute("""
					UPDATE student
					SET enrolled_ahc_ex_ns_ct_sw = student_enrolled_ahc_ex_sw_ct_ns_calculation.sum_of_enrolled_ahc
					FROM student_enrolled_ahc_ex_sw_ct_ns_calculation
					WHERE student.student_id = student_enrolled_ahc_ex_sw_ct_ns_calculation.student_id
					""")
		'''
		# q501d - tested OK - needs more testing (data did not match)
		'''
		cur.execute("""
					SELECT weekly_current.student_id, Sum(weekly_current.resulted_ahc) AS sum_of_resulted_ahc
					INTO student_resulted_ahc_ex_sw_ct_ns_calculation
					FROM weekly_current
					WHERE (weekly_current.outcome NOT IN ('SW', 'NS', 'CT', 'RPL-CAN') OR weekly_current.outcome IS NULL)
					AND (weekly_current.unit_attempt_status NOT IN ('ASSESSING', 'CANCELLED') OR weekly_current.unit_attempt_status IS NULL)
					GROUP BY weekly_current.student_id
					""")
		'''
		# q501e - tested OK - needs more testing (data did not match)
		'''
		cur.execute("""
					UPDATE student
					SET resulted_ahc_ex_ns_ct_sw = student_resulted_ahc_ex_sw_ct_ns_calculation.sum_of_resulted_ahc
					FROM student_resulted_ahc_ex_sw_ct_ns_calculation
					WHERE student.student_id = student_resulted_ahc_ex_sw_ct_ns_calculation.student_id
					""")
		'''
		# q501f - tested OK - needs more testing (data did not match)
		'''
		cur.execute("""
					UPDATE student
					SET ft_pt_status =	(case
											when enrolled_ahc_ex_ns_ct_sw < 540 then 'Part Time'
											when enrolled_ahc_ex_ns_ct_sw >= 540 then 'Full Time'
											else NULL
										end),
						equivalent_eftsl = (case
												when enrolled_ahc_ex_ns_ct_sw IS NOT NULL then ROUND(enrolled_ahc_ex_ns_ct_sw/720, 2)
												else NULL
											end)												
					""")
		'''
		# q501h - tested OK - no data so needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_atsi_description = xlookup_vfh_atsi.vfh_atsi_description
					FROM xlookup_vfh_atsi
					WHERE student.student_id = xlookup_vfh_atsi.vfh_atsi_code
					""")
		'''
		# q501i - tested OK - data did not match needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_citizenship_description = xlookup_vfh_citizenship.vfh_citizenship_description
					FROM xlookup_vfh_citizenship
					WHERE student.vfh_citizenship_code = xlookup_vfh_citizenship.vfh_citizenship_cd
					""")
		'''
		# q501j - tested OK - data did not match needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_birth_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student.vfh_birth_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q501k - tested OK - data did not match needs additional testing
		'''
		cur.execute("""
					UPDATE student 
					SET vfh_highest_attainment_description = xlookup_vfh_highest_attainment.vfh_highest_participation_description
					FROM xlookup_vfh_highest_attainment
					WHERE xlookup_vfh_highest_attainment.vfh_highest_participation_cd = student.vfh_highest_attainment_code					
					""")
		'''
		# q501l - tested OK - data did not match needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_home_language_description = xlookup_vfh_language.vfh_home_language_description
					FROM xlookup_vfh_language
					WHERE xlookup_vfh_language.vfh_home_language_cd = student.vfh_home_language_code
					""")
		'''
		# q501m - tested OK - data did not match needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_home_location_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE xlookup_vfh_birth_country.vfh_birth_country_cd = student.vfh_home_location_country_code
					""")
		'''
		# q501n - tested NOT OK - data did not match needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_permanent_resident_status = xlookup_vfh_permanent_residence.vfh_permanent_residence_description
					FROM xlookup_vfh_permanent_residence
					WHERE student.vfh_permanent_resident_code = xlookup_vfh_permanent_residence.vfh_permanent_residence_cd
					""")
		'''
		# q501o - tested NOT OK - data matched, but needs additional testing
		'''
		cur.execute("""
					UPDATE student
					SET vfh_term_location_country_code = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student.vfh_term_location_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q502a - tested NOT OK - not implemented correctly
		'''
		cur.execute("""
					INSERT INTO errors_for_correction_by_vet_teams (error_type, student_id, prior_education, gender, home_language_code,
																	birth_country_code, highest_school_level_completed_code,
																	highest_school_level_completed_year, residential_post_code, employment_category,
																	disability, unit_funding_source, delivery_location_team)
					SELECT DISTINCT 'Check Duplicate Student Due to Possible Invalid Funding Source Combination' AS error_message, student.student_id,
									weekly_current.highest_prior_education_level_completed_code, weekly_current.student_gender,
									weekly_current.home_language_code, weekly_current.birth_country_code, weekly_current.highest_school_level_completed_code,
									weekly_current.highest_school_level_completed_year, weekly_current.residential_postcode, weekly_current.employment_category,
									weekly_current.disability_flag, weekly_current.unit_funding_source, weekly_current.delivery_location_team
					FROM student
					INNER JOIN weekly_current
					ON student.student_id = weekly_current.student_id
					WHERE student.student_id in (	SELECT student_id
													FROM student AS tmp 
													GROUP BY student_id HAVING Count(*) > 1)
					ORDER BY student.student_id
					""")
		'''
		# q502b - tested NOT OK - not sure if implemented properly
		'''
		cur.execute("""
					SELECT 'Potential Duplicate Student - Matching first and last names' AS error_message,
							student.student_id, student.student_first_name, student.student_last_name, student.dob,
							student.student_gender, student.atsi, student.disability_flag, student.residential_postcode,
							student.country_of_birth, student.language, student.highest_school_level_completed_year,
							student.highest_school_level_completed
					INTO error_possible_student_dups_douglas
					FROM student
					WHERE student.student_first_name IN (	SELECT student_first_name
															FROM student As tmp
															GROUP BY student_first_name, student_last_name
															HAVING (Count(*) > 1
															AND student_last_name = student.student_last_name))
					ORDER BY student.student_first_name, student.student_last_name
					""")
		'''
		# q502c - tested NOT OK - not sure if implemented properly
		'''
		cur.execute("""
					INSERT INTO error_possible_student_dups_douglas (error_message, student_first_name, student_last_name,
																	student_id, dob, disability_flag, atsi, student_gender,
																	residential_postcode, language, country_of_birth,
																	highest_school_level_completed, highest_school_level_completed_year)
					SELECT 'Potential Duplicate Student - Matching first names and dates of birth' AS error_message,
							student_first_name, student_last_name, student_id, dob, disability_flag, atsi, student_gender,
							residential_postcode, language, country_of_birth, highest_school_level_completed,
							highest_school_level_completed_year
					FROM student
					WHERE student.student_first_name In (	SELECT student_first_name
															FROM student As Tmp GROUP BY student_first_name, dob
															HAVING (Count(*) > 1 
															AND dob = student.dob))
					ORDER BY student.student_first_name, student.dob
					""")
		'''
		# q502d - tested NOT OK - not sure if implemented properly
		'''
		cur.execute("""
					INSERT INTO error_possible_student_dups_douglas (error_message, student_first_name, student_last_name,
																	student_id, dob, atsi, student_gender, disability_flag, residential_postcode, highest_school_level_completed_year,
																	highest_school_level_completed, country_of_birth, language)
					SELECT 'Potential Duplicate Student - Matching last names and dates of birth' AS error_message,
					student_first_name, student_last_name, student_id, dob, atsi, student_gender, disability_flag,
					residential_postcode, highest_school_level_completed_year, highest_school_level_completed, country_of_birth,
					language
					FROM student
					WHERE student.student_last_name IN (SELECT student_last_name
														FROM student As Tmp
														GROUP BY student_last_name, dob
														HAVING (Count(*) > 1  AND dob = student.dob))
					ORDER BY student.student_last_name, student.dob
					""")
		'''
		# q502e - tested NOT OK - need to check implementation
		'''
		cur.execute("""
					SELECT DISTINCT 'Potential Duplicate Student - Matching last and first names' AS error_message,
									student.student_id AS student_id_2018,
									student.student_first_name AS student_first_name_2018,
									student.student_last_name AS student_last_name_2018,
									student.DOB AS dob_2018,
									weekly_2017.student_id AS student_id_2017,
									weekly_2017.student_first_name AS student_first_name_2017,
									weekly_2017.student_last_name AS student_last_name_2017,
									weekly_2017.student_dob AS dob_2017
					INTO error_possible_student_dups_2017_douglas
					FROM weekly_2017
					INNER JOIN student ON weekly_2017.student_first_name = student.student_first_name
					AND weekly_2017.student_last_name = student.student_last_name
					WHERE weekly_2017.student_id<>student.student_id
					AND weekly_2017.grade not in ('SW','NS')
					ORDER BY student.student_last_name, student.dob
					""")
		'''
		# q502f - tested OK
		'''
		cur.execute("""
					INSERT INTO error_possible_student_dups_2017_douglas (	error_message, student_first_name_2018, student_last_name_2018,
																			student_id_2018, dob_2018, student_id_2017, student_first_name_2017,
																			student_last_name_2017, dob_2017)
					SELECT DISTINCT 'Potential Duplicate Student - Matching first names and dates of birth' AS error_message,
									student.student_first_name AS student_first_name_2018,
									student.student_last_name AS student_last_name_2018,
									student.student_id AS student_id_2018,
									student.dob AS dob_2018,
									weekly_2017.student_id AS student_id_2017,
									weekly_2017.student_first_name AS student_first_name_2017,
									weekly_2017.student_last_name AS student_last_name_2017,
									weekly_2017.student_dob AS dob_2017
					FROM weekly_2017
					INNER JOIN student
					ON weekly_2017.student_first_name = student.student_first_name
					AND weekly_2017.student_dob = student.dob
					WHERE weekly_2017.student_id<>student.student_id
					AND weekly_2017.grade NOT IN ('SW','NS')
					ORDER BY student.student_last_name, student.dob
					""")
		'''
		# q502g - tested OK
		'''
		cur.execute("""
					INSERT INTO error_possible_student_dups_2017_douglas (	error_message, student_first_name_2018, student_last_name_2018,
																			student_id_2018, dob_2018, student_id_2017, student_first_name_2017,
																			student_last_name_2017, dob_2017)
					SELECT DISTINCT 'Potential Duplicate Student - Matching last names and dates of birth' AS error_message,
									student.student_first_name AS student_first_name_2018,
									student.student_last_name AS student_last_name_2018,
									student.student_id AS student_id_2018,
									student.DOB AS dob_2018,
									weekly_2017.student_id AS student_id_2017,
									weekly_2017.student_first_name AS student_first_name_2017,
									weekly_2017.student_last_name AS student_last_name_2017,
									weekly_2017.student_dob AS dob_2017
					FROM weekly_2017
					INNER JOIN student
					ON weekly_2017.student_last_name = student.student_last_name
					AND weekly_2017.student_dob = student.dob
					WHERE weekly_2017.student_id <> student.student_id
					AND weekly_2017.grade NOT IN ('SW','NS')
					ORDER BY student.student_last_name, student.dob
					""")
		'''
		# q503 -tested OK - needs further testing different number of rows to access
		'''
		cur.execute("""
					INSERT INTO student_course_attempt (student_id, course_code, course_name, residential_postcode, deceased_indicator,
														industry, course_attempt_status, contract_team, level, foe2, foe4, age, age_range,
														student_gender, student_home_state, fee_category, atsi, highest_school_level_completed,
														highest_school_level_completed_code, correspondence_category, vet_in_school_indicator,
														vet_school_name, at_school_indicator, postal_postcode, course_admin_team,
														sca_funding_source, division, course_commencement_date, course_delivery_mode,
														intention_to_complete_course, intention_to_complete_units_only, no_course_intention,
														course_requirements_completed_indicator, course_requirements_completed_date, chessn,
														birth_country, vfh_atsi_code, vfh_citizenship_code, vfh_birth_country_code,
														vfh_home_language_code, vfh_term_location_postcode, vfh_term_location_country_code,
														vfh_home_location_postcode, vfh_home_location_country_code, vfh_arrival_year,
														vfh_permanent_resident_code, vfh_commencing_location_postcode, vfh_highest_attainment_code,
														vfh_highest_attainment_year, basis_for_admission_code, hecs_payment_option_code, usi_flag,
														email_address, mobile_phone_number, entitlement_contract_description )
					SELECT DISTINCT weekly_current.student_id, weekly_current.course_code, weekly_current.course_name, weekly_current.residential_postcode,
									weekly_current.deceased_indicator, xlookup_det_industry.description, weekly_current.course_attempt_status,
									weekly_current.contract_team, xlookup_level.description, xlookup_foe2.description,
									xlookup_foe4.description, weekly_current.age, xlookup_age_group.age_range, weekly_current.student_gender,
									weekly_current.student_home_state, weekly_current.fee_category, weekly_current.atsi, xlookup_school_level.school_level_description,
									weekly_current.highest_school_level_completed_code, weekly_current.correspondence_category, weekly_current.vet_in_school_indicator,
									weekly_current.vet_school_name, weekly_current.at_school_indicator, weekly_current.postal_postcode,
									weekly_current.course_admin_team, weekly_current.sca_funding_source, xlookup_division.division,
									weekly_current.course_commencement_date, weekly_current.course_delivery_mode, weekly_current.intention_to_complete_course,
									weekly_current.intention_to_complete_unit_only, weekly_current.no_course_intention,
									weekly_current.course_requirements_completed_indicator, weekly_current.course_requirements_completed_date,
									weekly_current.chessn, xlookup_country.full_name, weekly_current.vfh_atsi_code, weekly_current.vfh_citizenship_code,
									weekly_current.vfh_birth_country_code, weekly_current.vfh_home_language_code, weekly_current.vfh_term_location_postcode,
									weekly_current.vfh_term_location_country_code, weekly_current.vfh_home_location_postcode,
									weekly_current.vfh_home_location_country_code, weekly_current.vfh_arrival_year, weekly_current.vfh_permanent_resident_code,
									weekly_current.vfh_commencing_location_postcode, weekly_current.vfh_highest_attainment_code,
									weekly_current.vfh_highest_attainment_year, weekly_current.basis_for_admission_code, weekly_current.hecs_payment_option_code,
									weekly_current.usi_flag, weekly_current.email_address, weekly_current.mobile_phone_number,
									weekly_current.entitlement_contract_description
					FROM 	weekly_current, xlookup_division, xlookup_foe4, xlookup_course, xlookup_level, xlookup_foe2, xlookup_age_group,
							xlookup_det_industry, xlookup_school_level, xlookup_country
					WHERE weekly_current.course_code = xlookup_course.code
					AND xlookup_course.level = xlookup_level.level_code
					AND xlookup_foe4.code = xlookup_COURSE.FOE4
					AND xlookup_course.foe2 = xlookup_foe2.code
					AND weekly_current.age = xlookup_age_group.age
					AND xlookup_division.team_code = weekly_current.course_admin_team
					AND weekly_current.course_industry = xlookup_det_industry.code
					AND weekly_current.highest_school_level_completed_code = xlookup_school_level.school_level_code
					AND weekly_current.birth_country_code = xlookup_country.identifier
					""")
		'''
		# q503a - tested OK - different number of rows (needs further testing)
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET a_ses2006 = xlookup_mceetya_ses.a_ses2006
					FROM xlookup_mceetya_ses
					WHERE student_course_attempt.residential_postcode = xlookup_mceetya_ses.postcode
					""")
		'''
		# q503c - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET basis_for_admission = xlookup_vfh_basis_for_admission.vfh_basis_for_admission_description
					FROM xlookup_vfh_basis_for_admission
					WHERE student_course_attempt.basis_for_admission_code = xlookup_vfh_basis_for_admission.vfh_basis_for_admission_cd
					""")
		'''
		# q503d - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET hecs_payment_option = xlookup_vfh_student_status.vfh_student_status_description
					FROM xlookup_vfh_student_status
					WHERE student_course_attempt.hecs_payment_option_code = xlookup_vfh_student_status.vfh_student_status_cd
					""")
		'''
		# q503e - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_atsi_description = xlookup_vfh_atsi.vfh_atsi_description
					FROM xlookup_vfh_atsi
					WHERE student_course_attempt.vfh_atsi_code = xlookup_vfh_atsi.vfh_atsi_code
					""")
		'''
		# q503f - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_birth_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE xlookup_vfh_birth_country.vfh_birth_country_cd = student_course_attempt.vfh_birth_country_code
					""")
		'''
		# q503g - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_citizenship_description = xlookup_vfh_citizenship.vfh_citizenship_description
					FROM xlookup_vfh_citizenship
					WHERE xlookup_vfh_citizenship.vfh_citizenship_cd = student_course_attempt.vfh_citizenship_code
					""")
		'''
		# q503h - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_highest_attainment_description = xlookup_vfh_highest_attainment.vfh_highest_participation_description
					FROM xlookup_vfh_highest_attainment
					WHERE student_course_attempt.vfh_highest_attainment_code = xlookup_vfh_highest_attainment.vfh_highest_participation_cd
					""")
		'''
		# q503i - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_home_language_description = xlookup_vfh_language.vfh_home_language_description
					FROM xlookup_vfh_language
					WHERE student_course_attempt.vfh_home_language_code = xlookup_vfh_language.vfh_home_language_cd
					""")
		'''
		# q503j - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_home_location_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student_course_attempt.vfh_home_location_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q503k - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_permanent_resident_status = xlookup_vfh_permanent_residence.vfh_permanent_residence_description
					FROM xlookup_vfh_permanent_residence
					WHERE student_course_attempt.vfh_permanent_resident_code = xlookup_vfh_permanent_residence.vfh_permanent_residence_cd
					""")
		'''
		# q503l - tested OK - different number of rows to access needs more testing
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET vfh_term_location_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student_course_attempt.vfh_term_location_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q504a - tested OK - dependent on funding source so needs further checking
		'''
		cur.execute("""
					SELECT student_id, course_code, sca_funding_source, SUM(enrolled_ahc) AS sum_of_enrolled_AHC
					INTO sca_enrolled_ahc_ex_sw_ct_ns_calculation
					FROM weekly_current
					WHERE outcome <> 'SW'
					And outcome <> 'NS'
					And outcome <> 'CT'
					And outcome <> 'RPL-CA'
					GROUP BY student_id, course_code, sca_funding_source
					""")
		'''
		# q504b - tested OK - dependent on funding source so needs further checking
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET enrolled_ahc_ex_ns_ct_sw = sca_enrolled_ahc_ex_sw_ct_ns_calculation.sum_of_enrolled_ahc
					FROM sca_enrolled_ahc_ex_sw_ct_ns_calculation
					WHERE sca_enrolled_ahc_ex_sw_ct_ns_calculation.sca_funding_source = student_course_attempt.sca_funding_source
					AND sca_enrolled_ahc_ex_sw_ct_ns_calculation.student_id = student_course_attempt.student_id
					AND sca_enrolled_ahc_ex_sw_ct_ns_calculation.course_code = student_course_attempt.course_code
					""")
		'''
		# q505a - tested OK - this needs further checking (initially implemented incorrectly)
		'''
		cur.execute("""
					SELECT student_id, course_code, sca_funding_source, SUM(resulted_ahc) AS sum_of_resulted_ahc
					INTO sca_resulted_ahc_ex_sw_ct_ns_calculation
					FROM weekly_current
					WHERE (weekly_current.outcome NOT IN ('SW', 'NS', 'RPL-CA') OR weekly_current.outcome IS NULL) 		
					AND (weekly_current.unit_attempt_status NOT IN ('ASSESSING', 'CANCELLED') OR weekly_current.unit_attempt_status IS NULL)
					GROUP BY weekly_current.student_id, weekly_current.course_code, weekly_current.sca_funding_source
					""")
		'''
		# q505b - tested OK - this needs further checking (initially implemented incorrectly)
		'''
		cur.execute("""
					UPDATE student_course_attempt
					SET resulted_ahc_ex_ns_ct_sw = sca_resulted_ahc_ex_sw_ct_ns_calculation.sum_of_resulted_ahc
					FROM sca_resulted_ahc_ex_sw_ct_ns_calculation
					WHERE student_course_attempt.student_id = sca_resulted_ahc_ex_sw_ct_ns_calculation.student_id
					AND student_course_attempt.course_code = sca_resulted_ahc_ex_sw_ct_ns_calculation.course_code
					AND student_course_attempt.sca_funding_source = sca_resulted_ahc_ex_sw_ct_ns_calculation.sca_funding_source
					""")
		'''
		# q506 - 
		'''
		cur.execute("""
					INSERT INTO student_unit_attempt ( teaching_period, student_id, deceased_indicator, level, course_admin_team,
													   unit_delivery_location, delivery_location_team, unit_funding_source,
													   course_delivery_mode, course_code, fee_category, course_name, unit_code,
													   unit_name, enrolled_ahc, resulted_ahc, grade, atsi, course_industry,
													   student_last_name, student_first_name, aci, tci, override_activity_end_date,
													   unit_attempt_status, correspondence_category, student_gender,
													   student_home_state, grade_keyed, vet_school_name, unit_delivery_type,
													   enrol_date, disc_date, result_date, staff_indicator, stream_code,
													   study_reason, granted_date, vet_in_school_indicator, at_school_indicator,
													   highest_prior_education_level_completed_code, home_language_code,
													   birth_country_code, highest_school_level_completed_code, highest_school_level_completed_year,
													   residential_postcode, employment_category, disability_flag, course_attempt_status,
													   course_commencement_date, sca_funding_source, enrolment_activity_end_date,
													   postal_postcode, override_activity_start_date, intention_to_complete_course,
													   intention_to_complete_units_only, no_course_intention, course_requirements_completed_indicator,
													   course_requirements_completed_date, result_type, unit_contact, cancelled_date,
													   not_approved_date, administrative_unit_status, chessn, vfh_atsi_code,
													   vfh_citizenship_code, vfh_birth_country_code, vfh_home_language_code,
													   vfh_term_location_postcode, vfh_term_location_country_code, vfh_home_location_postcode,
													   vfh_home_location_country_code, vfh_arrival_year, vfh_permanent_resident_code,
													   vfh_commencing_location_postcode, vfh_commencing_geographic_location,
													   vfh_highest_attainment_code, vfh_highest_attainment_year, basis_for_admission_code,
													   hecs_payment_option_code, unit_student_status_code, unit_census_date,
													   usi_flag, contract_course_unit_name, contract_course_unit_code, contract, outcome,
													   age, teaching_period_end_date, enrol_week, result_week, contract_team, ur_outcome,
													   country_of_birth, language, highest_school_level_completed, highest_prior_education_level_completed,
													   employment_category_description, delivery_postal_location, delivery_region,
													   delivery_remoteness, delivery_providence, delivery_state_code, unit_delivery_description,
													   course_industry_name, study_reason_description, division, unit_delivery_location_description,
													   email_address, mobile_phone_number, entitlement_contract_description )
					SELECT 	weekly_current.teaching_period, weekly_current.student_id, weekly_current.deceased_indicator,
							xlookup_level.description AS level, weekly_current.course_admin_team, weekly_current.unit_delivery_location,
							weekly_current.delivery_location_team, weekly_current.unit_funding_source, weekly_current.course_delivery_mode,
							weekly_current.course_code, weekly_current.fee_category, weekly_current.course_name, weekly_current.unit_code,
							weekly_current.unit_name, weekly_current.enrolled_ahc, weekly_current.resulted_ahc, weekly_current.grade,
							weekly_current.atsi, weekly_current.course_industry, weekly_current.student_last_name, weekly_current.student_first_name,
							weekly_current.aci, weekly_current.tci, weekly_current.override_activity_end_date, weekly_current.unit_attempt_status,
							weekly_current.correspondence_category, weekly_current.student_gender, weekly_current.student_home_state,
							weekly_current.grade_keyed, weekly_current.vet_school_name, weekly_current.unit_delivery_type, weekly_current.enrol_date,
							weekly_current.disc_date, weekly_current.result_date, weekly_current.staff_indicator, weekly_current.stream_code,
							weekly_current.study_reason, weekly_current.granted_date, weekly_current.vet_in_school_indicator, weekly_current.at_school_indicator,
							weekly_current.highest_prior_education_level_completed_code, weekly_current.home_language_code, weekly_current.birth_country_code,
							weekly_current.highest_school_level_completed_code, weekly_current.highest_school_level_completed_year,
							weekly_current.residential_postcode, weekly_current.employment_category, weekly_current.disability_flag,
							weekly_current.course_attempt_status, weekly_current.course_commencement_date, weekly_current.sca_funding_source,
							weekly_current.enrolment_activity_end_date, weekly_current.postal_postcode, weekly_current.override_activity_start_date,
							weekly_current.intention_to_complete_course, weekly_current.intention_to_complete_unit_only,
							weekly_current.no_course_intention, weekly_current.course_requirements_completed_indicator, weekly_current.course_requirements_completed_date,
							weekly_current.result_type, weekly_current.unit_contact, weekly_current.cancelled_date, weekly_current.not_approved_date,
							weekly_current.administrative_unit_status, weekly_current.chessn, weekly_current.vfh_atsi_code,
							weekly_current.vfh_citizenship_code, weekly_current.vfh_birth_country_code, weekly_current.vfh_home_language_code,
							weekly_current.vfh_term_location_postcode, weekly_current.vfh_term_location_country_code, weekly_current.vfh_home_location_postcode,
							weekly_current.vfh_home_location_country_code, weekly_current.vfh_arrival_year, weekly_current.vfh_permanent_resident_code,
							weekly_current.vfh_commencing_location_postcode, weekly_current.vfh_commencing_geographic_location,
							weekly_current.vfh_highest_attainment_code, weekly_current.vfh_highest_attainment_year, weekly_current.basis_for_admission_code,
							weekly_current.hecs_payment_option_code, weekly_current.unit_student_status_code, weekly_current.unit_census_date,
							weekly_current.usi_flag, weekly_current.contract_course_unit_name, weekly_current.contract_course_unit_code,
							weekly_current.contract, weekly_current.outcome, weekly_current.age, weekly_current.teaching_period_end_date,
							weekly_current.enrol_week, weekly_current.result_week, weekly_current.contract_team, weekly_current.ur_outcome,
							xlookup_country.full_name, xlookup_language.full_name, xlookup_school_level.school_level_description,
							xlookup_prior_education_level.description, xlookup_employment_status.employment_status_description,
							xlookup_location.postal_location AS delivery_postal_location, xlookup_location.region AS delivery_region,
							xlookup_location.remoteness AS delivery_remoteness, xlookup_location.providence AS delivery_providence,
							xlookup_location.state_code AS delivery_state, xlookup_unit_delivery_type.description, xlookup_det_industry.description,
							xlookup_study_reason.study_reason_description, xlookup_division.division, xlookup_location.description,
							weekly_current.email_address, weekly_current.mobile_phone_number, weekly_current.entitlement_contract_description
					FROM 	xlookup_unit_delivery_type, weekly_current, xlookup_location, xlookup_study_reason, xlookup_det_industry, xlookup_country,
							xlookup_language, xlookup_school_level, xlookup_prior_education_level, xlookup_employment_status, xlookup_course,
							xlookup_level, xlookup_division
					WHERE weekly_current.unit_delivery_location = xlookup_location.code
					AND weekly_current.study_reason = xlookup_study_reason.study_reason_id
					AND weekly_current.course_industry = xlookup_det_industry.code
					AND xlookup_UNIT_DELIVERY_TYPE.Code = weekly_current.unit_delivery_type
					AND weekly_current.birth_country_code = xlookup_country.identifier
					AND weekly_current.home_language_code = xlookup_language.identifier
					AND weekly_current.highest_school_level_completed_code = xlookup_school_level.school_level_code
					AND weekly_current.highest_prior_education_level_completed_code = xlookup_prior_education_level.level_code
					AND weekly_current.employment_category = xlookup_employment_status.employment_status_code
					AND weekly_current.course_code = xlookup_course.code
					AND xlookup_course.level = xlookup_level.level_code
					AND weekly_current.delivery_location_team = xlookup_division.team_code
					""")
		'''
		# q506a - tested OK - additional data was pulled compared to access db (check this)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET a_ses2006 = xlookup_mceetya_ses.a_ses2006
					FROM xlookup_mceetya_ses
					WHERE student_unit_attempt.residential_postcode = xlookup_mceetya_ses.postcode
					""")
		'''
		# q506c - tested OK
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET basis_for_admission = xlookup_vfh_basis_for_admission.vfh_basis_for_admission_description
					FROM xlookup_vfh_basis_for_admission
					WHERE student_unit_attempt.basis_for_admission_code = xlookup_vfh_basis_for_admission.vfh_basis_for_admission_cd
					""")
		'''
		# q506d - tested OK
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET student_unit_attempt.hecs_payment_option = xlookup_vfh_student_status.vfh_student_status_description
					FROM xlookup_vfh_student_status
					WHERE student_unit_attempt.hecs_payment_option_code = xlookup_vfh_student_status.vfh_student_status_cd
					""")
		'''
		# q506e - tested OK
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET unit_student_status = xlookup_vfh_student_status.vfh_student_status_description
					FROM xlookup_vfh_student_status
					WHERE student_unit_attempt.hecs_payment_option_code = xlookup_vfh_student_status.vfh_student_status_cd
					AND xlookup_vfh_student_status.vfh_student_status_cd = student_unit_attempt.unit_student_status_code
					""")
		'''
		# q506f - tested OK - data is not the same as access routine (need to check)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_atsi_description = xlookup_vfh_atsi.vfh_atsi_description
					FROM xlookup_vfh_atsi
					WHERE student_unit_attempt.vfh_atsi_code = xlookup_vfh_atsi.vfh_atsi_code
					""")
		'''
		# q506g - tested OK - data is not the same as access routine (need to check)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_birth_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student_unit_attempt.vfh_birth_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q506h - tested OK - data is not the same as access routine (need to check)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_citizenship_description = xlookup_vfh_citizenship.vfh_citizenship_description
					FROM xlookup_vfh_citizenship
					WHERE xlookup_vfh_citizenship.vfh_citizenship_cd = student_unit_attempt.vfh_citizenship_code
					""")
		'''
		# q506i - tested OK - data is not the same as access routine (need to check)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_highest_attainment_description = xlookup_vfh_highest_attainment.vfh_highest_participation_description
					FROM xlookup_vfh_highest_attainment
					WHERE xlookup_vfh_highest_attainment.vfh_highest_participation_cd = student_unit_attempt.vfh_highest_attainment_code
					""")
		'''
		# q506j - tested OK - data is not the same as access routine (need to check)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_home_language_description = xlookup_vfh_language.vfh_home_language_description
					FROM xlookup_vfh_language
					WHERE xlookup_vfh_language.vfh_home_language_cd = student_unit_attempt.vfh_home_language_code
					""")
		'''
		# q506k - tested OK
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_home_location_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student_unit_attempt.vfh_home_location_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q506l - tested OK - data is not the same as access routine (need to check)
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_permanent_resident_status = xlookup_vfh_permanent_residence.vfh_permanent_residence_description
					FROM xlookup_vfh_permanent_residence
					WHERE xlookup_vfh_permanent_residence.vfh_permanent_residence_cd = student_unit_attempt.vfh_permanent_resident_code
					""")
		'''
		# q506m - tested NOT OK
		'''
		cur.execute("""
					UPDATE student_unit_attempt
					SET vfh_term_location_country_description = xlookup_vfh_birth_country.vfh_birth_country_description
					FROM xlookup_vfh_birth_country
					WHERE student_unit_attempt.vfh_term_location_country_code = xlookup_vfh_birth_country.vfh_birth_country_cd
					""")
		'''
		# q507 - tested OK
		'''
		cur.execute("""
					INSERT INTO activity_pattern_trend (unit_delivery_team, division, funding_source, week_2017, week_2018,
														target_2018, target_2017, enrolled_2018, resulted_2018,
														funded_enrolled_2018, funded_resulted_2018, unfunded_enrolled_2018,
														unfunded_resulted_2018, enrolled_2017, resulted_2017,
														funded_enrolled_2017, funded_resulted_2017, unfunded_enrolled_2017,
														unfunded_resulted_2017 )
					SELECT 	unit_delivery_team, division, funding_source, week_2017, week_2018, target_2018, target_2017,
							enrolled_2018, resulted_2018, funded_enrolled_2018, funded_resulted_2018, unfunded_enrolled_2018,
							unfunded_resulted_2018, enrolled_2017, resulted_2017, funded_enrolled_2017, funded_resulted_2017,
							unfunded_enrolled_2017, unfunded_resulted_2017
					FROM xlookup_activity_pattern_trend
					WHERE xlookup_activity_pattern_trend.week_2017 = 	(case
																			when extract(YEAR FROM now()::date) < 2018 then 0
																			when extract(YEAR FROM now()::date) > 2018 then 53
																			else TRUNC(DATE_PART('day', now()::timestamp - '2018-01-01'::timestamp)/7)
																		end)
					ORDER BY xlookup_activity_pattern_trend.unit_delivery_team,
					xlookup_activity_pattern_trend.funding_source,
					xlookup_activity_pattern_trend.week_2017,
					xlookup_activity_pattern_trend.week_2018
					""")
		'''
		# q508 - tested NOT OK - based on funding sources so there will be difficulties with this query
		'''
		cur.execute("""
					SELECT 	delivery_location_team AS unit_delivery_team,
							(case
								when unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' then 'ETP2017'
								when unit_funding_source = 'ETP' then 'ETP2016'
								else unit_funding_source
							end) AS funding_source,
							weekly_current.enrol_week,
							SUM(weekly_current.enrolled_ahc) AS sum_of_enrolled_ahc
					INTO activity_pattern_enrolled
					FROM weekly_current
					GROUP BY weekly_current.delivery_location_team,
					(case
						when unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' then 'ETP2017'
						when unit_funding_source = 'ETP' then 'ETP2016'
						else unit_funding_source
					end),
					weekly_current.enrol_week
					""")
		'''
		# q508a - tested NOT OK - query not returning any results (this may be a problem with the query or the data)
		'''
		cur.execute("""
					UPDATE activity_pattern_trend
					SET enrolled_2018 = activity_pattern_enrolled.sum_of_enrolled_ahc
					FROM activity_pattern_enrolled
					WHERE activity_pattern_enrolled.funding_source = activity_pattern_trend.funding_source
					AND activity_pattern_enrolled.enrol_week = activity_pattern_trend.week_2018
					AND LEFT(activity_pattern_trend.unit_delivery_team, 3) = activity_pattern_enrolled.unit_delivery_team
					""")
		'''
		# q509 - tested NOT OK - based on funding sources so there will be difficulties with this query
		'''
		cur.execute("""
					SELECT 	delivery_location_team AS unit_delivery_team,
							(case
								when unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' then 'ETP2017'
								when unit_funding_source = 'ETP' then 'ETP2016'
								else unit_funding_source
							end) AS funding_source,
							weekly_current.result_week,
							SUM(weekly_current.resulted_ahc) AS sum_of_resulted_ahc
							INTO activity_pattern_resulted
					FROM weekly_current
					GROUP BY weekly_current.delivery_location_team,
					(case
						when unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' then 'ETP2017'
						when unit_funding_source = 'ETP' then 'ETP2016'
						else unit_funding_source
					end),
					weekly_current.result_week
					""")
		'''
		# q509a - tested NOT OK - query not returning any results (this may be a problem with the query or the data)
		'''
		cur.execute("""
					UPDATE activity_pattern_trend
					SET resulted_2018 = activity_pattern_resulted.sum_of_resulted_ahc
					FROM activity_pattern_resulted
					WHERE activity_pattern_resulted.result_week = activity_pattern_trend.week_2018
					AND activity_pattern_resulted.funding_source = activity_pattern_trend.funding_source
					AND LEFT(activity_pattern_trend.unit_delivery_team, 3) = activity_pattern_resulted.unit_delivery_team
					""")
		'''
		# q510 - tested NOT OK - based on funding sources so there will be difficulties with this query
		'''
		cur.execute("""
					SELECT weekly_current.delivery_location_team AS unit_delivery_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END) AS funding_source,
					weekly_current.enrol_week,
					SUM(weekly_current.enrolled_ahc) AS sum_of_enrolled_ahc
					INTO activity_pattern_enrolled_funded
					FROM weekly_current
					WHERE weekly_current.outcome NOT IN ('CT', 'NS', 'SW', 'RPL-CA') OR weekly_current.outcome IS NULL
					AND weekly_current.unit_attempt_status <> 'CANCELLED'
					GROUP BY weekly_current.delivery_location_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END),
					weekly_current.enrol_week
					""")
		'''
		# q510a - tested NOT OK - query not returning any results (this may be a problem with the query or the data)
		'''
		cur.execute("""
					UPDATE activity_pattern_trend
					SET funded_enrolled_2018 = activity_pattern_enrolled_funded.sum_of_enrolled_ahc
					FROM activity_pattern_enrolled_funded
					WHERE activity_pattern_trend.funding_source = activity_pattern_enrolled_funded.funding_source
					AND activity_pattern_trend.Week_2018 = activity_pattern_enrolled_funded.enrol_week
					AND LEFT(activity_pattern_trend.unit_delivery_team, 3) = activity_pattern_enrolled_funded.unit_delivery_team
					""")
		'''
		# q510b - tested NOT OK - based on funding source which is not correct
		'''
		cur.execute("""
					SELECT weekly_current.delivery_location_team AS unit_delivery_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END) AS funding_source,
					weekly_current.result_week,
					SUM(weekly_current.resulted_ahc) AS sum_of_resulted_ahc
					INTO activity_pattern_resulted_funded
					FROM weekly_current
					WHERE (weekly_current.outcome NOT IN ('CT','NS','SW','UR','RPL-CA') OR weekly_current.outcome IS NULL)
					AND (weekly_current.unit_attempt_status NOT IN ('ASSESSING','CANCELLED') OR weekly_current.unit_attempt_status IS NULL)
					GROUP BY weekly_current.delivery_location_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END),
					weekly_current.result_week
					""")
		'''
		# q510c - tested NOT OK did not return any results
		'''
		cur.execute("""
					UPDATE activity_pattern_trend
					SET funded_resulted_2018 = activity_pattern_resulted_funded.sum_of_resulted_ahc
					FROM activity_pattern_resulted_funded
					WHERE activity_pattern_resulted_funded.funding_source = activity_pattern_trend.funding_source
					AND activity_pattern_resulted_funded.result_week = activity_pattern_trend.week_2018
					AND LEFT(activity_pattern_trend.unit_delivery_team, 3) = activity_pattern_resulted_funded.unit_delivery_team
					""")
		'''
		# q511 - tested NOT OK - based on funding source which is not correct
		'''
		cur.execute("""
					SELECT weekly_current.delivery_location_team AS unit_delivery_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND  entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END) AS funding_source,
					weekly_current.enrol_week,
					SUM(weekly_current.enrolled_ahc) AS sum_of_enrolled_ahc
					INTO activity_pattern_enrolled_unfunded
					FROM weekly_current
					GROUP BY weekly_current.delivery_location_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND  entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END),
					weekly_current.enrol_week,
					weekly_current.outcome
					HAVING weekly_current.outcome IN ('CT','NS','SW','RPL-CA')
					""")
		'''
		# q511a - tested NOT OK - not returning any values not sure if issue with data or issue with query
		'''
		cur.execute("""
					UPDATE activity_pattern_trend
					SET unfunded_Enrolled_2018 = activity_pattern_enrolled_unfunded.sum_of_enrolled_ahc
					FROM activity_pattern_enrolled_unfunded
					WHERE activity_pattern_enrolled_unfunded.funding_source = activity_pattern_trend.funding_source
					AND activity_pattern_enrolled_unfunded.enrol_week = activity_pattern_trend.week_2018
					AND LEFT(activity_pattern_trend.unit_delivery_team, 3) = activity_pattern_enrolled_unfunded.unit_delivery_team
					""")
		'''
		# q511b - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT weekly_current.delivery_location_team AS unit_delivery_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END) AS funding_source,
					weekly_current.result_week,
					SUM(weekly_current.resulted_ahc) AS sum_of_resulted_ahc
					INTO activity_pattern_resulted_unfunded
					FROM weekly_current
					WHERE weekly_current.outcome IN ('CT','NS','SW','RPL-CA')
					GROUP BY weekly_current.delivery_location_team,
					(CASE
						WHEN unit_funding_source = 'ETP' AND entitlement_contract_description = '2017-MOA-4' THEN 'ETP2017'
						WHEN unit_funding_source = 'ETP' THEN 'ETP2016'
						ELSE unit_funding_source
					END),					
					weekly_current.result_week
					""")
		'''
		# q511c - tested NOT OK - not returning any values not sure if issue with data or issue with query
		'''
		cur.execute("""
					UPDATE activity_pattern_trend
					SET unfunded_resulted_2018 = activity_pattern_resulted_unfunded.sum_of_resulted_ahc
					FROM activity_pattern_resulted_unfunded
					WHERE activity_pattern_resulted_unfunded.funding_source = activity_pattern_trend.funding_source
					AND activity_pattern_resulted_unfunded.result_week = activity_pattern_trend.Week_2018
					AND LEFT(activity_pattern_trend.unit_delivery_team, 3) = activity_pattern_resulted_unfunded.unit_delivery_team
					""")
		'''
		# q512 - tested NOT OK - returns no results (something wrong with the unit attempt status field)
		'''
		cur.execute("""
					INSERT INTO unresulted_SUA_2017 (	teaching_period, student_id, course_admin_team, unit_delivery_location,
														sca_funding_source, course_code, course_name, unit_code, unit_name,
														enrolled_ahc, grade, student_last_name, student_first_name,
														enrolment_activity_end_date, contract_team, unit_attempt_status,
														result_type, usi_flag)
					SELECT 	teaching_period, student_id, delivery_location_team, unit_delivery_location, unit_funding_source,
							course_code, course_name, unit_code, unit_name, enrolled_ahc, grade, student_last_name,
							student_first_name, enrolment_activity_end_date, contract_team, unit_attempt_status,
							result_type, usi_flag
					FROM weekly_2017
					WHERE weekly_2017.grade IN ('UR','CE','OWA','RPL')
					AND weekly_2017.unit_attempt_status = 'ASSESSING'
					""")
		'''
		# q513 - tested NOT OK - based on funding source so query could not be reliably tested
		'''
		cur.execute("""
					INSERT INTO team_activity (	location, division, funding_source, contract_course, contract_course_name,
												total_target, total_enrolled, total_resulted, remoteness, unit_delivery_team,
												urban_target, urban_enrolled, urban_resulted, remote_target, remote_enrolled,
												remote_resulted, regional_target, regional_enrolled, regional_resulted,
												interstate_target, interstate_enrolled, interstate_resulted)
					SELECT DISTINCT student_unit_attempt.unit_delivery_location, student_unit_attempt.division,
									student_unit_attempt.unit_funding_source, student_unit_attempt.course_code,
									student_unit_attempt.course_name, 0 AS expr7,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									student_unit_attempt.delivery_remoteness, xlookup_team.description,
									0 AS expr8, SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1, 0 AS expr1, 0 AS expr2,
									0 AS expr3, 0 AS expr5, 0 AS expr6, 0 AS expr4, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code, 3) = delivery_location_team
					AND student_unit_attempt.outcome NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_delivery_location,
								student_unit_attempt.Division,
								student_unit_attempt.unit_funding_source,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								expr7,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description,
								expr8, expr1, expr2, expr3, expr5, expr6, expr4, exp13, exp14, exp15
					HAVING student_unit_attempt.unit_funding_source IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'URBAN'
					""")
		'''
		# q513a - tested NOT OK - no data returned from the table (issue from previous query)
		'''
		cur.execute("""
					UPDATE team_activity
					SET total_target = ahc, urban_target = ahc
					FROM xlookup_target
					WHERE team_activity.location = xlookup_target.location
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.funding_source = xlookup_target.funding
					AND team_activity.Remoteness = 'URBAN'
					AND team_activity.funding_source IN ('11N','11V','11H')
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q513b - NOT tested NOT OK (not sure if implemented correctly with LEFT JOIN)
		'''
		cur.execute("""
					INSERT INTO team_activity ( unit_delivery_team, division, location, funding_source, contract_course,
												contract_course_name, remoteness, total_target, total_enrolled, total_resulted,
												urban_target, urban_enrolled, urban_resulted, regional_target, regional_enrolled,
												regional_resulted, remote_target, remote_enrolled, remote_resulted,
												interstate_target, interstate_enrolled, interstate_resulted )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location,
							xlookup_target.funding, xlookup_target.contract_course_unit, xlookup_course.description,
							xlookup_target.remoteness, SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1, 0 AS expr2,
							SUM(xlookup_target.ahc) AS sum_of_ahc1, 0 AS expr5, 0 AS expr6, 0 AS expr7, 0 AS expr8, 0 AS expr9,
							0 AS expr10, 0 AS expr11, 0 AS expr12, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_target.remoteness = team_activity.remoteness
					AND xlookup_target.contract_team = team_activity.unit_delivery_team
					AND xlookup_target.location = team_activity.location
					AND xlookup_target.contract_course_unit = team_activity.contract_course
					AND xlookup_target.funding = team_activity.funding_source
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team,
								xlookup_target.division_school,
								xlookup_target.location,
								xlookup_target.funding,
								xlookup_target.contract_course_unit,
								xlookup_course.description,
								xlookup_target.remoteness, expr1,
								team_activity.unit_delivery_team,
								team_activity.location,
								team_activity.contract_course,
								team_activity.funding_source,
								team_activity.remoteness, expr2, expr5, expr6, expr7, expr8,
								expr9, expr10, expr11, expr12, exp13, exp14, exp15
					HAVING xlookup_target.funding IN ('11N','11V','11H')
					AND xlookup_target.Remoteness = 'URBAN'
					AND team_activity.unit_delivery_team IS NULL
					AND team_activity.location IS NULL
					AND team_activity.contract_course IS NULL
					AND team_activity.funding_source IS NULL
					AND team_activity.remoteness IS NULL
					""")
		'''
		# q514 - tested NOT OK - did not return any data (query needs to be checked) 
		'''
		cur.execute("""
					INSERT INTO team_activity (	location, division, funding_source, contract_course, contract_course_name,
												remoteness, total_target, total_enrolled, total_resulted, unit_delivery_team,
												urban_target, urban_enrolled, urban_resulted, remote_target, remote_enrolled,
												remote_resulted, regional_target, regional_enrolled, regional_resulted,
												interstate_target, interstate_enrolled, interstate_resulted)
					SELECT DISTINCT student_unit_attempt.unit_delivery_location, student_unit_attempt.division,
									student_unit_attempt.unit_funding_source, student_unit_attempt.course_code,
									student_unit_attempt.course_name, student_unit_attempt.delivery_remoteness,
									0 AS expr7, SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									xlookup_team.description, 0 AS expr8, 0 AS expr9, 0 AS expr10, 0 AS expr1,
									0 AS expr2, 0 AS expr3, 0 AS expr5,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1,
									0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code,3) = delivery_location_team
					AND student_unit_attempt.outcome NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_delivery_location,
								student_unit_attempt.division,
								student_unit_attempt.unit_funding_source,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description, expr7, expr8, expr9, expr10, expr1,
								expr2, expr3, expr5, exp13, exp14, exp15
					HAVING student_unit_attempt.unit_funding_source IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'REGIONAL'
					""")
		'''
		# q514a - tested NOT OK - did not return any 
		'''
		cur.execute("""
					UPDATE team_activity
					SET team_activity.total_target = ahc, team_activity.regional_target = ahc
					FROM xlookup_target
					WHERE team_activity.location = xlookup_target.location
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.funding_source = xlookup_target.funding
					AND team_activity.remoteness = 'REGIONAL'
					AND team_activity.funding_source IN ('11N','11V','11H')
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q514b - tested NOT OK returned data when access query did not
		'''
		cur.execute("""
					INSERT INTO team_activity ( unit_delivery_team, division, location, funding_source, contract_course,
												contract_course_name, remoteness, total_target, total_enrolled, total_resulted,
												urban_target, urban_enrolled, urban_resulted, regional_target, regional_enrolled,
												regional_resulted, remote_target, remote_enrolled, remote_resulted, interstate_target,
												interstate_enrolled, interstate_resulted )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location,
							xlookup_target.funding, xlookup_target.contract_course_unit, xlookup_course.description,
							xlookup_target.remoteness, SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1,
							0 AS expr2, 0 AS expr3, 0 AS expr5, 0 AS expr6, SUM(xlookup_target.ahc) AS sum_of_ahc_1,
							0 AS expr8, 0 AS expr9, 0 AS expr10, 0 AS expr11, 0 AS expr12, 0 AS exp13, 0 AS exp14,
							0 AS exp15
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_target.remoteness = team_activity.remoteness
					AND xlookup_target.contract_team = team_activity.unit_delivery_team
					AND xlookup_target.location = team_activity.location
					AND xlookup_target.contract_course_unit = team_activity.contract_course
					AND xlookup_target.funding = team_activity.funding_source
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team,
								xlookup_target.division_school,
								xlookup_target.location,
								xlookup_target.funding,
								xlookup_target.contract_course_unit,
								xlookup_course.description,
								xlookup_target.remoteness, expr1, expr2, expr3, expr5,
								expr6, expr8, expr9, expr10, expr11, expr12,
								team_activity.unit_delivery_team,
								team_activity.location,
								team_activity.contract_course,
								team_activity.funding_source,
								team_activity.remoteness, exp13, exp14, exp15
					HAVING xlookup_TARGET.Funding IN ('11N','11V','11H')
					AND xlookup_target.remoteness = 'REGIONAL'
					AND team_activity.unit_delivery_team IS NULL
					AND team_activity.location IS NULL
					AND team_activity.contract_course IS NULL
					AND team_activity.funding_source IS NULL
					AND team_activity.remoteness IS NULL
					""")
		'''
		# q515 - tested NOT OK - query did not return any results
		'''
		cur.execute("""
					INSERT INTO team_activity ( location, division, funding_source, contract_course, contract_course_name,
												remoteness, total_target, total_enrolled, total_resulted, unit_delivery_team,
												urban_target, urban_enrolled, urban_resulted, remote_target, remote_enrolled,
												remote_resulted, regional_target, regional_enrolled, regional_resulted,
												interstate_target, interstate_enrolled, interstate_resulted )
					SELECT DISTINCT student_unit_attempt.unit_delivery_location, student_unit_attempt.division,
									student_unit_attempt.unit_funding_source, student_unit_attempt.course_code,
									student_unit_attempt.course_name, student_unit_attempt.delivery_remoteness,
									0 AS expr7, SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									xlookup_team.description, 0 AS expr8, 0 AS expr9, 0 AS expr10, 0 AS expr1,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1,
									0 AS expr5, 0 AS expr4, 0 AS expr6, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code,3) = delivery_location_team
					AND student_unit_attempt.outcome NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_delivery_location,
								student_unit_attempt.division,
								student_unit_attempt.unit_funding_source,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description, expr7, expr8, expr9, expr10,
								expr1, expr5, expr4, expr6, exp13, exp14, exp15
					HAVING student_unit_attempt.unit_funding_source IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'REMOTE'
					""")
		'''
		# q515a - tested NOT OK - query did not return any data
		'''
		cur.execute("""
					UPDATE team_activity
					SET team_activity.total_target = ahc, team_activity.remote_target = ahc
					FROM xlookup_target
					WHERE team_activity.location = xlookup_target.location
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.funding_source = xlookup_target.funding
					AND team_activity.remoteness = 'REMOTE'
					AND team_activity.funding_source IN ('11N','11V','11H')
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q515b - NOT tested NOT OK
		'''
		cur.execute("""
					INSERT INTO team_activity ( unit_delivery_team, division, location, funding_source, contract_course,
												contract_course_name, remoteness, total_target, total_enrolled, total_resulted,
												urban_target, urban_enrolled, urban_resulted, regional_target, regional_enrolled,
												regional_resulted, remote_target, remote_enrolled, remote_resulted, interstate_target,
												interstate_enrolled, interstate_resulted )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location, xlookup_target.funding,
							xlookup_target.contract_course_unit, xlookup_course.description, xlookup_target.remoteness,
							SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1, 0 AS expr2, 0 AS expr7, 0 AS expr8, 0 AS expr9,
							0 AS expr10, 0 AS expr11, 0 AS expr12, SUM(xlookup_target.ahc) AS sum_of_ahc1, 0 AS expr5, 0 AS expr6,
							0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_target.funding = team_activity.funding_source
					AND xlookup_target.contract_course_unit = team_activity.contract_course
					AND xlookup_target.location = team_activity.location
					AND xlookup_target.contract_team = team_activity.unit_delivery_team
					AND xlookup_target.remoteness = team_activity.remoteness
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team,
								xlookup_target.division_school,
								xlookup_target.location,
								xlookup_target.funding,
								xlookup_target.contract_course_unit,
								xlookup_COURSE.description,
								xlookup_target.remoteness, expr1, expr2, expr7, expr8, expr9,
								expr10, expr11, expr12, expr5, expr6,
								team_activity.unit_delivery_team,
								team_activity.location,
								team_activity.contract_course,
								team_activity.funding_source,
								team_activity.remoteness, exp13, exp14, exp15
					HAVING xlookup_target.funding IN ('11N','11V','11H')
					AND xlookup_target.Remoteness = 'REMOTE'
					AND team_activity.unit_delivery_team IS NULL
					AND team_activity.location IS NULL
					AND team_activity.contract_course IS NULL
					AND team_activity.funding_source IS Null
					AND team_activity.remoteness IS NULL
					""")
		'''
		# q516 - tested NOT OK - need to check the implementation of this
		'''
		cur.execute("""
					INSERT INTO team_activity ( funding_source, division, contract_course, contract_course_name,
												total_target, total_enrolled, total_resulted, remoteness,
												unit_delivery_team, urban_target, urban_enrolled, urban_resulted,
												remote_target, remote_enrolled, remote_resulted, regional_target,
												regional_enrolled, regional_resulted, interstate_target,
												interstate_enrolled, interstate_resulted )
					SELECT DISTINCT student_unit_attempt.unit_funding_source, student_unit_attempt.division,
									student_unit_attempt.course_code, student_unit_attempt.course_name,
									0 AS expr7, SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									student_unit_attempt.delivery_remoteness, xlookup_team.description,
									0 AS expr8, SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1, 0 AS expr1,
									0 AS expr2, 0 AS expr3, 0 AS expr5, 0 AS expr6, 0 AS expr4, 0 AS exp13, 0 AS exp14,
									0 AS exp15
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code,3) = delivery_location_team
					AND student_unit_attempt.outcome NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_funding_source,
								student_unit_attempt.division,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description, expr7, expr8, expr1, expr2, expr3, expr5, expr6,
								expr4, exp13, exp14, exp15
					HAVING student_unit_attempt.unit_funding_source NOT IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'URBAN'
					""")
		'''
		# q516a - tested NOT OK - did not return any query results
		'''
		cur.execute("""
					UPDATE team_activity
					SET team_activity.total_target = ahc, team_activity.urban_target = ahc
					FROM xlookup_target
					WHERE team_activity.funding_source = xlookup_target.funding
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.remoteness = xlookup_target.remoteness
					AND team_activity.funding_source NOT IN ('11N','11V','11H')
					AND team_activity.remoteness = 'URBAN'
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q516b - tested NOT OK - did not return query results
		'''
		cur.execute("""
					INSERT INTO team_activity ( unit_delivery_team, division, location, funding_source, contract_course,
												contract_course_name, remoteness, total_target, total_enrolled,
												total_resulted, urban_target, urban_enrolled, urban_resulted,
												regional_target, regional_enrolled, regional_resulted, remote_target,
												remote_enrolled, remote_resulted, interstate_target, interstate_enrolled,
												interstate_resulted )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location,
							xlookup_target.funding, xlookup_target.contract_course_unit, xlookup_course.description,
							xlookup_target.remoteness, SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1, 0 AS expr2,
							SUM(xlookup_target.ahc) AS sum_of_ahc_1, 0 AS expr5, 0 AS expr6, 0 AS expr7, 0 AS expr8,
							0 AS expr9, 0 AS expr10, 0 AS expr11, 0 AS expr12, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_TARGET.contract_team = team_activity.unit_delivery_team
					AND xlookup_target.contract_course_unit = team_activity.contract_course
					AND xlookup_target.funding = team_activity.funding_source
					AND xlookup_target.remoteness = team_activity.remoteness
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team,
								xlookup_target.division_school,
								xlookup_target.location,
								xlookup_target.funding,
								xlookup_target.contract_course_unit,
								xlookup_course.description,
								xlookup_target.remoteness, expr1, expr2, expr5, expr6,
								expr7, expr8, expr9, expr10, expr11, expr12,
								team_activity.unit_delivery_team,
								team_activity.location,
								team_activity.contract_course,
								team_activity.funding_source,
								team_activity.remoteness, exp13, exp14, exp15
					HAVING xlookup_target.funding NOT IN ('11N','11V','11H')
					AND xlookup_target.remoteness = 'URBAN'
					AND team_activity.unit_delivery_team IS NULL
					AND team_activity.location IS NULL
					AND team_activity.contract_course IS NULL
					AND team_activity.funding_source IS NULL
					AND team_activity.remoteness IS NULL
					""")
		'''
		# q517 - tested NOT OK - different number of lines returned from the query
		'''
		cur.execute("""
					INSERT INTO team_activity ( funding_source, division, contract_course, contract_course_name, remoteness, total_target,
												total_enrolled, total_resulted, unit_delivery_team, urban_target, urban_enrolled,
												urban_resulted, remote_target, remote_enrolled, remote_resulted, regional_target,
												regional_enrolled, regional_resulted, interstate_target, interstate_enrolled, interstate_resulted )
					SELECT DISTINCT student_unit_attempt.unit_funding_source, student_unit_attempt.division,
									student_unit_attempt.course_code, student_unit_attempt.course_name,
									student_unit_attempt.delivery_remoteness, 0 AS expr7,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									xlookup_team.description, 0 AS expr8, 0 AS expr9, 0 AS expr10,
									0 AS expr1, 0 AS expr2, 0 AS expr3, 0 AS expr5,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1,
									0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code,3) = delivery_location_team
					AND (student_unit_attempt.outcome) NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_funding_source,
								student_unit_attempt.division,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description, expr7, expr8, expr9, expr10, expr1,
								expr2, expr3, expr5, exp13, exp14, exp15
					HAVING student_unit_attempt.unit_funding_source NOT IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'REGIONAL'
					""")
		'''
		# q517a - tested NOT OK - did not return any data
		'''
		cur.execute("""
					UPDATE team_activity
					SET team_activity.total_target = ahc, team_activity.regional_target = ahc
					FROM xlookup_target
					WHERE team_activity.funding_source = xlookup_target.funding
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.remoteness = xlookup_target.remoteness
					AND team_activity.remoteness = 'REGIONAL'
					AND team_activity.funding_source NOT IN ('11N','11V','11H')
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q517b - tested NOT OK - did not return any data need to check
		'''
		cur.execute("""
					INSERT INTO team_activity ( unit_delivery_team, division, location, funding_source,
												contract_course, contract_course_name, remoteness, total_target,
												total_enrolled, total_resulted, urban_target, urban_enrolled,
												urban_resulted, regional_target, regional_enrolled, regional_resulted,
												remote_target, remote_enrolled, remote_resulted, interstate_target,
												interstate_enrolled, interstate_resulted )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.Location,
							xlookup_target.Funding, xlookup_target.contract_course_unit, xlookup_course.description,
							xlookup_target.remoteness, SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1, 0 AS expr2,
							0 AS expr7, 0 AS expr8, 0 AS expr9, SUM(xlookup_target.ahc) AS sum_of_ahc1, 0 AS expr5,
							0 AS expr6, 0 AS expr10, 0 AS expr11, 0 AS expr12, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_target.remoteness = team_activity.remoteness
					AND xlookup_target.contract_course_unit = team_activity.contract_course
					AND xlookup_target.funding = team_activity.funding_source
					AND xlookup_target.contract_team = team_activity.unit_delivery_team
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team,
								xlookup_target.division_school,
								xlookup_target.Location,
								xlookup_target.Funding,
								xlookup_target.contract_course_unit,
								xlookup_COURSE.Description,
								xlookup_target.Remoteness, expr1, expr2, expr7, expr8, expr9, expr5,
								expr6, expr10, expr11, expr12, team_activity.unit_delivery_team, team_activity.location,
								team_activity.contract_course, team_activity.funding_source, team_activity.remoteness,
								exp13, exp14, exp15
					HAVING xlookup_target.Funding NOT IN ('11N','11V','11H')
					AND xlookup_target.Remoteness = 'REGIONAL'
					AND TEAM_ACTIVITY.unit_delivery_team IS NULL
					AND TEAM_ACTIVITY.location IS NULL
					AND TEAM_ACTIVITY.contract_course IS NULL
					AND TEAM_ACTIVITY.funding_source IS NULL
					AND TEAM_ACTIVITY.remoteness IS NULL
					""")
		'''
		# q518 - tested NOT OK - query returned a different number of results (needs further checking)
		'''
		cur.execute("""
					INSERT INTO team_activity ( funding_source, division, contract_course, contract_course_name,
												remoteness, total_target, total_enrolled, total_resulted,
												unit_delivery_team, urban_target, urban_enrolled, urban_resulted,
												remote_target, remote_enrolled, remote_resulted, regional_target,
												regional_enrolled, regional_resulted, interstate_target,
												interstate_enrolled, interstate_resulted )
					SELECT DISTINCT student_unit_attempt.unit_funding_source, student_unit_attempt.division,
									student_unit_attempt.course_code, student_unit_attempt.course_name,
									student_unit_attempt.delivery_remoteness, 0 AS expr7,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									xlookup_team.description, 0 AS expr8, 0 AS expr9, 0 AS expr10, 0 AS expr1,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1,
									0 AS expr5, 0 AS expr4, 0 AS expr6, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code,3) = delivery_location_team
					AND student_unit_attempt.outcome NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_funding_source,
								student_unit_attempt.division,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description, expr7, expr8, expr9, expr10, expr1,
								expr5, expr4, expr6, exp13, exp14, exp15
					HAVING student_unit_attempt.unit_funding_source NOT IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'REMOTE'
					""")
		'''
		# q518a - tested NOT OK - query did not return any data
		'''
		cur.execute("""
					UPDATE team_activity
					SET team_activity.total_target = ahc, team_activity.remote_target = ahc
					FROM xlookup_target
					WHERE team_activity.remoteness = xlookup_target.remoteness
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.funding_source = xlookup_target.funding
					AND team_activity.remoteness = 'REMOTE'
					AND team_activity.funding_source NOT IN ('11N','11V','11H')
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q518b - tested NOT OK - 
		'''
		cur.execute("""
					INSERT INTO TEAM_ACTIVITY ( unit delivery team, division, location, funding source, contract course,
												contract course name, remoteness, total target, total enrolled,
												total resulted, urban target, urban enrolled, urban resulted,
												regional target, regional enrolled, regional resulted, remote target,
												remote enrolled, remote resulted, interstate target, interstate enrolled,
												interstate resulted )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location,
							xlookup_target.funding, xlookup_target.contract_course_unit, xlookup_course.description,
							xlookup_target.remoteness, SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1, 0 AS expr2,
							0 AS expr7, 0 AS expr8, 0 AS expr9, 0 AS expr10, 0 AS expr11, 0 AS expr12,
							SUM(xlookup_target.ahc) AS sum_of_ahc1, 0 AS expr5, 0 AS expr6, 0 AS exp13, 0 AS exp14, 0 AS exp15
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_target.contract_team = team_activity.unit_delivery_team
					AND xlookup_target.remoteness = team_activity.remoteness
					AND xlookup_target.funding = team_activity.funding_source
					AND xlookup_target.contract_course_unit = team_activity.contract_course
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team,
								xlookup_target.division_school,
								xlookup_target.location,
								xlookup_target.funding,
								xlookup_target.contract_course_unit,
								xlookup_course.description,
								xlookup_target.remoteness, expr1, expr2, expr7, expr8,
								expr9, expr10, expr11, expr12, expr5, expr5,
								team_activity.unit_delivery_team,
								team_activity.location,
								team_activity.contract_course,
								team_activity.funding_source,
								team_activity.remoteness, exp13, exp14, exp15
					HAVING xlookup_target.funding NOT IN ('11N','11V','11H')
					AND xlookup_target.remoteness = 'REMOTE'
					AND team_activity.unit_delivery_team IS NULL
					AND team_activity.location IS NULL
					AND team_activity.contract_course IS NULL
					AND team_activity.funding_source IS NULL
					AND team_activity.remoteness IS NULL
					""")
		'''
		# q519 - tested NOT OK - query did not return any data
		'''
		cur.execute("""
					INSERT INTO team_activity ( funding_source, division, contract_course, contract course name,
												remoteness, total target, total enrolled, total resulted,
												unit delivery team, urban target, urban enrolled, urban resulted,
												remote target, remote enrolled, remote resulted, regional target,
												regional enrolled, regional resulted, interstate target, interstate enrolled,
												interstate resulted )
					SELECT DISTINCT student_unit_attempt.unit_funding_source, student_unit_attempt.division, student_unit_attempt.course_code,
									student_unit_attempt.course_name, student_unit_attempt.delivery_remoteness, 0 AS expr7,
									SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc, SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc,
									xlookup_team.description, 0 AS expr8, 0 AS expr9, 0 AS expr10, 0 AS expr1, 0 AS exp11,
									0 AS exp12, 0 AS expr5, 0 AS expr4, 0 AS expr6, 0 AS exp13, SUM(student_unit_attempt.enrolled_ahc) AS sum_of_enrolled_ahc1,
									SUM(student_unit_attempt.resulted_ahc) AS sum_of_resulted_ahc1
					FROM student_unit_attempt, xlookup_team
					WHERE LEFT(code,3) = delivery_location team
					AND student_unit_attempt.outcome NOT IN ('SW','NS','CT','RPL-CA')
					GROUP BY 	student_unit_attempt.unit_funding_source,
								student_unit_attempt.division,
								student_unit_attempt.course_code,
								student_unit_attempt.course_name,
								student_unit_attempt.delivery_remoteness,
								xlookup_team.description, expr7, expr8, expr9, expr10,
								expr1, exp11, exp12, expr5, expr4, expr6, exp13
					HAVING student_unit_attempt.unit_funding_source NOT IN ('11N','11V','11H')
					AND student_unit_attempt.delivery_remoteness = 'INTERSTATE'
					""")
		'''
		# q519a - tested NOT OK - did not return any data
		'''
		cur.execute("""
					UPDATE team_activity
					SET team_activity.total_target = ahc, team_activity.interstate_target = ahc
					FROM xlookup_target
					WHERE team_activity.funding_source = xlookup_target.funding
					AND team_activity.unit_delivery_team = xlookup_target.contract_team
					AND team_activity.contract_course = xlookup_target.contract_course_unit
					AND team_activity.remoteness = xlookup_target.remoteness
					AND team_activity.remoteness = 'INTERSTATE'
					AND team_activity.funding_source NOT IN ('11N','11V','11H')
					AND xlookup_target.ahc <> 0
					""")
		'''
		# q519b - tested NOT OK did not return any data
		'''
		cur.execute("""
					INSERT INTO TEAM_ACTIVITY ( unit_delivery_team, division, location, funding_source, contract_course,
												contract_course_name, remoteness, total_target, total_enrolled, total_resulted,
												urban_target, urban_enrolled, urban_resulted, regional_target,
												regional_enrolled, regional_resulted, remote_target, remote_enrolled,
												remote_resulted, interstate_target )
					SELECT 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location, xlookup_target.funding,
							xlookup_target.contract_course_unit, xlookup_course.description, xlookup_target.remoteness,
							SUM(xlookup_target.ahc) AS sum_of_ahc, 0 AS expr1, 0 AS expr2, 0 AS expr7, 0 AS expr8,
							0 AS expr9, 0 AS expr10, 0 AS expr11, 0 AS expr12, 0 AS exp13, 0 AS expr5, 0 AS expr6,
							SUM(xlookup_target.ahc) AS sum_of_ahc_1
					FROM xlookup_target
					LEFT JOIN team_activity
					ON xlookup_target.contract_course_unit = team_activity.contract_course
					AND xlookup_target.funding = team_activity.funding_source
					AND xlookup_target.remoteness = team_activity.remoteness
					AND xlookup_target.contract_team = team_activity.unit_delivery_team
					INNER JOIN xlookup_course ON xlookup_target.contract_course_unit = xlookup_course.code
					GROUP BY 	xlookup_target.contract_team, xlookup_target.division_school, xlookup_target.location,
								xlookup_target.funding, xlookup_target.contract_course_unit, xlookup_course.description,
								xlookup_target.remoteness, team_activity.unit_delivery_team, team_activity.location,
								team_activity.contract_course, team_activity.funding_source, team_activity.remoteness,
								expr1, expr2, expr7, expr8, expr9, expr10, expr11, expr12, exp13, expr5, expr6
					HAVING xlookup_target.funding NOT IN ('11N','11V','11H')
					AND xlookup_target.remoteness = 'INTERSTATE'
					AND team_activity.unit_delivery_team IS NULL
					AND team_activity.location IS NULL
					AND team_activity.contract_course IS NULL
					AND team_activity.funding_source IS NULL
					AND team_activity.remoteness IS NULL
					""")
		'''
		# q520 - NOT tested NOT OK (not sure if implemented correctly)
		
		cur.execute("""
					SELECT DISTINCT weekly_current.delivery_location_team, weekly_current.course_admin_team,
									weekly_current.student_id, weekly_current.atsi, weekly_current.age,
									xlookup_age_group.age_range, weekly_current.disability_flag,
									weekly_current.employment_category, xlookup_employment_status.employment_status_description,
									weekly_current.residential_postcode, weekly_current.highest_school_level_completed_code,
									xlookup_school_level.school_level_description, weekly_current.highest_school_level_completed_year,
									weekly_current.birth_country_code, xlookup_country.full_name AS birth_country_name,
									weekly_current.home_language_code, xlookup_language.full_name AS home_language_name,
									weekly_current.highest_prior_education_level_completed_code,
									xlookup_prior_education_level.description AS prior_education_level,
									weekly_current.at_school_indicator, weekly_current.vet_in_school_indicator,
									weekly_current.course_industry, xlookup_det_industry.description AS course_industry_description,
									xlookup_foe2.description AS foe2_description, xlookup_foe4.description AS foe4_description,
									xlookup_course.level AS course_level, xlookup_level.description AS course_level_description,
									weekly_current.course_code, xlookup_course.description AS course_name,
									weekly_current.unit_code, weekly_current.unit_name, weekly_current.unit_funding_source,
									weekly_current.grade, weekly_current.unit_delivery_location, weekly_current.enrol_date,
									weekly_current.result_date, weekly_current.outcome, weekly_current.fee_category,
									weekly_current.enrolled_ahc, weekly_current.resulted_ahc, vet_apprentice.api_id,
									vet_apprentice.api_start_date, vet_apprentice.api_end_date, vet_apprentice.addr_type,
									vet_apprentice.addr_start_date, vet_apprentice.addr_end_date, vet_apprentice.addr_line1,
									vet_apprentice.addr_line2, vet_apprentice.addr_line3, vet_apprentice.addr_line4,
									vet_apprentice.addr_line5, format(addr_aust_postcode,"0000") AS addr_aust_pc,
									vet_apprentice.phone_1, vet_apprentice.phone_2, vet_apprentice.phone_3, vet_apprentice.other_details
					INTO apprentice_mega
					FROM xlookup_foe2
					INNER JOIN xlookup_level
						INNER JOIN xlookup_course ON xlookup_LEVEL.Level Code = xlookup_course.Level
					ON xlookup_foe2.code = xlookup_course.foe2
					INNER JOIN xlookup_foe4 ON xlookup_course.foe4 = xlookup_foe4.code
					INNER JOIN xlookup_language
					INNER JOIN (weekly_current
						INNER JOIN xlookup_country ON weekly_current.birth_country_code = xlookup_country.identifier
					ON xlookup_Language.identifier = weekly_current.home_language_code
					INNER JOIN xlookup_prior_education_level ON weekly_current.highest_prior_education_level_completed_code = xlookup_prior_education_level.level_code
					INNER JOIN xlookup_det_industry ON weekly_current.course_industry = xlookup_det_industry.code
					INNER JOIN xlookup_age_group ON weekly_current.age = xlookup_age_group.age
					INNER JOIN xlookup_school_level ON weekly_current.highest_school_level_completed_code = xlookup_school_level.school_level_code
					INNER JOIN xlookup_employment_status ON weekly_current.employment_category = xlookup_employment_status.employment_status_code ON xlookup_course.code = weekly_current.course_code
					INNER JOIN vet_apprentice
					ON weekly_current.tci = vet_apprentice.api_id
					AND weekly_current.student_id = vet_apprentice.person_id
					AND weekly_current.unit_code = vet_apprentice.unit_cd
					AND weekly_current.course_code = vet_apprentice.course_code
					""")
		
		# q521 - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT DISTINCT delivery_location_team, student_id,
									atsi, age_range, disability_flag,
									employment_category,
									employment_status_description AS employment_category_description,
									residential_postcode, highest_school_level_completed_code,
									school_level_description AS highest_school_level_completed,
									highest_school_level_completed_year,
									birth_country_name AS country_of_birth,
									home_language_name AS language,
									prior_education_level AS highest_prior_education_level_completed,
									at_school_indicator, vet in school_indicator,
									course_industry,
									course_industry_description AS course_industry_name,
									foe_2_description AS foe_2,
									foe_4_description AS foe_4,
									course_level_description AS course_level_description,
									course_code, unit_code,
									fee_category, unit_funding_source,
									Grade, unit_delivery_location,
									enrol_date, result_date, api_id AS tci,
									api_start_date AS tci_start_date, api_end_date AS tci_end_date,
									enrolled_ahc, resulted_ahc
									INTO apprentice_sua
					FROM apprentice_mega
					WHERE apprentice_mega.api_end_date is NULL
					""")
		'''
		# q522 - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT DISTINCT course_admin_team, student_id, atsi, age_range, disability_flag, employment_category,
									employment_status_description AS employment_category_description, residential_postcode,
									highest_school_level_completed_code, school_level_description AS highest_school_level_completed,
									highest_school_level_completed_year, birth_country_name AS country_of_birth,
									home_language_name AS language, prior_education_level AS highest_prior_education_level_completed,
									at_school_indicator, course_industry_description AS industry, foe2_description AS foe2,
									foe4_description AS foe4, course_level_description AS course_level_description, course_code,
									course_name, unit_funding_source, api_id AS tci, api_start_date AS tci_start_date,
									api_end_date AS tci_end_date, SUM(enrolled_ahc) AS sum_of_enrolled_ahc,
									sum(resulted_ahc) AS sum_of_resulted_ahc, addr_start_date AS address_start_date,
									addr_end_date AS address_end_date, addr_line1 AS employer_or_business_name,
									addr_line2 AS employer_address_line_1, addr_line3 AS employer_address_line_2,
									addr_line4 AS employer_suburb, addr_line5 AS employer_state, addr_aust_pc AS employer_postcode,
									phone_1 AS employer_phone_number, phone_2 AS employer_fax_number, phone_3 AS employer_contact_name,
									other_details AS employer_email_details
					INTO apprentice_course
					FROM apprentice_mega
					GROUP BY 	apprentice_mega.course_admin_team,
								apprentice_mega.student_id,
								apprentice_mega.atsi,
								apprentice_mega.age_range,
								apprentice_mega.disability_flag,
								apprentice_mega.employment_category,
								apprentice_mega.employment_status_description,
								apprentice_mega.residential_postcode,
								apprentice_mega.highest_school_level_completed_code,
								apprentice_mega.school_level_description,
								apprentice_mega.highest_school_level_completed_year,
								apprentice_mega.birth_country_name,
								apprentice_mega.home_language_name,
								apprentice_mega.prior_education_level,
								apprentice_mega.at_school_indicator,
								apprentice_mega.course_industry_description,
								apprentice_mega.foe2_description,
								apprentice_mega.foe4_description,
								apprentice_mega.course_level_description,
								apprentice_mega.course_code,
								apprentice_mega.course_name,
								apprentice_mega.unit_funding_source,
								apprentice_mega.api_id,
								apprentice_mega.api_start_date,
								apprentice_mega.api_end_date,
								apprentice_mega.addr_start_date,
								apprentice_mega.addr_end_date,
								apprentice_mega.addr_line1,
								apprentice_mega.addr_line2,
								apprentice_mega.addr_line3,
								apprentice_mega.addr_line4,
								apprentice_mega.addr_line5,
								apprentice_mega.addr_aust_pc,
								apprentice_mega.phone_1,
								apprentice_mega.phone_2,
								apprentice_mega.phone_3,
								apprentice_mega.other_details,
								apprentice_mega.addr_type
					HAVING apprentice_mega.api_end_date IS NULL
					AND apprentice_mega.addr_end_date IS NULL
					AND apprentice_mega.addr_type = 'EMPLOYER'
					ORDER BY apprentice_mega.student_id
					""")
		'''
		# q524 - NOT tested NOT OK
		'''
		cur.execute("""
					INSERT INTO vet_course_completions_2018 ( 	student_id, student_last_name, student_first_name,
																student_gender, student_dob, student_email_address,
																course_code, course_name, course_commencement_date,
																course_attempt_status, course_requirements_completed_date,
																sca_funding_source, course_admin_location, course_admin_team,
																course_delivery_mode, study_reason, study_reason_description,
																vet_in_school_indicator, unit_only_enrolment_indicator,
																highest_school_level_completed, highest_school_level_completed_code,
																highest_school_level_completed_year, residential_postcode,
																home_language_code, birth_country_code, at_school_indicator,
																atsi, employment_category, employment_category_description,
																conferral_date, vet_school_name, usi_flag,
																entitlement_contract_description )
					SELECT 	vet_course_completions.student_id, vet_course_completions.student_last_name,
							vet_course_completions.student_first_name, vet_course_completions.student_gender,
							vet_course_completions.student_dob, vet_course_completions.student_email_address,
							vet_course_completions.course_code, vet_course_completions.course_name,
							vet_course_completions.course_commencement_date, vet_course_completions.course_attempt_status,
							vet_course_completions.course_requirements_completed_date, vet_course_completions.sca_funding_source,
							vet_course_completions.course_admin_location, vet_course_completions.course_admin_team,
							vet_course_completions.course_delivery_mode, vet_course_completions.study_reason, '' AS study_reason_description,
							vet_course_completions.vet_in_school_indicator, vet_course_completions.unit_only_enrolment_indicator, "" AS highest_school_level_completed,
							vet_course_completions.highest_school_level_completed_code, vet_course_completions.highest_school_level_completed_year,
							vet_course_completions.residential_postcode, vet_course_completions.home_language_code,
							vet_course_completions.birth_country_code, vet_course_completions.at_school_indicator,
							(CASE
								WHEN atsi_status IN ('1','2','3') THEN 'Y'
								WHEN atsi_status IN ('@','4') THEN 'N'
							END) AS atsi,
							vet_course_completions.employment_category, '' AS employment_category_description,
							vet_course_completions.conferral_date, vet_course_completions.vet_school_name,
							vet_course_completions.usi_flag, vet_course_completions.entitlement_contract_description
					FROM vet_course_completions
					""")
		'''
		# q524a - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE vet_course_completions_2018
					SET study_reason_description = study_reason_description
					FROM xlookup_study_reason
					WHERE vet_course_completions_2018.study_reason = xlookup_study_reason.study_reason_id
					""")
		'''
		# q524b - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE vet_course_completions_2018
					SET highest_school_level_completed = school_level_description
					FROM xlookup_school_level
					WHERE vet_course_completions_2018.highest_school_level_completed_code = xlookup_school_level.school_level_code
					""")
		'''
		# q524c - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE vet_course_completions_2018
					SET vet_course_completions_2018.highest_school_level_completed_year = '@@@@'
					WHERE vet_course_completions_2018.highest_school_level_completed_year is NULL
					OR vet_course_completions_2018.highest_school_level_completed_year=''
					""")
		'''
		# q524d - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE vet_course_completions_2018
					SET vet_course_completions_2018.employment_category_description = employment_status_description
					FROM xlookup_employment_status
					WHERE vet_course_completions_2018.employment_category = xlookup_employment_status.employment_status_code
					""")
		'''
		# q530 - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT xref_etp_sca.division, xref_etp_sca.unit_delivery_team, xref_etp_sca.course_code,
					xref_etp_sca.number_of_units_to_complete, xref_etp_sca.target_sca,
					xref_etp_sca.successful_ahc_ca_rpl, xref_etp_sca.funded_enrolled_sca,
					xref_etp_sca.funded_enrolled_ahc, xref_etp_sca.team_target_ahc
					INTO etp_activity
					FROM xref_etp_sca;
					""")
		'''
		# q531a - NOT tested NOT OK
		'''
		cur.execute("""
					INSERT INTO etp_activity ( division, unit_delivery_team, team_target_ahc, target_sca )
					SELECT 	xlookup_etp_targets.division, xlookup_etp_targets.unit_delivery_team,
							xlookup_etp_targets.team_target_ahc, xlookup_etp_targets.team_target_headcount
					FROM xlookup_etp_targets
					""")
		'''
		# q532a - NOT tested NOT OK - not fully implemented properly
		'''
		cur.execute("""
					INSERT INTO etp_activity ( 	division, unit_delivery_team, course_code, successful_ahc_ca_rpl,
												funded_enrolled_sca, funded_enrolled_ahc )
					SELECT 	xlookup_division.division, xlookup_team.description, weekly_current.course_code,
							0 AS expr1, 0 AS expr2, SUM(weekly_current.enrolled_ahc) AS sum_of_enrolled_ahc
					FROM weekly_current
					INNER JOIN xlookup_team
						INNER JOIN xlookup_division ON xlookup_team.code = xlookup_division.team_code
					ON weekly_current.delivery_location_team = xlookup_division.team_code
					WHERE weekly_current.grade IS NULL
					AND xlookup_team.current_2018 = 'Y'
					AND weekly_current.unit_funding_source = 'ETP'
					OR weekly_current.grade NOT IN ('CT','NS','SW','RPL-CA')
					AND xlookup_team.Current_2018 = 'Y'
					AND weekly_current.unit_funding_source = 'ETP'
					GROUP BY 	xlookup_division.division,
								xlookup_team.description,
								weekly_current.course_code, expr1, expr2
					HAVING weekly_current.course_code <> 'LRNSUPP'
					OR weekly_current.course_code <> 'LRNSUPP'
					""")
		'''
		# q532b - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT DISTINCT xlookup_division.division, xlookup_team.description, weekly_current.student_id,
									weekly_current.course_code
					INTO q532b_distinct_funded_enrolled_etp_headcount
					FROM weekly_current
					INNER JOIN xlookup_division ON weekly_current.course_admin_team = xlookup_division.team_code
					INNER JOIN xlookup_team ON xlookup_division.team_code = xlookup_team.code
					WHERE (xlookup_team.current_2018 = 'Y'
					AND weekly_current.grade NOT IN ('CT','NS','SW','RPL-CA')
					AND weekly_current.unit_funding_source = 'ETP')
					OR (xlookup_team.current_2018 = 'Y'
					AND weekly_current.grade IS NULL
					AND weekly_current.unit_funding_source = 'ETP')
					GROUP BY 	xlookup_division.division,
								xlookup_team.description,
								weekly_current.student_id,
								weekly_current.course_code
					HAVING weekly_current.course_code <> 'LRNSUPP'
					OR weekly_current.course_code <> 'LRNSUPP'
					""")
		'''
		# q532c - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT division, description, course_code, COUNT(student_id) AS count_of_student_id
					INTO q532c_count_distinct_funded_enrolled_etp_sca
					FROM q532b_distinct_funded_enrolled_etp_headcount
					GROUP BY division, description, course_code
					""")
		'''
		# q532d - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE etp_activity
					SET funded_enrolled_sca = count_of_student_id
					FROM q532c_count_distinct_funded_enrolled_etp_sca
					WHERE etp_activity.division = q532c_count_distinct_funded_enrolled_etp_sca.division
					AND q532c_count_distinct_funded_enrolled_etp_sca.description = etp_activity.unit_delivery_team
					AND q532c_count_distinct_funded_enrolled_etp_sca.course_code = etp_activity.course_code
					""")
		'''
		# q534a - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT xlookup_division.division, xlookup_team.description, weekly_current.course_code, Sum(weekly_current.resulted_ahc) AS successful_ahc_ca_rpl
					INTO q534a_successful_etp_ahc
					FROM weekly_current
					INNER JOIN (xlookup_team
								INNER JOIN xlookup_division
								ON xlookup_team.code = xlookup_division.team_code)
					ON weekly_current.delivery_location_team = xlookup_team.code
					WHERE weekly_current.grade in ('RPL','CA')
					AND weekly_current.unit_attempt_status in ('COMPLETED','GRANTED')
					AND weekly_current.unit_funding_source='ETP'
					AND xlookup_team.current_2018='Y'
					GROUP BY xlookup_division.division, xlookup_team.description, weekly_current.course_code
					HAVING weekly_current.course_code<>'LRNSUPP'
					""")
		'''
		# q534b - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE q534a_successful_etp_ahc
					SET etp_activity.successful_ahc_ca_rpl = q534a_successful_etp_ahc.successful_ahc_ca_rpl
					FROM etp_activity
					WHERE q534a_successful_etp_ahc.course_code = etp_activity.course_code
					AND q534a_successful_etp_ahc.description = etp_activity.unit_delivery_team
					AND q534a_successful_etp_ahc.division = etp_activity.division
					""")
		'''
		# q999a - NOT tested NOT OK
		'''
		cur.execute("""
					SELECT 	delivery_location_team, student_id, unit_code, unit_attempt_status, teaching_period,
							grade, enrol_date, override_activity_start_date, result_date, enrolment_activity_end_date,
							Course Code, Unit Funding Source,
							(CASE
								WHEN override_activity_start_date IS NULL THEN enrol_date
								ELSE override_activity_start_date
							END) AS start_date,
							(CASE
								WHEN result_date IS NULL THEN enrolment_activity_end_date
								ELSE result_date
							END) AS end_date,
							'' AS status
					FROM errors_sua_duplicates_exc_sw_ct_ns_douglas_to_check
					ORDER BY 	student_id,
								unit_code,
								(CASE
									WHEN override_activity_start_date IS NULL THEN enrol_date
									ELSE override_activity_start_date
								END)
					""")
		'''
		# q999b - NOT tested NOT OK
		'''
		cur.execute("""
					UPDATE errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked
					INNER JOIN errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked AS errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked_1
					ON errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked.student_id = errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked_1.student_id)
					AND errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked.unit_code = errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked_1.unit_code)
					SET errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked.status = errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked_1.status
					WHERE errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked.status = 'TO BE UPDATED'
					AND errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check_checked_1.status <> 'TO BE UPDATED'
					""")
		'''
		# q999c - this check SUA will need to be implemented using Python it has a non-standard script
		'''
		cur.execute("""
					SELECT 	Delivery Location Team, Student ID, Unit Code, Unit Attempt Status, Teaching Period, Grade,
							Enrol Date, Override Activity Start Date, Result Date, Enrolment Activity End Date,
							Course Code, Unit Funding Source,
							(CASE
								WHEN override_activity_start_date IS NULL THEN enrol_date
								ELSE override_activity_start_date
							END) AS start_date,
							(CASE
								WHEN result_date IS NULL THEN enrolment_activity_end_date
								ELSE result_date
							END) AS end_date
							CheckSUA(Student ID,Unit Code,Grade,Start Date,End Date,Course Code,Result Date) AS Status INTO ERRORS SUA DUPLICATES (exc SW/CT/NS) DOUGLAS TO CHECK_CHECKED
					FROM errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check
					ORDER BY errors_sua_duplicates_ex_sw_ct_ns_douglas_to_check.Student ID, ERRORS SUA DUPLICATES (exc SW/CT/NS) DOUGLAS TO CHECK.[Unit Code, IIf(IsNull([Override Activity Start Date]),[Enrol Date],[Override Activity Start Date]);
					""")
		'''
		# q999d - has not been implemented correctly
		'''
		cur.execute("""
					SELECT [ERRORS SUPERSEDED UNITS - DOUGLAS].[Course Admin Team], [ERRORS SUPERSEDED UNITS - DOUGLAS].[Student ID], IIf([UNIT CODE DESCRIPTION]='SUPERSEDED',[RELATED UNIT],[Unit Code]) AS [Current Unit Code], [ERRORS SUPERSEDED UNITS - DOUGLAS].[Unit Code], [ERRORS SUPERSEDED UNITS - DOUGLAS].[RELATED UNIT], [ERRORS SUPERSEDED UNITS - DOUGLAS].[Course Code], [ERRORS SUPERSEDED UNITS - DOUGLAS].[Override Activity Start Date], [ERRORS SUPERSEDED UNITS - DOUGLAS].[Result Date], [ERRORS SUPERSEDED UNITS - DOUGLAS].[Override Activity End Date], [ERRORS SUPERSEDED UNITS - DOUGLAS].Grade, [ERRORS SUPERSEDED UNITS - DOUGLAS].[Teaching Period], [ERRORS SUPERSEDED UNITS - DOUGLAS].[UNIT CODE DESCRIPTION], xlookup_Ntis_superseded_unit_equivalent_flag.equivalent
					FROM [ERRORS SUPERSEDED UNITS - DOUGLAS]
					LEFT JOIN xlookup_Ntis_superseded_unit_equivalent_flag ON ([ERRORS SUPERSEDED UNITS - DOUGLAS].[RELATED UNIT] = xlookup_Ntis_superseded_unit_equivalent_flag.identifier) AND ([ERRORS SUPERSEDED UNITS - DOUGLAS].[Unit Code] = xlookup_Ntis_superseded_unit_equivalent_flag.superseding_identifier)
					ORDER BY [ERRORS SUPERSEDED UNITS - DOUGLAS].[Student ID], IIf([UNIT CODE DESCRIPTION]='SUPERSEDED',[RELATED UNIT],[Unit Code]), [ERRORS SUPERSEDED UNITS - DOUGLAS].[Result Date];
					""")
		'''
		# q999z - has not been implemented correctly
		'''
		cur.execute("""
					SELECT WEEKLY_CURRENT.[Teaching Period], WEEKLY_CURRENT.[Course Admin Team], WEEKLY_CURRENT.[Student ID], WEEKLY_CURRENT.[Unit Funding Source], WEEKLY_CURRENT.[Course Code], WEEKLY_CURRENT.[Fee Category], WEEKLY_CURRENT.[Unit Code], WEEKLY_CURRENT.[Override Activity Start Date], WEEKLY_CURRENT.[Course Commencement Date] INTO [ERROR - 2018 NOT REPORTED TLS-TL0 - DOUGLAS]
					FROM WEEKLY_CURRENT
					WHERE (((WEEKLY_CURRENT.[Unit Funding Source]) In ("TLS","TL0")));
					""")
		'''
		##################################################
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