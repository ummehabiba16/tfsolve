---
marks: 20
topics: [deadlock-detection-graph]
kind: numerical
source: {page: 26}
params:
  type: resource_graph
  instances_per_resource: 1
  processes: [A, B, C, D, E]
  resources: [1, 2, 3, 4, 5]
  holds:
    A: [1, 3]
    B: [4]
    C: []
    D: []
    E: [5]
  requests:
    A: [2]
    B: [3, 5]
    C: [2]
    D: [2]
    E: [1]
  detection_start_node: B
---
Draw the resource graph for the following scenario where A, B, C, D, and E denote processes and 1, 2, 3, 4, and 5 denote resource types. There exists only one resource of each type. Show the steps of the execution of the deadlock detection algorithm on the constructed graph starting from node B.

(i) Process A holds 1 and 3, wants 2

(ii) Process B holds 4, wants 3 and 5

(iii) Process C holds nothing, wants 2

(iv) Process D holds nothing, wants 2

(v) Process E holds 5 and wants 1
