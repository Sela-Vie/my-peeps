# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating a database to log my sleep schedules
# ========================================================================
# HEADERS
# ========================================================================

from db_connection import SQLConnection
from class_person import TABLE_person

from datetime import datetime, timezone

# ========================================================================
# CLASS
# ========================================================================

class DB_Functions(SQLConnection):
	
	def init_table_people(self)->None:
		CREATE_table_people = """
		CREATE TABLE IF NOT EXISTS people (
			name_first TXT,
			name_last TXT,
			date_birth TXT,
			
			status_deleted INT,
			time_entry_added TEXT,
			id_person INTEGER PRIMARY KEY AUTOINCREMENT
		);
		"""
		self.SQL_execute(
			SQL_command=CREATE_table_people
		)

	# ========================================================================

	def CREATE_person(
		self,
		name_first:str = "NULL", 
		name_last:str = "NULL",
		birth_date:int = 2001,
		birth_month:int = 1,
		birth_year:int = 1,
	):
		time_now:str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
		date_birth:str = "NULL"
		if (birth_date == 2001 and
	  		birth_month == 1 and
			birth_year == 1):
			pass
		else:
			date_birth:str = datetime(
				year=birth_year,
				month=birth_month,
				day=birth_date
			).date().isoformat()


		INSERT_person = f"""
		INSERT INTO people (
			time_entry_added,
			status_deleted,
			name_first, 
			name_last, 
			date_birth
		) VALUES (
			{self.SQL_value(time_now)},
			{self.SQL_value(0)},
			{self.SQL_value(name_first)},
			{self.SQL_value(name_last)},
			{self.SQL_value(date_birth)}
		);
		"""
		# YYYY-MM-DD for birthday
		# YYYY-MM-DDTHH:MM for time now

		self.SQL_execute(
			SQL_command = INSERT_person
		)

	# ========================================================================
	
	def GET_people(self)->list:
		SQL_command = "SELECT * FROM people"
		rows:list = self.SQL_fetch(
			SQL_command=SQL_command
		)
		return rows
	
	def GET_person(self, id:int = -1) -> list:
		SQL_command = f"""
		SELECT * 
		FROM people
		WHERE id_person = '{id}';
		"""
		rows:list = self.SQL_fetch(
			SQL_command=SQL_command
		)

		return rows

	# ========================================================================

	def DELETE_person(self, id) -> str:
		ret_val:str = f"DELETE person-{id}"

		if self.GET_person(id):

			DELETE_person = f"""
			DELETE FROM people
			WHERE id_person = '{id}';
			"""

			self.SQL_execute(
				SQL_command = DELETE_person
			)

			if not (self.GET_person(id)):
				ret_val = f"{ret_val:20}DELETE SUCCESS"
		else:
			ret_val = f"{ret_val:20}FAILED - person not found"

		return ret_val

	# ========================================================================

	def UPDATE_person(
		self,
		id = -1,
		name_first:str = "NULL", 
		name_last:str = "NULL",
		birth_date:int = 1,
		birth_month:int = 1,
		birth_year:int = 2001,
		status_deleted:int = -1
		)-> str:

		ret_val:str = f"UPDATE person-{id}"

		response = self.GET_person(id)
		if response and (id != -1):
			person:TABLE_person = TABLE_person()

			person.set_from_touple(response[0])

			# checking if theres actual changes to implement
			date_birth:str = "NULL"
			if not(
					birth_date == 2001 and
					birth_month == 1 and
					birth_year == 1
				):
				date_birth:str = datetime(
					year=birth_year,
					month=birth_month,
					day=birth_date
				).date().isoformat()

			change_flag:bool = False
			if not((name_first == "NULL") or (name_first == person.name_first)):
				person.name_first = name_first
				change_flag = True
			if not((name_last == "NULL") or (name_last == person.name_last)):
				person.name_last = name_last
				change_flag = True
			if not((date_birth == "NULL") or (date_birth == person.date_birth)):
				person.date_birth = date_birth
				change_flag = True
			if not((status_deleted == -1) or (status_deleted == person.status_deleted)):
				person.status_deleted = status_deleted
				change_flag = True

			if change_flag:

				SQL_command = f"""
				UPDATE people
				SET
					status_deleted = {self.SQL_value(person.status_deleted)},
					name_first = {self.SQL_value(person.name_first)},
					name_last = {self.SQL_value(person.name_last)},
					date_birth = {self.SQL_value(person.date_birth)}
				WHERE id_person = '{person.id}';
				"""

				self.SQL_execute(
					SQL_command = SQL_command
				)
				ret_val = f"{ret_val:20}SUCCESS"
			else:
				ret_val = f"{ret_val:20}FAILED - no chanages"
		else:
			ret_val = f"{ret_val:20}FAILED - person not found"

		return ret_val


	# ========================================================================
	# MISC FUNCTIONS
	# ========================================================================
	
	def GET_birthdays_adjacent(
			self, 
			month:int = -1
		)->list:

		if month == -1:
			month = datetime.now(timezone.utc).month

		SQL_command = f"""
			SELECT *
			FROM people
			WHERE CAST(strftime('%m', date_birth) AS INTEGER) IN ({month}, {(month % 12) + 1})
			ORDER BY strftime('%m-%d', date_birth);
		"""
		rows:list = self.SQL_fetch(
			SQL_command=SQL_command
		)
		return rows