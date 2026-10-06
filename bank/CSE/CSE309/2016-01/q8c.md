---
marks: 15
topics: [simple-codegen, register-allocation]
kind: numerical
source: {page: 50}
note: "The last three columns are blank in the paper (to be filled in by the student)."
---
What are register descriptor, address descriptor, and spilling? Assume the system has only two registers, provide the status of register descriptor, address descriptor, and the variable spilled for the following code:

| Statements | Code Generated | Register Descriptor | Address Descriptor | Spilled Variable |
|:--|:--|:--|:--|:--|
| `t := a - b` | `MOV a, R0` | | | |
| | `SUB b, R0` | | | |
| `u := a - c` | `MOV a, R1` | | | |
| | `SUB c, R1` | | | |
| `v := t + u` | `ADD R1, R0` | | | |
| `d := v + u` | `ADD R1, R0` | | | |
| | `MOV R0, d` | | | |
