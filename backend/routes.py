# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask, request as f_req, jsonify

from db_functions_people import DB_Functions

# ========================================================================
# ROUTES
# ========================================================================

def define_routes(
		app:Flask,
		db_file:str = ""
	):
	db_access:DB_Functions = DB_Functions()
	db_access.init_table_people()

	# ========================================================================

	@app.route("/people/birthdays", methods=["GET"])
	def GET_birthdays():
		ret_val = 200
		try:
			data:dict = f_req.get_json()
			month_num:int = int(data.get("month", 0))
			
			ret_val = jsonify(db_access.GET_birthdays_adjacent(month = month_num))
		except Exception as e:
			try:
				ret_val = jsonify(db_access.GET_birthdays_adjacent())
			except Exception as e:
				print(e)
				ret_val = 500
		
		return ret_val

	# ========================================================================

	@app.route("/people", methods=["GET"])
	def GET_people():
		ret_val = "200"
		try:
			ret_val = jsonify(db_access.GET_people())
		except Exception as e:
			ret_val = "500"
		return ret_val

	@app.route("/people", methods=["POST"])
	def CREATE_person():
		ret_val = "200"
		try:
			data:dict = f_req.get_json()
			db_access.CREATE_person(
				name_first = data.get("name_first"),
				name_last = data.get("name_last"),
				birth_date = int(data.get("birth_date")),
				birth_month = int(data.get("birth_month")),
				birth_year = int(data.get("birth_year"))
			)
		except Exception as e:
			ret_val = "500"
		return ret_val

	@app.route("/people", methods=["PUT"])
	def PATCH_person():
		ret_val = "200"
		try:
			data:dict = f_req.get_json()
			ret_val = db_access.UPDATE_person(
				id = data.get("id"),
				name_first = data.get("name_first"),
				name_last = data.get("name_last"),
				birth_date = int(data.get("birth_date")),
				birth_month = int(data.get("birth_month")),
				birth_year = int(data.get("birth_year"))
			)
		except Exception as e:
			print(e)
			ret_val = "500"
		return ret_val

	
	@app.route("/people", methods=["DELETE"])
	def DELETE_person():
		ret_val = 200
		try:
			data:dict = f_req.get_json()
			ret_val = db_access.UPDATE_person(
				id = data.get("id"),
				status_deleted = 1
			)
		except Exception as e:
			ret_val = 500
		return ret_val