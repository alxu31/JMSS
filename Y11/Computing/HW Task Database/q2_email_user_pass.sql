WITH const AS (SELECT "@jmss.vic.edu.au" AS suffix) -- Temp var storing email suffix to add to user to create email
SELECT Student.studentID, Student.Name, CONCAT(Student.loginUser, const.suffix) AS "email", Student.loginUser AS "user", Student.loginPass AS "password"
FROM Student, const;

/*
get studentid, student, user + "@jmss.vic.edu.au", user, password
*/