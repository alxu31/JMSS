SELECT ROUND(AVG(Allocation.grade),2) AS "task average", Allocation.taskID, Subject.Name AS "subject", Task.subjectID
FROM Allocation, Task, Subject
WHERE Allocation.taskID = Task.taskID
AND Task.subjectID = Subject.subjectID
GROUP BY Allocation.taskID;

/*
get avggrade, taskid, subject, subjectid
group avgs if they have the same taskid
*/