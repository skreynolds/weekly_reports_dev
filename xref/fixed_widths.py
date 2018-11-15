#!/usr/bin/python

# Slices used to convert fixed width data to csv format ready for postres import
# for the VET_weekly_AHC
weekly_ahc_slices =		[slice(0, 11, None), 			# teaching period
						slice(11, 22, None),			# student id
						slice(22, 33, None),			# course admin team
						slice(33, 36, None),			# unit delivery location
						slice(36, 44, None),			# delivery location team
						slice(44, 55, None),			# unit funding source
						slice(55, 58, None),			# course delivery mode
						slice(58, 79, None),			# course code
						#slice(79, 99, None),			# course version
						slice(99, 110, None),			# fee category
						slice(110, 211, None),			# course name
						slice(211, 232, None),			# unit code
						slice(232, 333, None),			# unit name
						#slice(333, 353, None),			# unit version
						slice(353, 366, None),			# enrolled ahc
						slice(366, 379, None),			# resulted ahc
						slice(379, 385, None),			# grade
						slice(385, 387, None),			# atsi
						slice(387, 398, None),			# course industry
						#slice(398, 409, None),			# school unit teacher
						#slice(409, 420, None),			# faculty course owner
						slice(420, 451, None),			# student last name
						slice(451, 492, None),			# student first name
						slice(492, 513, None),			# aci
						slice(513, 534, None),			# tci
						slice(534, 544, None),			# student dob
						slice(544, 554, None),			# override activity end date
						#slice(554, 573, None),			# calendar number
						slice(573, 584, None),			# unit attempt status
						slice(584, 595, None),			# correspndence category
						slice(595, 597, None),			# student gender
						slice(597, 638, None),			# student home state
						slice(638, 641, None),			# grade keyed
						slice(641, 742, None),			# vet school name
						slice(742, 753, None),			# unit delivery type
						#slice(753, 804, None),			# school course owner
						#slice(804, 835, None),			# school % owned
						slice(835, 846, None),			# enrol date
						slice(846, 857, None),			# disc date
						slice(857, 868, None),			# result date
						slice(868, 870, None),			# staff indicator
						slice(870, 921, None),			# stream code
						slice(921, 932, None),			# study reason
						slice(932, 943, None),			# granted date
						slice(943, 945, None),			# vet in school indicator
						slice(945, 947, None),			# at school indicator
						#slice(947, 949, None),			# field 47
						slice(949, 960, None),			# highest prior education level completed code
						slice(960, 971, None),			# home language code
						slice(971, 982, None),			# birth country code
						slice(982, 993, None),			# highest school level completed code
						slice(993, 1022, None),			# highest school level completed year
						slice(1022, 1027, None),		# residential postcode
						slice(1027, 1038, None),		# employment category
						slice(1038, 1049, None),		# disability flag
						#slice(1049, 1059, None),		# tci end date
						slice(1059, 1070, None),		# course attempt status
						slice(1070, 1080, None),		# course commencement date
						slice(1080, 1091, None),		# sca funding source
						slice(1091, 1102, None),		# enrolment activity end date
						slice(1102, 1107, None),		# postal postcode
						slice(1107, 1117, None),		# override activity start date
						slice(1117, 1119, None),		# intention to complete course
						slice(1119, 1121, None),		# intention to complete units only
						slice(1121, 1123, None),		# no course intention
						slice(1123, 1125, None),		# course requirements completed indicator
						slice(1125, 1135, None),		# course requirements completed date
						slice(1135, 1146, None),		# result type
						slice(1146, 1247, None),		# unit contact
						slice(1247, 1257, None),		# cancelled date
						slice(1257, 1267, None),		# not approved date
						slice(1267, 1278, None),		# administrative unit status
						slice(1278, 1289, None),		# chessn
						slice(1289, 1300, None),		# vfh atsi code
						slice(1300, 1311, None),		# vfh citizenship code
						slice(1311, 1322, None),		# vfh birth country code
						slice(1322, 1333, None),		# vfh home language code
						slice(1333, 1338, None),		# vfh term location postcode
						slice(1338, 1349, None),		# vfh term location country code
						slice(1349, 1354, None),		# vfh home location postcode
						slice(1354, 1365, None),		# vfh home location country code
						slice(1365, 1370, None),		# vfh arrival year
						slice(1370, 1381, None),		# vfh permanent resident code
						slice(1381, 1387, None),		# vfh commencing location postcode
						slice(1387, 1415, None),		# vfh commencing geographic location
						slice(1415, 1417, None),		# vfh highest attainment code
						slice(1417, 1422, None),		# vfh highest attainment year
						slice(1422, 1433, None),		# basis for admission code
						slice(1433, 1444, None),		# hecs payment option code
						slice(1444, 1455, None),		# unit student status code
						slice(1455, 1465, None),		# unit census date
						slice(1465, 1467, None),		# usi flag
						slice(1467, 1469, None),		# deceased indicator
						slice(1469, 1724, None),		# entitlement contract description
						#slice(1724, 5470, None),		# field 48
						slice(5470, 5571, None),		# email address
						slice(5571, 5592, None),		# mobile phone number
						slice(5592, 5725, None),		# contract course unit name
						slice(5725, 5745, None),		# contract course unit code
						slice(5745, 5760, None),		# contract
						slice(5760, 5770, None),		# outcome
						slice(5770, 5780, None),		# age
						slice(5780, 5790, None),		# teaching period end date
						slice(5790, 5792, None),		# enrol week
						slice(5792, 5794, None),		# result week
						slice(5794, 5894, None),		# contract team
						slice(5894, 5904, None)		# ur outcome
						]

# Slices used to convert fixed width data to csv format ready for postres import
# for the VET_Course_Completions
completions_slices =	[slice(0, 11, None),			# student id		
						slice(11, 42, None),			# student last name
						slice(42, 83, None),			# student first name
						slice(83, 85, None),			# student gender
						slice(85, 97, None),			# student dob
						slice(97, 198, None),			# student email address
						slice(198, 219, None),			# course code
						slice(219, 320, None),			# course name
						slice(320, 332, None),			# course commencement date
						slice(332, 343, None),			# course attempt status
						slice(343, 353, None),			# course requirements completed date
						slice(353, 364, None),			# sca funding source
						slice(364, 367, None),			# course admin location
						slice(367, 375, None),			# course admin team
						slice(375, 378, None),			# course delivery mode 
						slice(378, 389, None),			# study reason
						slice(389, 391, None),			# vet in school indicator
						slice(391, 393, None),			# unit only enrolment indicator
						slice(393, 404, None),			# highest school level completed code
						slice(404, 433, None),			# highest school level completed year
						slice(433, 438, None),			# residential postcode
						slice(438, 449, None),			# home language code
						slice(449, 460, None),			# birth country code
						slice(460, 462, None),			# at school indicator
						slice(462, 473, None),			# atsi status
						slice(473, 484, None),			# employment category
						#slice(484, 495, None),			# spoken english proficiency
						slice(495, 505, None),			# conferral date
						slice(505, 606, None),			# vet school name
						slice(606, 608, None),			# no course intention
						slice(608, 619, None),			# chessn
						slice(619, 630, None),			# vfh atsi code
						slice(630, 641, None),			# vfh citizenship code
						slice(641, 652, None),			# vfh birth country code
						slice(652, 663, None),			# vfh home language code
						slice(663, 668, None),			# vfh term location postcode
						slice(668, 679, None),			# vfh term location country code
						slice(679, 684, None),			# vfh home location postcode
						slice(684, 695, None),			# vfh home location country code
						slice(695, 700, None),			# vfh arrival year
						slice(700, 711, None),			# vfh permanent resident code
						slice(711, 717, None),			# vfh commencing location postcode
						slice(717, 745, None),			# vfh commencing geographic location
						slice(745, 747, None),			# vfh highest attainment code
						slice(747, 752, None),			# vfh highest attainment year
						slice(752, 763, None),			# basis for admission code
						slice(763, 774, None),			# hecs payment option code
						slice(774, 784, None),			# usi flag
						slice(784, 1039, None),			# entitlement contract description
						#slice(1039, 4784, None)		# field 1
						]

# Slices used to convert fixed width data to csv format ready for postres import
# for the VET_Apprentice
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