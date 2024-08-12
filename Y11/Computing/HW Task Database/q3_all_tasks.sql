SELECT Task.taskID, Task.dueDate, Task.title, Task.details, subject.Name AS "subject", Task.subjectID
FROM Task, Subject
WHERE Task.subjectID = subject.SubjectID
ORDER BY CONCAT(
	SUBSTR(Task.dueDate, 7, 4),
	SUBSTR(Task.dueDate, 4, 2),
	SUBSTR(Task.dueDate, 1, 2)); -- Creates a new string in the form of yyyymmdd and orders based off that
	
/*
get taskid, duedate, title, details, subject, subjectid
order by yyyymmdd (date)
*/