# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating a database to log my sleep schedules
# ========================================================================
# HEADERS
# ========================================================================

from flask import Flask, request as f_req, jsonify
from db_connection import SQLConnection

# ========================================================================
# CLASS
# ========================================================================

class People(SQLConnection):
	table_name:str = "people"

	def init_table_people(self)->None:
		CREATE_table_people = f"""
		CREATE TABLE IF NOT EXISTS {self.table_name} (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			created_at TEXT DEFAULT CURRENT_TIMESTAMP,
			updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
			deleted_at TEXT,
			name_display TEXT UNIQUE,
			name_full TEXT,
			birth_date_day TINYINT,
			birth_date_month TINYINT,
			birth_date_year SMALLINT
		);
		"""
		self.SQL_execute(
			SQL_command=CREATE_table_people
		)

	# ========================================================================

	def define_routes(
		self,
		app:Flask
	):
		@app.route(f"/{self.table_name}", methods=["POST"])
		def POST():
			try:
				data:dict = f_req.get_json()

				# DATA VALIDATION
				if not data:
					return jsonify({
						"success": False,
						"message": "Request body must be JSON"
					}), 400

				fields = [
					"name_display",
					"name_full",
					"birth_date_day",
					"birth_date_month",
					"birth_date_year"
				]

				for field in fields:
					if field not in data:
						return jsonify({
							"success": False,
							"message": f"Missing required field: {field}"
						}), 400

				# SQL COMMAND
				INSERT_person = f"""
				INSERT INTO {self.table_name} (
					name_display,
					name_full,
					birth_date_day, 
					birth_date_month, 
					birth_date_year
				) VALUES (?, ?, ?, ?, ?);
				"""
				params:tuple = (
					data.get("name_display"),
					data.get("name_full"),
					data.get("birth_date_day"),
					data.get("birth_date_month"),
					data.get("birth_date_year")
				)

				self.SQL_execute(
					SQL_command = INSERT_person,
					params=params
				)

				return jsonify({
					"success": True,
					"message": "person entry created successfully"
				}), 201
			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================
			
		@app.route(f"/{self.table_name}", methods=["GET"])
		def GET():
			try:
				id:int = f_req.get_json().get("id")

				# BASE QUERY
				SELECT_person = f"""
					SELECT *
					FROM {self.table_name}
					WHERE deleted_at IS NULL;
					"""
				params:tuple = ()
				if id:
					SELECT_person = f"""
					SELECT *
					FROM {self.table_name}
					WHERE id = ?;
					"""
					params = (id,)

				rows = self.SQL_fetch(
					SQL_command=SELECT_person,
					params=params
				)

				# NORMALIZE OUTPUT (depends on your SQL_execute return format)
				return jsonify({
					"success": True,
					"data": rows
				}), 200

			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================

		# is only a soft delete
		@app.route(f"/{self.table_name}", methods=["DELETE"])
		def DELETE():
			try:
				id:int = f_req.get_json().get("id")
				if not id:
					return jsonify({
						"success": False,
						"message": "Missing required field: id"
					}), 500
				params:tuple = (id,)
				
				# 1. Check record exists + status
				SELECT_person = f"""
					SELECT id, deleted_at
					FROM {self.table_name}
					WHERE id = ?;
				"""
				fetch:list = self.SQL_fetch(
					SQL_command = SELECT_person,
					params = params
				)
				if not fetch:
					return jsonify({
						"success": False,
						"message": f"Person not found"
					}), 404
				elif fetch[0][1] :
					return jsonify({
						"success": False,
						"message": f"Person already deleted"
					}), 404


				DELETE_person = f"""
				UPDATE {self.table_name}
				SET 
				deleted_at = CURRENT_TIMESTAMP,
				updated_at = CURRENT_TIMESTAMP
				WHERE id = ?;
				"""
				self.SQL_execute(
					SQL_command = DELETE_person,
					params=params
				)

				return jsonify({
					"success": True,
					"message": f"person entry deleted successfully"
				}), 201
			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================

		@app.route(f"/{self.table_name}", methods=["PATCH"])
		def PATCH():
			try:
				data:dict = f_req.get_json()
				if not data:
					return jsonify({
						"success": False,
						"message": "Request body must be JSON"
					}), 400

				id:int = data.get("id")
				if not id:
					return jsonify({
						"success": False,
						"message": "Missing required field: id"
					}), 500
				
				# 1. Check record exists + status
				SELECT_person = f"""
					SELECT id, deleted_at
					FROM {self.table_name}
					WHERE id = {self.SQL_value(id)};
				"""
				fetch:list = self.SQL_fetch(SELECT_person)
				if not fetch:
					return jsonify({
						"success": False,
						"message": f"Person not found"
					}), 404
				elif fetch[0][1] :
					return jsonify({
						"success": False,
						"message": f"Person already deleted"
					}), 404
				
				# check the fields that are to be updated
				fields = [
					"name_display",
					"name_full",
					"birth_date_day",
					"birth_date_month",
					"birth_date_year"
				]

				missing_field_flag:bool = False
				missing_fields:list[str] = []
				for field in fields:
					if ((field not in data) 
		 			or (data.get(field) == None)):
						missing_fields.append(field)
						missing_field_flag = True
				if missing_field_flag:
					return jsonify({
						"success": False,
						"message": f"Missing required field: {missing_fields}"
					}), 400

				UPDATE_person = f"""
					UPDATE {self.table_name}
					SET 
						name_display = ?,
						name_full = ?,
						birth_date_day = ?,
						birth_date_month = ?,
						birth_date_year = ?,
						updated_at = CURRENT_TIMESTAMP
					WHERE id = ?;
				"""
				params = (
					data.get("name_display"),
					data.get("name_full"),
					data.get("birth_date_day"),
					data.get("birth_date_month"),
					data.get("birth_date_year"),
					id
				)

				self.SQL_execute(
					SQL_command = UPDATE_person,
					params = params
				)

				return jsonify({
					"success": True,
					"message": f"person entry updated successfully"
				}), 201
			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================
		
		@app.route(f"/{self.table_name}/upcoming", methods=["GET"])
		def upcoming():
			try:
				data:dict = f_req.get_json()

				# DATA VALIDATION
				if not data:
					return jsonify({
						"success": False,
						"message": "Request body must be JSON"
					}), 400
				if "month" not in data:
						return jsonify({
							"success": False,
							"message": f"Missing required field: month"
						}), 400
				
				month:int = int(data.get("month"))

				# BASE QUERY
				SELECT_person = f"""
					SELECT *
					FROM {self.table_name}
					WHERE deleted_at IS NULL
					AND birth_date_month IN (?, ?);
					"""
				params:tuple = (month, (month%12)+1)

				rows = self.SQL_fetch(
					SQL_command=SELECT_person,
					params = params
				)

				# NORMALIZE OUTPUT (depends on your SQL_execute return format)
				return jsonify({
					"success": True,
					"data": rows
				}), 200

			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
