-- 删除数据库
DROP SCHEMA IF EXISTS testing;

-- 创建数据库
CREATE SCHEMA testing;

-- 进入数据库
USE testing;


-- 创建accounts表
CREATE TABLE IF NOT EXISTS accounts
(
    accountid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    roleid INT NOT NULL
);
