create table customer_table(
c_id int primary key,
c_name varchar(50),
c_address varchar(50),
city varchar(50)
)



insert into customer_table (c_id,c_name,c_address,city)
values
(1,'Rohit','A-block','Gwalior'),
(2,'Akash','B-block','Indore'),
(3,'Abhay','C-block','Jhashi'),
(4,'Vikas','D-block','Banglore');

create table order_table
(
ord_id int ,
Item varchar(50),
Quantity int,
price int ,
c_id int,
PRIMARY KEY (ord_id),
FOREIGN KEY (c_id) REFERENCES customer_table(c_id)
);
select * from customer_table;
select * from order_table;
insert into order_table (ord_id,Item,Quantity,Price,c_id)
values
(1,'mobile',1,1200,1),
(2,'keyboard',1,1200,2),
(3,'charger',2,1300,3),
(4,'lamp',3,1500,1),
(5,'tv',4,100000,2),
(6,'table',1,1100,4);

-- delete from customer_table where c_id=3;  
-- above line can not delete customer 3 because customer table is connected to order table

-- dropping or appling alter key on table using alter
alter table order_table drop constraint order_table_ibfk_1;
alter table order_table add foreign key (c_id) references customer_table(c_id);

-- No Action 
delete from customer_table where c_id=2;
update customer_table set c_id=7 where c_id=2;


 
