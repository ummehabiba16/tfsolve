---
marks: 10
topics: [deadlock-detection-graph]
kind: numerical
source: {page: 35}
note: "Printed as 'P3, ad P4'. The matrices are read as C = current allocation, R = request, E = existing resource vector, A = available vector (matching their listing in the question)."
---
Write down the algorithm for deadlock detection with multiple resources of each type with describing each of the matrices (C, R, E, A) the algorithm requires.

Consider the following state of a system with four processes, P1, P2, P3, ad P4, and five types of resources, RS1, RS2, RS3, RS4, and RS5:

$$C=\begin{pmatrix}0&1&1&1&2\\0&1&0&1&0\\0&0&0&0&1\\2&1&0&0&0\end{pmatrix}$$

$$R=\begin{pmatrix}1&1&0&2&1\\0&1&0&2&1\\0&2&0&3&1\\0&2&1&1&0\end{pmatrix}$$

$$E=(2\;\;4\;\;1\;\;4\;\;4)$$

$$A=(0\;\;1\;\;0\;\;2\;\;1)$$

Using the above deadlock detection algorithm, find out whether there is a deadlock in the system and identify the processes that are deadlocked.
