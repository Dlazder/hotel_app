from mysql import connector


def get_connection():
	try:
		conn = connector.connect(
			host='localhost',
			user='dlazder',
			password='',
			database='hotel'
		)

		if conn.is_connected():
			print('Info: database connected;')
			return conn

	except Exception as e:
		print(f'Error: database; {e}')
		return None