# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: template class to connect to a .db file and interact with it
# ========================================================================
# HEADERS
# ========================================================================

import sqlite3
import textwrap

# ========================================================================
# CLASS
# ========================================================================

class SQLConnection():
	def __init__(
		self, 
		db_file_name:str = "my_peeps.db"
	):
		self.db_file_name = db_file_name

	# ====================================================================
	
	def SQL_execute(
		self,
		SQL_command:str
	) -> bool:
		is_executed_just_fine = False

		try:
			this_connection:sqlite3.Connection = sqlite3.connect(self.db_file_name)
			this_cursor:sqlite3.Cursor = this_connection.cursor()
			this_cursor.execute(textwrap.dedent(SQL_command))
			this_connection.commit()
			this_connection.close()
			is_executed_just_fine = True
		except Exception as e:
			print(e)

		return is_executed_just_fine

	def SQL_fetch(
			self,
			SQL_command:str
		) -> bool:
		ret_val = 0

		try:
			this_connection:sqlite3.Connection = sqlite3.connect(self.db_file_name)
			this_cursor:sqlite3.Cursor = this_connection.cursor()
			this_cursor.execute(textwrap.dedent(SQL_command))
			ret_val:list = this_cursor.fetchall()
			this_connection.close()
		except Exception as e:
			print(e)

		return ret_val

	# ====================================================================
	# this thing is just here for the utility

	def SQL_value(self, val) -> str:
		if val == -1 or val == "NULL":
			return "NULL"
		else:
			return f'"{val}"'