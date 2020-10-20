import sqlite3


class DataBase():

	def __init__(self, path_to_db='authme.db'):
		self.path_to_db = path_to_db

	def create_connection(self):
		self.conn = sqlite3.connect(self.path_to_db, check_same_thread=False)
		self.cursor = self.conn.cursor()

	def close_connection(self):
		self.cursor.close()
		self.conn.close()

	def select_user_for_name(self, username):
		self.create_connection()

		sql = ' SELECT * FROM authme WHERE username=?'
		self.cursor.execute(sql, [(username)])
		unit = self.cursor.fetchall()

		self.close_connection()

		try:
			return unit[0]

		except IndexError:
			return None

		