---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) reliability (the OS must bullet-proof itself); (ii) privacy/security: a third-party app cannot read the contacts without consent."
sources: ["Anderson and Dahlin, OSPP, ch. 1 (OS challenges: reliability, security, privacy, fairness)"]
---
- **Reliability:** the OS must continue to work correctly despite bugs or misuse by applications and users.
- **Security:** the OS must enforce its policy (who may do what) and resist malicious attacks.
- **Privacy:** data may be read only by those the owner authorised.
- **Fairness:** resources are shared reasonably among users.

**(i) "An operating system must bullet-proof itself to operate correctly regardless of what an application or user might do"** $\Rightarrow$ **Reliability** (the OS and the other applications keep running correctly even if an application is buggy or malicious; protection of the kernel).

**(ii) A smartphone OS must ensure that a third-party app cannot access the user's contact list without consent** $\Rightarrow$ **Privacy** (personal data is accessible only to those authorised by the user); the mechanism that enforces it, the access-control policy, is a **security** function, so security is also acceptable.
