use testing;

create table voter_table
(
voter_id int,
voter_name varchar(50),
voter_address varchar(50)
);

create table voter_city
(
city_id int,
city_name varchar(50),
voter_id int
);

insert into voter_table values(1,'akash','a');
insert into voter_table values(2,'abhay','b');
insert into voter_table values(3,'rohit','c');
insert into voter_table values(4,'jeetu','d');

select * from voter_table;

alter table voter_table modify column voter_name varchar(50) not null;
insert into voter_table values(5,'jeetu1','e');
insert into voter_table (voter_id,voter_name,voter_address) 
values(7,'jeetu2','e');
insert into voter_table (voter_id,voter_address) 
values(8,'f');

-- we can not add not null contraint on column if column is already present 
-- one null values

-- appling unique constraint
alter table voter_table add unique(voter_id);

-- appling and dropping primary constraint 
alter table voter_table add primary key(voter_id);
alter table voter_table drop primary key;

-- appling and dropping foreign key 
alter table voter_city add foreign key(voter_id)
 references voter_table(voter_id);
alter table voter_city drop foreign key voter_city_ibfk_1;

-- appling and dropping check
alter table voter_table add column voter_age int;
select * from voter_table;
insert into voter_table values(23,'zakir','ad',24);
insert into voter_table values(24,'zakir1','ade',29);
alter table voter_table add check(voter_age>=18);
 
 -- appling and dropping default
 alter table voter_table alter voter_age set default 18;
 insert into voter_table (voter_id,voter_name,voter_address)
 values(8,'coco','ades');
 select * from voter_table;
 alter table voter_table alter voter_age drop default;


