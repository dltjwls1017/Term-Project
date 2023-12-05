create user bank_user@localhost identified by '1017';
create user bank_user@'%' identified by '1017';
select * from mysql.user;

create database Bank;


grant all privileges on Bank.* to bank_user@localhost with grant option;
grant all privileges on Bank.* to bank_user@'%' with grant option;

flush privileges;

############################################
