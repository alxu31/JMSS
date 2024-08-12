SELECT ROUND(AVG(Allocation.grade),2) AS "student average", Student.Name AS "student", Student.studentID
FROM Allocation, Student
WHERE Allocation.studentID = Student.studentID
GROUP BY Allocation.studentID
ORDER BY ROUND(AVG(Allocation.grade),2) DESC;

/*
get avggrade, student, studentid
group avgs if they have the same studentid
order by avggrade high->low
*/