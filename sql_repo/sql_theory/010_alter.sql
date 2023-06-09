ALTER TABLE Employees
ADD COLUMN Age INT;

ALTER TABLE Employees
ALTER COLUMN Salary DECIMAL(12, 2);

ALTER TABLE Employees
DROP COLUMN Age;

ALTER TABLE Employees
ADD CONSTRAINT PK_Employees PRIMARY KEY (EmployeeID);


-- The ALTER statement in SQL is used to modify the structure and metadata of database objects, such as tables, columns, constraints, and other properties. It does not directly update the values of existing rows in the table.

-- The UPDATE statement in SQL is used to modify the values of existing rows in a table. It allows you to update specific columns or multiple columns based on specified conditions. The UPDATE statement directly affects the data within the table, rather than modifying the structure or metadata of the table.
