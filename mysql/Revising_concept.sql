use testing;

create table schools_tbls(
sch_id int,
sch_name varchar(50),
sch_addres varchar(50)
);

insert into schools_tbls values(1,'tanwer','thatipur');
insert into schools_tbls values(1,'model','9 dukan');


select * from sch_info;

-- changing table name
rename table schools_tbls to school_data;
alter table school_data rename to school_info;
alter table school_info rename sch_info;

-- drop table
drop table sch_info;

-- adding new column
alter table sch_info add column sch_rank int;

-- drop column
alter table sch_info drop column sch_rank;

-- drop row
insert into sch_info values(2,'model1','10 dukan');
select * from sch_info;
delete from sch_info where sch_id=2;