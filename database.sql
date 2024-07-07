--RUN THIS FILE IN SQL QUERY RUNNER IN MY-PHP-ADMIN

-- Log in to MySQL
-- mysql -u root -p

-- Create the database
CREATE DATABASE codingblog;

-- Use the database
USE codingblog;

-- Create the Contacts table
CREATE TABLE Contacts (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    phone_num VARCHAR(12) NOT NULL,
    msg VARCHAR(120) NOT NULL,
    date VARCHAR(12),
    email VARCHAR(20) NOT NULL
);

-- Optional: Verify the table creation
SHOW TABLES;
DESCRIBE Contacts;
