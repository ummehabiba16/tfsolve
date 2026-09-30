---
marks: 15
topics: [deadlock-detection-graph]
kind: numerical
source: {page: 9}
params:
  type: resource_graph
  instances_per_resource: 1
  processes: [A, B, C, D]
  resources: [1, 2, 3, 4, 5, 6]
  holds:
    A: [6]
    B: [1]
    C: [4]
    D: [5]
  requests:
    A: [1, 3]
    B: [4]
    C: [3, 5]
    D: [6]
  detection_start_node: C
---
Construct the resource graph for the following scenario where A, B, C, and D denote processes and 1, 2, 3, 4, 5, and 6 denote resource types. There exists only one resource of each type. Show the steps of the execution of the deadlock detection algorithm on the constructed graph starting from node C.

(i) Process A holds 6, and wants 1 and 3

(ii) Process B holds 1, and wants 4

(iii) Process C holds 4, and wants 3 and 5

(iv) Process D holds 5, and wants 6
