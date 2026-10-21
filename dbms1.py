
# select * from employee;
# select * from employee where Exprience between 1 and 3;

# /*like operator*/

# select * from employee where lastname like 'P%';

# /*limit operator = used to number of rows */

# select * from employee order by exprience limit 3;

# /* IS NULL = */
# insert into employee values(106 , 'Yash' , 'Joshi' , 'M' , 'president' , 'HR' , ' ' , null);
# insert into employee values(107 , 'Rohan' , 'Gurav' , 'F' , 'president' , 'HR' , ' ' , null);

# use Organization;

# select * from employee;

# select count(*) from employee;
# select count(empid)from employee where dept = 'Finance';
# select Min(Exprience) from employee;

# select Max(Exprience) from employee;
# select sum(Exprience) from employee;
# select Avg(Exprience)as emp_exr from employee;
# select dept , count(*) as employee_count from employee group by dept;
# select role , count(*) as employee_count from employee group by role;
# select gender , count(*) as employee_count from employee group by gender;
# select * from employee;

# select dept , sum(Exprience)as total_exprience from employee group by dept having total_exprience >= 1 and total_exprience <=5;


# select dept , sum(Exprience)as total_exprience from employee group by dept having total_exprience >= 1 or total_exprience <=1;
