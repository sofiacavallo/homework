-- 1/ List the following details of each employee: employee number, last name, first name, gender, and salary.
	SELECT employees.emp_no, last_name, first_name, gender, salaries.salary
	FROM employees
	LEFT JOIN salaries
	ON employees.emp_no = salaries.emp_no;
	
-- 2/ List employees who were hired in 1986.
	SELECT emp_no
	FROM employees
	WHERE hire_date BETWEEN '19860101' AND '19861231'

-- 3/ List the manager of each department with the following information department number, department name, the manager's employee number, last name, first name, start date, end date	
	SELECT dept_manager.dept_no, dept_manager.emp_no, dept_manager.from_date, dept_manager.to_date, departments.dept_name, employees.first_name, employees.last_name
	FROM dept_manager
	FULL OUTER JOIN departments
	ON dept_manager.dept_no = departments.dept_no
	INNER JOIN employees
	ON employees.emp_no = dept_manager.emp_no

-- 4/ List the department of each employee with the following information: employee number, last name, first name, and department name.
	SELECT employees.emp_no, employees.last_name, employees.first_name, dept_emp.dept_no, departments.dept_name
	FROM employees
	INNER JOIN dept_emp
	ON employees.emp_no = dept_emp.emp_no
	FULL OUTER JOIN departments
	ON departments.dept_no = dept_emp.dept_no
	ORDER BY employees.emp_no
	
-- 5/ List all employees whose first name is "Hercules" and last names begin with "B."
	SELECT emp_no
	FROM employees
	WHERE first_name = 'Hercules' AND last_name LIKE 'B%'

-- 6/ List all employees in the Sales department, including their employee number, last name, first name, and department name.
	SELECT dept_emp.emp_no, dept_emp.dept_no, departments.dept_name, employees.first_name, employees.last_name
	FROM dept_emp
	INNER JOIN departments
	ON dept_emp.dept_no = departments.dept_no
	INNER JOIN employees
	ON employees.emp_no = dept_emp.emp_no
	WHERE departments.dept_name = 'Sales'
	
-- 7/ List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
	SELECT dept_emp.emp_no, dept_emp.dept_no, departments.dept_name, employees.first_name, employees.last_name
	FROM dept_emp
	INNER JOIN departments
	ON dept_emp.dept_no = departments.dept_no
	INNER JOIN employees
	ON employees.emp_no = dept_emp.emp_no
	WHERE departments.dept_name = 'Sales' OR departments.dept_name = 'Development'

-- 8/ In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
	SELECT last_name, COUNT (last_name)
	FROM employees
	GROUP BY last_name 
	ORDER BY count desc