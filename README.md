 ## Useful links:

 [MySql python connector docs](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html)

 [os walk method for iterating through directories](https://www.geeksforgeeks.org/os-walk-python/)

 [take advantage of datetime data type in your queries](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)

 [using variables in MySQL](https://www.mysqltutorial.org/mysql-basics/mysql-variables/)


When testing:

start:
make db

finished:
make down
make clean

Useful commands:

## 5. Access MySQL in a Running Docker Container
docker exec -it mysqldb mysql -u root -p

## 6. Show Databases in MySQL
SHOW DATABASES;

## 7. Create a Database
CREATE DATABASE testdb;

## 8. Use a Database
USE testdb;

## 9. Show Tables in the Selected Database
SHOW TABLES;

## 10. Create a Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

## 11. Insert Data into Table
INSERT INTO users (name, age) VALUES ('Alice', 28);

## 12. Select All Data from Table
SELECT * FROM users;

## 13. Update Data in Table
UPDATE users SET age = 29 WHERE name = 'Alice';

## 14. Delete Data from Table
DELETE FROM users WHERE name = 'Alice';

## 15. Drop a Table
DROP TABLE users;

## 16. Drop a Database
DROP DATABASE testdb;

## 17. Exit MySQL
EXIT;

## 18. View Docker Container Logs (for debugging)
docker logs mysqldb