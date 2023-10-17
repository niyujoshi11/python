# first you had to install mysql installer from this site
```
https://dev.mysql.com/downloads/installer/
```

Than as it is set up & user set up

Some basic commands:

show the database:
- show database

create the database:
- create database dbname:

use the database:
- use  dbname

create the table:

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    birthdate DATE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


# for installation to insall mysql connector

- pip install mysql-connector-python