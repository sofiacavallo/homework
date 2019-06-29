-- TABLE SCHEMATA
-- Create a table for EMPLOYEES.
CREATE TABLE employees (
	emp_no INT PRIMARY KEY,
	birth_date DATE,
	first_name VARCHAR (40),
	last_name VARCHAR (40),
	gender VARCHAR (1),
	hire_date DATE
);
-- View table columns and data types.
Select * FROM employees;

-- Create a table for DEPARTMENTS.
CREATE TABLE departments (
	dept_no VARCHAR (6) PRIMARY KEY,
	dept_name VARCHAR (40)
);
-- View table columns and data types.
Select * FROM departments;

-- Create a table for DEPARTMENT EMPLOYEES.
CREATE TABLE dept_emp (
	emp_no INT,
	dept_no VARCHAR (6),
	from_date DATE,
	to_date DATE,
	FOREIGN KEY(emp_no) REFERENCES employees(emp_no) ON DELETE SET NULL,
	FOREIGN KEY(dept_no) REFERENCES departments(dept_no) ON DELETE SET NULL
);
-- View table columns and data types.
Select * FROM dept_emp;

-- Create a table for TITLES.
CREATE TABLE titles (
	emp_no INT,
	title VARCHAR (40),
	from_date DATE,
	to_date DATE,
	FOREIGN KEY(emp_no) REFERENCES employees(emp_no) ON DELETE SET NULL
);
-- View table columns and data types.
Select * FROM titles;

-- Create a table for SALARIES.
CREATE TABLE salaries (
	emp_no INT,
	salary INT,
	from_date DATE,
	to_date DATE,
	FOREIGN KEY(emp_no) REFERENCES employees(emp_no) ON DELETE SET NULL
);
-- View table columns and data types.
Select * FROM salaries;

-- Create a table for DEPARTMENT MANAGERS.
CREATE TABLE dept_manager (
	dept_no VARCHAR (6),
	emp_no INT,
	from_date DATE,
	to_date DATE,
	FOREIGN KEY(dept_no) REFERENCES departments(dept_no) ON DELETE SET NULL,
	FOREIGN KEY(emp_no) REFERENCES employees(emp_no) ON DELETE SET NULL
);
-- View table columns and data types.
Select * FROM dept_manager;
