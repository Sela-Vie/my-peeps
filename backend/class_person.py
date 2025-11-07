# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: 
#   class for the person table 
#   to have an easy format to transport person infos
# ========================================================================
# HEADERS
# ========================================================================

class TABLE_person():
	def __init__(
		self,
		name_first:str = "NULL", 
		name_last:str = "NULL",
		date_birth:str = 'NULL',
		status_deleted:int = 0,
		time_entry_added:str = "NULL",
		id = -1
		):
		self.name_first:str = name_first
		self.name_last:str = name_last
		self.date_birth:str = date_birth
		self.status_deleted:int = status_deleted
		self.time_entry_added:str = time_entry_added
		self.id = id
	
	def __str__(self) -> str:
		space:int = 15
		message:str = ""
		message += f"{'id':{space}}{self.id}\n"
		message += f"{'entry date':{space}}{self.time_entry_added}\n"
		message += f"{'deleted status':{space}}{self.status_deleted}\n"
		message += f"\n"
		message += f"{'name':{space}}{self.name_first}, {self.name_last}\n"
		message += f"{'birthday':{space}}{self.date_birth}\n"
		return message

	def set_from_touple(self, tuple:tuple):
		try:
			self.name_first = tuple[0]
			self.name_last = tuple[1]
			self.date_birth = tuple[2]
			self.status_deleted = tuple[3]
			self.time_entry_added = tuple[4]
			self.id = tuple[5]
		except Exception as e:
			print(e)