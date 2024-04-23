# Write your MySQL query statement below
select project_id, avg(experience_years) as average_years 
from Project,Employee 
where Employee.employee_id=Project.employee_id 
group by project_id