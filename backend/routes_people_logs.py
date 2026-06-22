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

class PeopleLogs(SQLConnection):
	table_name:str = "people_logs"

	def init_table(self)->None:
		CREATE_table = f"""
		CREATE TABLE IF NOT EXISTS {self.table_name} (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			id_user INTEGER NOT NULL,
			created_at TEXT DEFAULT CURRENT_TIMESTAMP,
			updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
			deleted_at TEXT,
			content TEXT UNIQUE,
			
			FOREIGN KEY (id_user) REFERENCES people(id)
		);
		"""
		self.SQL_execute(
			SQL_command=CREATE_table
		)

	# ========================================================================

	def define_routes(
		self,
		app:Flask
	):
		@app.route(f"/{self.table_name}", methods=["POST"])
		def POST_PeopleLogs():
			try:
				data:dict = f_req.get_json()

				# DATA VALIDATION
				if not data:
					return jsonify({
						"success": False,
						"message": "Request body must be JSON"
					}), 400

				fields = [
					"id_user",
					"content"
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
					id_user,
					content
				) VALUES (?, ?);
				"""
				params:tuple = (
					data.get("id_user"),
					data.get("content"),
				)

				self.SQL_execute(
					SQL_command = INSERT_person,
					params=params
				)

				return jsonify({
					"success": True,
					"message": "person_log entry created successfully"
				}), 201
			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================
			
		@app.route(f"/{self.table_name}", methods=["GET"])
		def GET_PeopleLogs():
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
		def DELETE_PeopleLogs():
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
						"message": f"person_log not found"
					}), 404
				elif fetch[0][1] :
					return jsonify({
						"success": False,
						"message": f"person_log already deleted"
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
					"message": f"person_log entry deleted successfully"
				}), 201
			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================

		@app.route(f"/{self.table_name}", methods=["PATCH"])
		def PATCH_PeopleLogs():
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
					WHERE id = {id};
				"""
				fetch:list = self.SQL_fetch(SELECT_person)
				if not fetch:
					return jsonify({
						"success": False,
						"message": f"person_log not found"
					}), 404
				elif fetch[0][1] :
					return jsonify({
						"success": False,
						"message": f"person_log already deleted"
					}), 404
				
				# check the fields that are to be updated
				fields = [
					"content"
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
						content = ?,
						updated_at = CURRENT_TIMESTAMP
					WHERE id = ?;
				"""
				params = (
					data.get("content"),
					id
				)

				self.SQL_execute(
					SQL_command = UPDATE_person,
					params = params
				)

				return jsonify({
					"success": True,
					"message": f"person_log entry updated successfully"
				}), 201
			except Exception as e:
				return jsonify({
					"success": False,
					"message": str(e)
				}), 500
		# ========================================================================
		