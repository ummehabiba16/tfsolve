---
marks: 13
topics: [bn-representation]
kind: numerical
mandatory: true
source: {page: 7}
---
Suppose, you want to model a Bayesian network to represent how instructors give letters of recommendation ("recommend" or "not recommend") based on students' grades ("good" or "bad") in their courses. A student's grade in a course depends on Course difficulty and Student Intelligence. Courses are classified as "difficult" or "easy". A student is either "highly intelligent" or "low in intelligence" determined by an intelligence test taken after admission. If a student has high intelligence, the probability of getting a good grade is 90%, regardless of course difficulty. If a student has low intelligence, then the chance of getting a good grade is 80% in easy courses and 60% in difficult courses. If a student receives a good grade, the instructor gives a recommendation with a 95% probability. If a student receives a bad grade, the instructor still recommends him with a 20% probability due to personal bias. Among 500 students in the department, 100 students have high intelligence, and 400 have low intelligence. Out of 150 courses, 25 are difficult, and 125 are easy.

Construct a Bayesian network for the above problem and provide all the conditional probability tables (CPTs).
