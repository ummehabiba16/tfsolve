---
marks: 18
topics: [planning]
kind: analysis
source: {page: 54}
set_by: [UNKNOWN]
---
A flat tire problem is defined by the following predicates and actions.

Initial state - at (flat, axle) $\land$ at (spare, trunk)

Goal state - at (spare, axle).

Actions:

(i) remove (spare, trunk) means spare tire is taken out from trunk and put on ground.

(ii) remove (flat, axle) means flat tire is taken out from axle and put on ground.

(iii) puton (spare, axle) means spare tire is taken out from ground and put on axle.

(iv) leaveovernight means neither flat nor spare tire is on ground or on axle or in trunk.

How can a partial-order-planning help to achieve the goal state from the initial state for the "flat-tire" problem?
