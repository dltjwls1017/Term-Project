create user blauser@localhost identified by 'blapw';
create user blauser@'%' identified by 'blapw';
select * from mysql.user;

create database bladb;


grant all privileges on bladb.* to blauser@localhost with grant option;
grant all privileges on bladb.* to blauser@'%' with grant option;

flush privileges;

############################################
