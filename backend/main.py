# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating an api for the database
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask
from routes_people import People

# ========================================================================
# MAIN
# ========================================================================

# Run server
if __name__ == "__main__":
	db_file_name:str = "my_peeps.db"

	app = Flask(__name__)
	classic:People = People(db_file_name=db_file_name)
	classic.init_table_people()
	classic.define_routes(app=app)

	app.run(
		debug=True, 
		host='0.0.0.0', 
		port=8080
	)
