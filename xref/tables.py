#!/usr/bin/python

tables = {
	'xref_error_for_correction_template': 			"""
													CREATE TABLE {} (
														error_type text,
														course_admin_team text,
														delivery_location_team text,
														teaching_period text,
														student_id text,
														student_last_name text,
														student_first_name text,
														atsi text,
														gender text,
														dob date,
														deceased_indicator text,
														disability text,
														home_language_code text,
														birth_country_code text,
														residential_post_code text,
														home_state text,
														prior_education text,
														employment_category text,
														at_school_indicator text,
														vet_in_school_indicator text,
														highest_school_level_completed_code text,
														highest_school_level_completed_year text,
														age_highest_school_completed text,
														course_code text,
														unit_code text,
														unit_funding_source text,
														enrol_date date,
														outcome text,
														unit_attempt_status text,
														study_reason text,
														intention_to_complete_course text,
														intention_to_complete_units_only text,
														no_course_intention text,
														total_lrnsupp_ahc text,
														total_enrolled_ahc text,
														granted_date date,
														cancelled_date date,
														not_approved_date date,
														usi_flag text,
														entitlement_contract_description text,
														course_commencement_date date,
														course_attempt_status text
													)
													""",
	'xref_vet_course_completions_YYYY_template':	"""
													CREATE TABLE {} (
														at_school_indicator text,
														atsi text,
														basis_for_admission_code text,
														birth_country_code text,
														chessn text,
														conferral_date date,
														course_admin_location text,
														course_admin_team text,
														course_attempt_status text,
														course_code text,
														course_commencement_date date,
														course_delivery_mode text,
														course_name text,
														course_requirements_completed_date date,
														employment_category text,
														employment_category_description text,
														entitlement_contract_description text,
														hecs_payment_option_code text,
														highest_school_level_completed text,
														highest_school_level_completed_code text,
														highest_school_level_completed_year text,
														home_language_code text,
														no_course_intention text,
														residential_postcode text,
														sca_funding_source text,
														student_dob date,
														student_email_address text,
														student_first_name text,
														student_gender text,
														student_id text,
														student_last_name text,
														study_reason text,
														study_reason_description text,
														unit_only_enrolment_indicator text,
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
														vfh_term_location_postcode text
													)
													""",
	'xref_weekly_template':							"""
													CREATE TABLE weekly_{} (
														teaching_period text,
														student_id text,
														course_admin_team text,
														unit_delivery_location text,
														delivery_location_team text,
														unit_funding_source text,
														course_delivery_mode text,
														course_code text,
														fee_category text,
														course_name text,
														unit_code text,
														unit_name text,
														enrolled_ahc numeric,
														resulted_ahc numeric,
														grade text,
														atsi text,
														course_industry text,
														student_last_name text,
														student_first_name text,
														aci text,
														tci text,
														student_dob date,
														override_activity_end_date date,
														unit_attempt_status text,
														correspondence_category text,
														student_gender text,
														student_home_state text,
														grade_keyed text,
														vet_school_name text,
														unit_delivery_type text,
														enrol_date date,
														disc_date date,
														result_date date,
														staff_indicator text,
														stream_code text,
														study_reason text,
														granted_date date,
														vet_in_school_indicator text,
														at_school_indicator text,
														highest_prior_education_level_completed_code text,
														home_language_code text,
														birth_country_code text,
														highest_school_level_completed_code text,
														highest_school_level_completed_year text,
														residential_postcode text,
														employment_category text,
														disability_flag text,
														course_attempt_status text,
														course_commencement_date date,
														sca_funding_source text,
														enrolment_activity_end_date date,
														postal_postcode text,
														override_activity_start_date date,
														intention_to_complete_course text,
														intention_to_complete_unit_only text,
														no_course_intention text,
														course_requirements_completed_indicator text,
														course_requirements_completed_date date,
														result_type text,
														unit_contact text,
														cancelled_date date,
														not_approved_date date,
														administrative_unit_status text,
														chessn text,
														vfh_atsi_code text,
														vfh_citizenship_code text,
														vfh_birth_country_code text,
														vfh_home_language_code text,
														vfh_term_location_postcode text,
														vfh_term_location_country_code text,
														vfh_home_location_postcode text,
														vfh_home_location_country_code text,
														vfh_arrival_year text,
														vfh_permanent_resident_code text,
														vfh_commencing_location_postcode text,
														vfh_commencing_geographic_location text,
														vfh_highest_attainment_code text,
														vfh_highest_attainment_year text,
														basis_for_admission_code text,
														hecs_payment_option_code text,
														unit_student_status_code text,
														unit_census_date date,
														usi_flag text,
														deceased_indicator text,
														entitlement_contract_description text,
														email_address text,
														mobile_phone_number text,
														contract_course_unit_name text,
														contract_course_unit_code text,
														contract text,
														outcome text,
														age numeric,
														teaching_period_end_date date,
														enrol_week numeric,
														result_week numeric,
														contract_team text,
														ur_outcome text
													)
													""",
	'xref_course_completions':						"""
													CREATE TABLE vet_course_completions (
														student_id text,
														student_last_name text,
														student_first_name text,
														student_gender text,
														student_dob date,
														student_email_address text,
														course_code text,
														course_name text,
														course_commencement_date date,
														course_attempt_status text,
														course_requirements_completed_date date,
														sca_funding_source text,
														course_admin_location text,
														course_admin_team text,
														course_delivery_mode text,
														study_reason text,
														vet_in_school_indicator text,
														unit_only_enrolment_indicator text,
														highest_school_level_completed_code text,
														highest_school_level_completed_year text,
														residential_postcode text,
														home_language_code text,
														birth_country_code text,
														at_school_indicator text,
														atsi_status text,
														employment_category text,
														conferral_date date,
														vet_school_name text,
														no_course_intention text,
														chessn text,
														vfh_atsi_code text,
														vfh_citizenship_code text,
														vfh_birth_country_code text,
														vfh_home_language_code text,
														vfh_term_location_postcode text,
														vfh_term_location_country_code text,
														vfh_home_location_postcode text,
														vfh_home_location_country_code text,
														vfh_arrival_year text,
														vfh_permanent_resident_code text,
														vfh_commencing_location_postcode text,
														vfh_commencing_geographic_location text,
														vfh_highest_attainment_code text,
														vfh_highest_attainment_year text,
														basis_for_admission_code text,
														hecs_payment_option_code text,
														usi_flag text,
														entitlement_contract_description text
													)
													""",
	'xref_vet_apprentice_template':					"""
													CREATE TABLE vet_apprentice (
														person_id text,
														api_id text,
														api_type text,
														course_code text,
														api_start_date text,
														api_end_date text,
														funding_source text,
														unit_cd text,
														unit_act_end_date text,
														enr_act_end_dte text,
														addr_type text,
														addr_start_date text,
														addr_end_date text,
														addr_line1 text,
														addr_line2 text,
														addr_line3 text,
														addr_line4 text,
														addr_line5 text,
														addr_aust_postcode text,
														other_details text,
														phone_3 text,
														phone_2 text,
														phone_1 text
													)
													""",
	'xref_student_template':						"""
													CREATE TABLE student (
														a_ses2006 text,
														age numeric,
														age_range text,
														atsi text,
														chessn text,
														country_of_birth text,
														deceased_indicator text,
														disability_flag text,
														dob date,
														email_address text,
														employment_category text,
														enrolled_ahc_ex_ns_ct_sw numeric,
														equivalent_eftsl numeric,
														ft_pt_status text,
														highest_prior_education_level_completed text,
														highest_school_level_completed text,
														highest_school_level_completed_year text,
														language text,
														mobile_phone_number text,
														postal_postcode text,
														residential_postcode text,
														resulted_ahc_ex_ns_ct_sw numeric,
														student_first_name text,
														student_gender text,
														student_home_state text,
														student_id text,
														student_last_name text,
														usi_flag text,
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
														vfh_term_location_postcode text
													)
													""",
	'xref_student_course_attempt_template':			"""
													CREATE TABLE student_course_attempt (
														a_ses2006 text,
														age numeric,
														age_range text,
														at_school_indicator text,
														atsi text,
														basis_for_admission text,
														basis_for_admission_code text,
														birth_country text,
														chessn text,
														contract_team text,
														correspondence_category text,
														course_admin_team text,
														course_attempt_status text,
														course_code text,
														course_commencement_date date,
														course_delivery_mode text,
														course_name text,
														course_requirements_completed_date date,
														course_requirements_completed_indicator text,
														deceased_indicator text,
														division text,
														email_address text,
														enrolled_ahc_ex_ns_ct_sw numeric,
														entitlement_contract_description text,
														fee_category text,
														foe2 text,
														foe4 text,
														hecs_payment_option text,
														hecs_payment_option_code text,
														highest_school_level_completed text,
														highest_school_level_completed_code text,
														industry text,
														intention_to_complete_course text,
														intention_to_complete_units_only text,
														level text,
														mobile_phone_number text,
														no_course_intention text,
														postal_postcode text,
														residential_postcode text,
														resulted_ahc_ex_ns_ct_sw numeric,
														sca_funding_source text,
														student_gender text,
														student_home_state text,
														student_id text,
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
														vfh_term_location_postcode text
													)
													""",
	'xref_student_unit_attempt_template':			"""
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
													""",
	'xref_activity_pattern_trend_template':			"""
													CREATE TABLE activity_pattern_trend (
														unit_delivery_team text,
														division text,
														funding_source text,
														week_2018 numeric,
														week_2017 numeric,
														target_2018 numeric,
														target_2017 numeric,
														enrolled_2018 numeric,
														resulted_2018 numeric,
														funded_enrolled_2018 numeric,
														funded_resulted_2018 numeric,
														unfunded_enrolled_2018 numeric,
														unfunded_resulted_2018 numeric,
														enrolled_2017 numeric,
														resulted_2017 numeric,
														funded_enrolled_2017 numeric,
														funded_resulted_2017 numeric,
														unfunded_enrolled_2017 numeric,
														unfunded_resulted_2017 numeric
													)
													""",
	'xref_unresulted_sua_template':					"""
													CREATE TABLE unresulted_sua_{} (
														contract_team text,
														course_code text,
														course_name text,
														course_admin_team text,
														enrolled_ahc numeric,
														grade text,
														enrolment_activity_end_date date,
														result_type text,
														sca_funding_source text,
														student_first_name text,
														student_id text,
														student_last_name text,
														teaching_period text,
														unit_attempt_status text,
														unit_code text,
														unit_delivery_location text,
														unit_name text,
														usi_flag text
													)
													""",
	'xref_team_activity_template':					"""
													CREATE TABLE team_activity (
														unit_delivery_team text,
														division text,
														funding_source text,
														contract_course text,
														contract_course_name text,
														total_target numeric,
														total_enrolled numeric,
														total_resulted numeric,
														location text,
														remoteness text,
														urban_target numeric,
														urban_enrolled numeric,
														urban_resulted numeric,
														regional_target numeric,
														regional_enrolled numeric,
														regional_resulted numeric,
														remote_target numeric,
														remote_enrolled numeric,
														remote_resulted numeric,
														interstate_target numeric,
														interstate_enrolled numeric,
														interstate_resulted numeric
													)
													""",
	'xref_apprentice_sua_template':					"""
													CREATE TABLE apprentice_sua (
														delivery_location_team text,
														student_id text,
														atsi text,
														age_range text,
														disability_flag text,
														employment_category text,
														employment_category_description text,
														residential_postcode text,
														highest_school_level_completed_code text,
														highest_school_level_completed text,
														highest_school_level_completed_year text,
														country_of_birth text,
														language text,
														highest_prior_education_level_completed text,
														at_school_indicator text,
														vet_in_school_indicator text,
														course_industry text,
														course_industry_name text,
														foe2 text,
														foe4 text,
														course_level_description text,
														course_code text,
														unit_code text,
														fee_catagory text,
														unit_funding_source text,
														grade text,
														unit_delivery_location text,
														enrol_date date,
														result_date date,
														tci text,
														tci_start_date text,
														tci_end_date text,
														enrolled_ahc numeric,
														resulted_ahc numeric
													)
													""",
	'xref_apprentice_course_template':				"""
													CREATE TABLE apprentice_course (
														course_admin_team text,
														student_id text,
														atsi text,
														age_range text,
														disability_flag text,
														employment_category text,
														employment_category_description text,
														residential_postcode text,
														highest_school_level_completed_code text,
														highest_school_level_completed text,
														highest_school_level_completed_year text,
														country_of_birth text,
														language text,
														highest_prior_education_level_completed text,
														at_school_indicator text,
														industry text,
														foe2 text,
														foe4 text,
														course_level_description text,
														course_code text,
														course_name text,
														unit_funding_source text,
														tci text,
														tci_start_date text,
														tci_end_date text,
														sum_of_enrolled_ahc numeric,
														sum_of_resulted_ahc numeric,
														address_start_date text,
														address_end_date text,
														employer_or_business_name text,
														employer_address_line_1 text,
														employer_address_line_2 text,
														employer_suburb text,
														employer_state text,
														employer_postcode text,
														employer_phone_number text,
														employer_fax_number text,
														employer_contact_name text,
														employer_email_details text
													)
													""",
	'xref_vfh_unit_tp_template':					"""
													CREATE TABLE xref_vfh_unit_tp (
														course text,
														status text,
														course_name text,
														location text,
														unit text,
														unit_name text,
														hrs text,
														eftsl text,
														ntg_tuition text,
														ntg_rpl text,
														full_fee text,
														sponsored_full_fee text,
														sponsored_rpl_fee text,
														rpl_fee text,
														start_date text,
														teaching_period text,
														rpl_only text,
														end_date text,
														census_date text,
														team text,
														duration text,
														full_fee_est_cost text,
														subsidised_est_cost text,
														delivery text,
														est_sponsored_cost text
													)
													"""
}


xlookup_tables = {
	'xlookup_activity_pattern_trend':				"""
													CREATE TABLE xlookup_activity_pattern_trend (
														unit_delivery_team text,
														division text,
														funding_source text,
														week_2018 numeric,
														week_2017 numeric,
														target_2018 numeric,
														target_2017 numeric,
														enrolled_2018 numeric,
														resulted_2018 numeric,
														funded_enrolled_2018 numeric,
														funded_resulted_2018 numeric,
														unfunded_enrolled_2018 numeric,
														unfunded_resulted_2018 numeric,
														enrolled_2017 numeric,
														resulted_2017 numeric,
														funded_enrolled_2017 numeric,
														funded_resulted_2017 numeric,
														unfunded_enrolled_2017 numeric,
														unfunded_resulted_2017 numeric
													)
													""",
	'xlookup_afb_course_table':						"""
													CREATE TABLE xlookup_afb_course_table (
														course_code text,
														course_name text
													)
													""",
	'xlookup_age_group':							"""
													CREATE TABLE xlookup_age_group (
														age numeric,
														age_range text
													)
													""",
	'xlookup_australia_post':						"""
													CREATE TABLE xlookup_australia_post (
														pcode text,
														locality text,
														state text,
														comments text,
														deliveryoffice text,
														presortindicator text,
														parcelzone text,
														bspnumber text,
														bspname text,
														category text
													)
													""",
	'xlookup_country':								"""
													CREATE TABLE xlookup_country (
														identifier text,
														full_name text,
														last_updated date
													)
													""",
	'xlookup_course':								"""
													CREATE TABLE xlookup_course (
														code text,
														description text,
														active_indicator text,
														code_reference text,
														description_reference text,
														level text,
														foe2 text,
														foe4 text,
														anzsco text,
														industry text
													)
													""",
	'xlookup_det_industry':							"""
													CREATE TABLE xlookup_det_industry (
														code text,
														description text
													)
													""",
	'xlookup_division':								"""
													CREATE TABLE xlookup_division (
														team_code text,
														division text
													)
													""",
	'xlookup_employment_status':					"""
													CREATE TABLE xlookup_employment_status (
														employment_status_code text,
														employment_status_description text
													)
													""",
	'xlookup_etp_eligible_course_list':				"""
													CREATE TABLE xlookup_etp_eligible_course_list (
														course_code text,
														course_name text,
														units_to_complete numeric,
														price_urban numeric,
														price_regional numeric,
														price_remote numeric
													)
													""",
	'xlookup_etp_eligible_course_list_by_contract':	"""
													CREATE TABLE xlookup_etp_eligible_course_list_by_contract (
														course_code text,
														course_name text,
														purchasing_contract_identifier text
													)
													""",
	'xlookup_etp_targets':							"""
													CREATE TABLE xlookup_etp_targets (
														division text,
														unit_delivery_team text,
														team_target_ahc numeric,
														team_target_headcount numeric
													)
													""",
	'xlookup_etp_targets_2016':						"""
													CREATE TABLE xlookup_etp_targets_2016 (
														division text,
														unit_delivery_team text,
														division_target_ahc numeric
													)
													""",
	'xlookup_etp_targets_2017':						"""
													CREATE TABLE xlookup_etp_targets_2017 (
														division text,
														unit_delivery_team text,
														team_target_ahc numeric,
														team_target_headcount numeric
													)
													""",
	'xlookup_FOE2':									"""
													CREATE TABLE xlookup_FOE2 (
														code text,
														description text
													)
													""",
	'xlookup_FOE4':									"""
													CREATE TABLE xlookup_FOE4 (
														code text,
														description text	
													)
													""",
	'xlookup_language':								"""
													CREATE TABLE xlookup_language (
														identifier text,
														full_name text,
														last_updated date
													)
													""",
	'xlookup_level':								"""
													CREATE TABLE xlookup_level (
														level_code text,
														description text
													)
													""",
	'xlookup_location':								"""
													CREATE TABLE xlookup_location (
														code text,
														description text,
														postal_location text,
														profile_location text,
														region text,
														remoteness text,
														providence text,
														postcode text,
														state_code text
													)
													""",
	'xlookup_mceetya_ses':							"""
													CREATE TABLE xlookup_mceetya_ses (
														postcode text,
														state text,
														a_ses text,
														s_ses text,
														m1 numeric,
														m2 numeric,
														m3 numeric,
														m4 numeric,
														m5 numeric,
														m6 numeric,
														m7 numeric,
														m8 numeric,
														m9 numeric,
														m_total numeric,
														a_ses2006 text,
														s_ses2006 text
													)
													""",
	'xlookup_ntis_superseded_unit':					"""
													CREATE TABLE xlookup_ntis_superseded_unit (
														identifier text,
														short_name text,
														superseding_identifier text,
														superseding_short_name text,
														description text,
														last_update date
													)
													""",
	'xlookup_ntis_superseded_unit_equivalent_flag':	"""
													CREATE TABLE xlookup_ntis_superseded_unit_equivalent_flag (
														identifier text,
														short_name text,
														superseding_identifier text,
														superseding_short_name text,
														description text,
														last_update date,
														equivalent text
													)
													""",
	'xlookup_prior_education_level':				"""
													CREATE TABLE xlookup_prior_education_level (
														level_code text,
														description text
													)
													""",
	'xlookup_school_level':							"""
													CREATE TABLE xlookup_school_level (
														school_level_code text,
														school_level_description text
													)
													""",
	'xlookup_state_reference':						"""
													CREATE TABLE xlookup_state_reference (
														state text,
														state_identifier text
													)
													""",
	'xlookup_study_reason':							"""
													CREATE TABLE xlookup_study_reason (
														study_reason_id text,
														study_reason_description text,
														current_2018 text,
														current_2017 text,
														current_2016 text,
														current_2015 text,
														current_2014 text,
														current_2013 text,
														current_2012 text,
														current_2011 text,
														current_2010 text,
														current_2009 text,
														current_2008 text
													)
													""",
	'xlookup_target':								"""
													CREATE TABLE xlookup_target (
														contract_team text,
														division_school text,
														location text,
														region text,
														remoteness text,
														providence text,
														contract_unit text,
														contract_course_unit text,
														note text,
														funding text,
														source text,
														contract text,
														ahc numeric,
														course_orig text
													)
													""",
	'xlookup_team':									"""
													CREATE TABLE xlookup_team (
														code text,
														description text,
														current_2018 text,
														current_2017 text,
														current_2016 text,
														current_2015 text,
														current_2014 text,
														current_2013 text,
														current_2012 text,
														current_2011 text,
														current_2010 text,
														current_2009 text,
														current_2008 text
													)
													""",
	'xlookup_unit_delivery_type':					"""
													CREATE TABLE xlookup_unit_delivery_type (
														code text,
														description text
													)
													""",
	'xlookup_units':								"""
													CREATE TABLE xlookup_units (
														identifier text,
														full_name text,
														module_foe text
													)
													""",
	'xlookup_vfh_atsi':								"""
													CREATE TABLE xlookup_vfh_atsi (
														vfh_atsi_code text,
														vfh_atsi_description text
													)
													""",
	'xlookup_vfh_basis_for_admission':				"""
													CREATE TABLE xlookup_vfh_basis_for_admission (
														vfh_basis_for_admission_cd text,
														vfh_basis_for_admission_description text
													)
													""",
	'xlookup_vfh_birth_country':					"""
													CREATE TABLE xlookup_vfh_birth_country (
														vfh_birth_country_cd text,
														vfh_birth_country_description text
													)
													""",
	'xlookup_vfh_citizenship':						"""
													CREATE TABLE xlookup_vfh_citizenship (
														vfh_citizenship_cd text,
														vfh_citizenship_description text
													)
													""",
	'xlookup_vfh_highest_attainment':				"""
													CREATE TABLE xlookup_vfh_highest_attainment (
														vfh_highest_participation_cd text,
														vfh_highest_participation_description text
													)
													""",
	'xlookup_vfh_language':							"""
													CREATE TABLE xlookup_vfh_language (
														vfh_home_language_cd text,
														vfh_home_language_description text
													)
													""",
	'xlookup_vfh_permanent_residence':				"""
													CREATE TABLE xlookup_vfh_permanent_residence (
														vfh_permanent_residence_cd text,
														vfh_permanent_residence_description text
													)
													""",
	'xlookup_vfh_student_status':					"""
													CREATE TABLE xlookup_vfh_student_status (
														vfh_student_status_cd text,
														vfh_student_status_description text
													)
													"""
}