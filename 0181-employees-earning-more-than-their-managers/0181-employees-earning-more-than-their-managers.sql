# Write your MySQL query statement below
SELECT E.name AS Employee FROM Employee E JOIN Employee M ON E.managerId=M.id AND E.salary>M.salary;
