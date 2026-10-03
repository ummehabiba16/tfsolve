---
marks: 20
topics: [decision-tree]
kind: numerical
source: {page: 9}
---
Given the dataset shown in Figure 8(a), construct a decision tree which predicts if students obtain Grade "A" or above in the Artificial Intelligence course, based on their GPA (High, Medium, or Low), Attendance Score ($\ge$ 80% or $<$ 80%), and Exam Preparation (Good or Bad). Use the information gain criteria to select the best attribute. Show all the entropy computations at each stage.

| Student No. | GPA | Attendance Score | Exam Preparation | Grade "A" or Above? |
|:-:|:-:|:-:|:-:|:-:|
| 1 | High | >=80% | Good | Yes |
| 2 | Medium | >=80% | Good | Yes |
| 3 | Low | >=80% | Good | Yes |
| 4 | High | <80% | Good | Yes |
| 5 | Low | <80% | Good | No |
| 6 | Low | <80% | Good | No |
| 7 | Medium | <80% | Good | Yes |
| 8 | Medium | >=80% | Bad | No |
| 9 | Low | >=80% | Bad | Yes |
| 10 | High | >=80% | Bad | Yes |

*Figure 8(a)*
