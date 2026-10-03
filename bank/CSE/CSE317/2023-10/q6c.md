---
marks: 23
topics: [markov-hmm]
kind: numerical
source: {page: 13}
---
A professor wants to know if students are getting enough sleep. Each day, the professor observes whether the students in the class have red eyes. The professor has the following domain theory: The prior probability of getting enough sleep, with no observations, is 0.7. The probability of getting enough sleep on night t is 0.8 given that the student got enough sleep the previous night, and 0.3 if not. The probability of having red eyes is 0.2 if the student got enough sleep, and 0.7 if not. Answer the following questions. (8+15=23)

(i) Build a hidden Markov model (HMM) to formulate the above problem that the professor could use to filter or predict from a sequence of observations. Show the state transition probabilities (transition model) and observation probabilities (sensor model).

(ii) Let the state variable be $X_t = EnoughSleep_t$. Given the evidence values $e_1$ = not red eyes, $e_2$ = red eyes, and $e_3$ = red eyes for the first three days, compute the filtered estimates $P(X_t \mid e_{1:t})$ for each of $t$ = 1,2,3 using filtering algorithm. Using the filtered estimate, compute smoothed probability estimates $P(X_t \mid e_{1:3})$ for each of $t$ = 1,2,3 using forward-backward algorithm.
