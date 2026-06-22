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
			SQL_command:str,
			params:tuple = ()
		) -> None:

		try:
			# this_connection = sqlite3.connect(self.db_file_name)
			# the with statement avoids the database locking when
			# an sql error happens and the database connection isnt closed
			with sqlite3.connect(self.db_file_name) as this_connection:
				this_connection.execute("PRAGMA foreign_keys = ON;")		
				# this one makes the foreign_keys necessarily exist before you can assign them
				
				this_cursor:sqlite3.Cursor = this_connection.cursor()
				this_cursor.execute(
					textwrap.dedent(SQL_command),
					params  # tuple or dict
				)
				this_connection.commit()
		except Exception as e:
			raise(e)

	def SQL_fetch(
			self,
			SQL_command:str,
			params:tuple = ()
		) -> list:
		ret_val:list = []

		try:
			this_connection:sqlite3.Connection = sqlite3.connect(self.db_file_name)
			this_connection.execute("PRAGMA foreign_keys = ON;")
			# this one makes the foreign_keys necessarily exist before you can assign them
			
			this_cursor:sqlite3.Cursor = this_connection.cursor()
			this_cursor.execute(
				textwrap.dedent(SQL_command),
				params  # tuple or dict
			)
			ret_val = this_cursor.fetchall()
			this_connection.close()
		except Exception as e:
			raise(e)

		return ret_val