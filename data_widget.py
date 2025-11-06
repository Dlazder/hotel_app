from get_connection import get_connection
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DataWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		conn = get_connection()
		cursor = conn.cursor()
		cursor.execute('select number, floor, name from rooms r join statuses s on s.id = r.status;')
		rooms = cursor.fetchall()
		print(rooms)

		main_layout = QVBoxLayout()
		self.setLayout(main_layout)

		self.rooms_widget = QTableWidget(len(rooms), len(rooms[0]))
		for i, room_data in enumerate(rooms):
			for j, cell_data in enumerate(room_data):
				self.rooms_widget.setItem(i, j, QTableWidgetItem(str(cell_data)))

		main_layout.addWidget(self.rooms_widget)

		text = QLabel('main')
		main_layout.addWidget(text)