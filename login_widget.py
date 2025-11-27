from get_connection import get_connection
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QMessageBox, QWidget
from PyQt6.QtCore import Qt


class LoginWidget(QWidget):
	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent
		self.initUI()
		self.conn = get_connection()

	def initUI(self):

		main_layout = QVBoxLayout()
		main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setLayout(main_layout)

		auth_layout = QVBoxLayout()
		self.login_label = QLabel('login')
		self.login_input = QLineEdit()
		self.password_label = QLabel('password')
		self.password_input = QLineEdit()
		self.login_button = QPushButton('Войти')
		self.login_button.setMinimumWidth(0)
		self.login_button.clicked.connect(self.on_login)
		auth_layout.addWidget(self.login_label)
		auth_layout.addWidget(self.login_input)
		auth_layout.addWidget(self.password_label)
		auth_layout.addWidget(self.password_input)
		auth_layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)

		login_frame = QFrame()
		login_frame.setFrameStyle(QFrame.Shape.StyledPanel)
		login_frame.setFixedWidth(300)
		login_frame.setLayout(auth_layout)

		main_layout.addWidget(login_frame)

	def on_login(self):
		login = self.login_input.text()
		password = self.password_input.text()

		
		cursor = self.conn.cursor()

		cursor.execute('SELECT login, password FROM users WHERE login = %s AND password = %s', (login, password))
		result = cursor.fetchone()
		if result:
			self.parent.show_data_screen()
		else:
			QMessageBox.warning(self, "Ошибка", "Логин или пароль не верен")
