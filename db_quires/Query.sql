-- Create database
CREATE DATABASE IF NOT EXISTS ums;

-- =====================================================
-- Development Database Setup
-- Replace DB_PASSWORD_FROM_ENV with your own password.
-- Do NOT use production credentials.
-- =====================================================

-- Create application user
-- Set user name and user passowrd that you set in .env DB_PASSWORD nad DB_NAME
CREATE USER IF NOT EXISTS 'ums_user'@'%'
IDENTIFIED BY 'DB_PASSWORD_FROM_ENV';

-- Grant full access to the ums database
GRANT ALL PRIVILEGES ON ums.* TO 'ums_user'@'%';

-- Reload privilege tables
FLUSH PRIVILEGES;

-- Verify granted permissions
SHOW GRANTS FOR 'ums_user'@'%';

-- Verify user exists
SELECT User, Host
FROM mysql.user
WHERE User = 'ums_user';


-- =====================================================
-- Optional Maintenance Commands
-- Uncomment only if you know what you're doing
-- =====================================================

-- DROP DATABASE ums;

USE ums;

-- View data
SELECT * FROM admin;
SELECT * FROM courses;
SELECT * FROM enrollments;
SELECT * FROM faculties;
SELECT * FROM students;
