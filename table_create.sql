use Bank;
create table bankaccountlist(
계좌번호 bigint not null,  
이름 varchar(4) not null,
잔액 bigint not null);

create table IF NOT EXISTS history(
계좌번호 varchar(30) not null,  
이름 varchar(20) not null,
입출금 varchar(20) not null,
금액 bigint not null,
잔액 bigint not null);

