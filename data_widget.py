from get_connection import get_connection
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DataWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		main_layout = QVBoxLayout()
		self.setLayout(main_layout)

		text = QLabel('main')
		main_layout.addWidget(text)