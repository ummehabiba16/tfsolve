---
marks: 24
topics: [exceptions-386, privilege-protection]
kind: analysis
source: {page: 66}
note: "Sections are named ST1 and ST2, then referred to as 'Section S1 and S2' in (ii), as printed."
---
As a System Software Developer of a world renowned device manufacturing company, you are writing an exception handler for some possible interrupt conditions of a new device. Your handler code contains the following sections: (9+15)

Section PL: This section contains one or more privileged instruction (s).

Section ST1: This section contains stack operations.

Section H: This section contains the instructions related to handling the interrupt.

Section ST2: This section contains stack operations.

Section IR: This section contains an IRET instruction.

(i) Can you explain what could be the reason for having Section PL, Section ST1 and Section ST2?

(ii) Looking at your code, your genius little brother suggests two alternatives as follows: in alternative #1, you do not need Section PL and in alternative #2, you do not need Section S1 and S2, but you need another section with one instruction after Section IR. Explain the two alternatives.
