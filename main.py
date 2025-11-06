from get_connection import get_connection
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from login_widget import LoginWidget
from data_widget import DataWidget



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Hotel')

		self.stacked_widget = QStackedWidget()
		self.setCentralWidget(self.stacked_widget)

		self.login_widget = LoginWidget(self)
		self.data_widget = DataWidget()

		self.stacked_widget.addWidget(self.login_widget)
		self.stacked_widget.addWidget(self.data_widget)

	def show_data_screen(self):
		self.stacked_widget.setCurrentWidget(self.data_widget)

		


def main():
	try:
		app = QApplication([])

		window = MainWindow()
		window.show()

		app.exec()

	except Exception as e:
		print(f'Error: {e}')


if __name__ == '__main__':
	main()