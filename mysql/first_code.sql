show databases;

create database testing;

use testing;

create table student_bio_data (
stdid int,
student_name varchar(50),
roll_no int);

select * from 	student_bio_data;

insert into student_bio_data values(1,'akash',1);
insert into student_bio_data values(2,'golu',2);
insert into student_bio_data values(2,'rahul',3);
insert into student_bio_data values(4,'rahul',4);


-- insert into student_bio_data (stdid,studet_name,roll_no) 
-- values();

update student_bio_data  set student_name='jyoti' where roll_no=3;


