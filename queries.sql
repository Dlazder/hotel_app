CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	login varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	role varchar(255) NOT NULL
);
INSERT INTO users (login, password, role) VALUES ('admin', '123', 'admin'), ('root', '123', 'root');

CREATE TABLE rooms (
	id INT PRIMARY KEY AUTO_INCREMENT,
	number INT NOT NULL,
	floor INT NOT Null,
	status INT,
	FOREIGN KEY (status) REFERENCES statuses(id)
);
INSERT INTO rooms (number, floor, status)
VALUES (1, 1, 1), (2, 1, 1), (3, 1, 1),
(1, 2, 1), (2, 2, 1), (3, 2, 1);

CREATE TABLE statuses (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50)
);
INSERT INTO statuses (name)
VALUES ('Чистый'), ('Грязный'), ('Уборка');

CREATE TABLE visitors (
	id INT PRIMARY KEY AUTO_INCREMENT,
	first_name varchar(255),
	last_name varchar(255),
);






elect number, floor, name from rooms r join statuses s on s.id = r.status;