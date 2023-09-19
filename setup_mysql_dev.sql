-- script prepares a database server for the project : hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant privileges to hbnb_dev user
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- ensures user has the required privileges
FLUSH PRIVILEGES;
