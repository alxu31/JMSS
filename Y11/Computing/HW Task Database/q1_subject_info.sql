SELECT Teacher.teacherID, Teacher.Name, Subject.Name, Subject.subjectID
FROM Teacher, Subject
WHERE Teacher.teacherID = Subject.teacherID
ORDER BY Subject.subjectID;

/*
get teacherid, teacher, subject, subjectid
order by subjectid low->high
*/