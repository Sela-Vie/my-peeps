# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating an api for the database
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask
from routes import define_routes

# ========================================================================
# CLASS
# ========================================================================

class API():
	def __init__(
		self, 
		db_file:str = ""
	):
		self.db_file:str = db_file
		self.flask_object:Flask = Flask(__name__)
	
	def run(self):
		define_routes(
			app = self.flask_object,
			db_file = self.db_file
		)
		self.flask_object.run(
			debug=True, 
			host='0.0.0.0', 
			port=5000
		)

# Run server
if __name__ == "__main__":
	db_file:str = "my_peeps.db"

	backend:API = API(
		db_file=db_file
	)
	backend.run()
