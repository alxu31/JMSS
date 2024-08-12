SELECT Allocation.grade AS "raw grade", ROUND(SQRT(Allocation.grade)*10, 2) AS "scaled grade", Student.Name AS "student", Allocation.studentID, Allocation.taskID
FROM Allocation, Student
WHERE Allocation.taskID = "2" -- Change for different tasks
AND Allocation.studentID = Student.studentID;

/*
get grade, scaledgrade, student, studenid, taskid
for task 2 (can change)
*/