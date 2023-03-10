/*
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

 Write an SQL query to find the employees who earn more than their managers.
*/
SELECT e1.name AS Employee
FROM Employee e1, Employee e2
WHERE e2.id=e1.managerId AND e1.salary > e2.salary ;