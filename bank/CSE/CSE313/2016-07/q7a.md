---
marks: 18
topics: [process-thread]
kind: analysis
source: {page: 48}
note: "Printed 'thread _join' in (vi). The output in the figure prints 'Thread N returned 10N', while the program prints 'Thread %d returned with %ld' (a mismatch present in the paper itself)."
---
Now answer the following questions about the figure for Question 7(a) (the program and its output are given in the stem). (6x3=18)

(i) Why has the "Hello" message from thread 3 been printed before the "Hello" message from thread 2? Is it guaranteed that this sequence is always maintained?

(ii) Why has the "Thread returned" message from thread 3 been printed after the "Thread returned" message from thread 2? Is it guaranteed that this sequence is always maintained?

(iii) Why have the "Hello" message been merged with "Thread returned" messages?

(iv) What is the minimum and maximum number of threads that could exist when main thread prints "Thread returned" message?

(v) What is the minimum and maximum number of times that the thread 2 enters the READY state on a uniprocessor?

(vi) When thread _join returns for thread 3, what is the state of the main thread?
