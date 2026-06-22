# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating an api for the database
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask
from routes_people import People
from routes_people_logs import PeopleLogs

# ========================================================================
# MAIN
# ========================================================================

# Run server
if __name__ == "__main__":
	db_file_name:str = "my_peeps.db"

	app = Flask(__name__)
	people_table:People = People(db_file_name=db_file_name)
	people_table.init_table()
	people_table.define_routes(app=app)
	people_logs_table:PeopleLogs = PeopleLogs(db_file_name=db_file_name)
	people_logs_table.init_table()
	people_logs_table.define_routes(app=app)

	app.run(
		debug=True, 
		host='0.0.0.0', 
		port=8080
	)
