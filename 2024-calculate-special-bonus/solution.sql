SELECT employee_id, IF(employee_id % 2 AND name NOT LIKE 'M%', salary, 0) as 'bonus'
FROM Employees
ORDER BY employee_id;
