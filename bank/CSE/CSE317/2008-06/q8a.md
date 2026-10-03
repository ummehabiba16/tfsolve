---
marks: 28
topics: [decision-tree]
kind: numerical
source: {page: 77}
---
Consider the set of training examples given in figure 8(a) each indicating whether or not a person played tennis denoted by the Boolean classification variable PlayTennis, given four attributes: Outlook, Temperature, Humidity and Wind.

Find the information gain of each attribute. Based on the calculated information gains, select the attribute for the root of the decision tree. Using the information gain criterion choose the best attribute to classify the examples at each subsequent steps. Draw the complete decision tree learned from this set of examples.

| Day | Outlook | Temperature | Humidity | Wind | PlayTennis |
|:--|:--|:--|:--|:--|:--|
| D1 | Sunny | Hot | High | Weak | No |
| D2 | Sunny | Hot | High | Strong | No |
| D3 | Overcast | Hot | High | Weak | Yes |
| D4 | Rain | Mild | High | Weak | Yes |
| D5 | Rain | Cool | Normal | Weak | Yes |
| D6 | Rain | Cool | Normal | Strong | No |
| D7 | Overcast | Cool | Normal | Strong | Yes |
| D8 | Sunny | Mild | High | Weak | No |
| D9 | Sunny | Cool | Normal | Weak | Yes |
| D10 | Rain | Mild | Normal | Weak | Yes |
| D11 | Sunny | Mild | Normal | Strong | Yes |
| D12 | Overcast | Mild | High | Strong | Yes |
| D13 | Overcast | Hot | Normal | Weak | Yes |
| D14 | Rain | Mild | High | Strong | No |

*Figure 8(a): Examples for the PlayTennis domain*
