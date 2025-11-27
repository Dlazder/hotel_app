from get_connection import get_connection
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QLabel, QTableWidget, QTableWidgetItem, QWidget


class DataWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.conn = get_connection()

	def initUI(self):
		cursor = self.conn.cursor()
		
		cursor.execute('select number, floor, name from rooms r join statuses s on s.id = r.status;')
		rooms = cursor.fetchall()

		cursor.execute('select * from statuses;')
		self.statuses = cursor.fetchall()

		main_layout = QVBoxLayout()
		self.setLayout(main_layout)

		self.rooms_widget = QTableWidget(len(rooms), len(rooms[0]))
		self.rooms_widget.setHorizontalHeaderLabels(['Номер', 'Этаж', 'Статус'])
		for i, room_data in enumerate(rooms):
			for j, cell_data in enumerate(room_data):
				if j == 2:
					select = QComboBox()
					select.addItems(list(map(lambda e: e[1], self.statuses)))

					select.currentTextChanged.connect(lambda text, row=i: self.on_status_change(row, text))
					self.rooms_widget.setCellWidget(i, j, select)
				else:
					self.rooms_widget.setItem(i, j, QTableWidgetItem(str(cell_data)))

		main_layout.addWidget(self.rooms_widget)

		text = QLabel('main')
		main_layout.addWidget(text)

	def on_status_change(self, row, new_status):
		cursor = self.conn.cursor()
		status_id = None
		for id, name in self.statuses:
			if name == new_status:
				status_id = id
				break
		cursor.execute('UPDATE rooms set status = %s WHERE id = %s', [status_id, row+1])
		self.conn.commit()