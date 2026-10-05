---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Gains at the root: Outlook 0.246, Humidity 0.151, Wind 0.048, Temperature 0.029, so the root is Outlook. Overcast -> Yes. Sunny (2+, 3-): Humidity 0.971 (Temperature 0.571, Wind 0.020): High -> No, Normal -> Yes. Rain (3+, 2-): Wind 0.971 (Temperature and Humidity 0.020): Weak -> Yes, Strong -> No."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "Mitchell, Machine Learning, ch. 3 (PlayTennis)", "AIMA 3e sec. 18.3"]
---
**Root** (14 examples: 9 Yes, 5 No): $H(S)=-\frac9{14}\log_2\frac9{14}-\frac5{14}\log_2\frac5{14}=0.940$.

| Attribute | Values (Yes, No) | Remainder | Gain |
|:--|:--|:-:|:-:|
| Outlook | Sunny (2,3): 0.971; Overcast (4,0): 0; Rain (3,2): 0.971 | $\frac5{14}0.971\times2=0.694$ | **0.246** |
| Temperature | Hot (2,2): 1; Mild (4,2): 0.918; Cool (3,1): 0.811 | 0.911 | 0.029 |
| Humidity | High (3,4): 0.985; Normal (6,1): 0.592 | 0.789 | 0.151 |
| Wind | Weak (6,2): 0.811; Strong (3,3): 1 | 0.892 | 0.048 |

**Outlook** is the root. Overcast (D3, D7, D12, D13) is all Yes, so it is a leaf **Yes**.

**Outlook = Sunny** (D1, D2, D8, D9, D11: 2 Yes, 3 No; $H=0.971$):

| Attribute | Values | Gain |
|:--|:--|:-:|
| Temperature | Hot (0,2), Mild (1,1), Cool (1,0) | $0.971-0.4=0.571$ |
| Humidity | High (0,3), Normal (2,0) | **0.971** |
| Wind | Weak (1,2), Strong (1,1) | 0.020 |

Split on **Humidity**: High gives No, Normal gives Yes.

**Outlook = Rain** (D4, D5, D6, D10, D14: 3 Yes, 2 No; $H=0.971$):

| Attribute | Values | Gain |
|:--|:--|:-:|
| Temperature | Mild (2,1), Cool (1,1) | 0.020 |
| Humidity | High (1,1), Normal (2,1) | 0.020 |
| Wind | Weak (3,0), Strong (0,2) | **0.971** |

Split on **Wind**: Weak gives Yes, Strong gives No.

**Complete decision tree.**

```text
Outlook ?
|-- Sunny    -> Humidity ?
|                |-- High   -> No
|                |-- Normal -> Yes
|-- Overcast -> Yes
|-- Rain     -> Wind ?
                 |-- Weak   -> Yes
                 |-- Strong -> No
```

It classifies all 14 examples correctly. Temperature is never used.
