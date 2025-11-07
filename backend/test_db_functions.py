# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating a database to log my sleep schedules
# ========================================================================
# HEADERS
# ========================================================================

from db_functions_people import DB_Functions
# ========================================================================
# TEST
# ========================================================================

db_functions:DB_Functions = DB_Functions()
db_functions.init_table_people()

# for j in range(1, 13):
# 	for i in range(1, 3):
# 		db_functions.CREATE_person(
# 			name_first = "Jhon", 
# 			name_last = f"Doe_{j}",
# 			birth_date = i,
# 			birth_month = j,
# 			birth_year = i,
# 		)

# for peeps in db_functions.GET_people():
#     print(peeps)

for peeps in db_functions.GET_birthdays_adjacent(2):
    print(peeps)

# print()

# for peeps in db_functions.GET_birthdays_adjacent():
#     print(peeps)

# print(db_functions.DELETE_person(47))

# print(db_functions.UPDATE_person(name_first="kill", id=25))