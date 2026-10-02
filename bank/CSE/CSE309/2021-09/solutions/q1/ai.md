---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "#line n 'file' is a C preprocessor directive that resets the compiler's line number (and optionally file name) for the following lines, changing \\_\\_LINE\\_\\_, \\_\\_FILE\\_\\_ and error messages; used mainly by code generators (Lex, Yacc, cpp) so that errors point to the original source."
sources: ["MMA introduction slides 22-25 (Line Control Directive)"]
---
**Concept.** When the compiler finds an error, it reports the file name and line number. The C/C++ preprocessor's **line control directive**

```c
#line number "filename"
```

tells the compiler to treat the **next** source line as line `number` of file `filename` (the file name is optional). From that point on, `__LINE__`, `__FILE__`, error and warning messages, and debugging information use the new numbering. In effect it resets the line counter.

**Example** (from the slides; the file is `clinecontrol.cpp`):

```cpp
// Demonstrate line control, clinecontrol.cpp
#include <iostream>
using namespace std;
int main()
{
    cout << "CSE 309 line control" << endl;
    cout << __LINE__ << " "
         << __FILE__ << endl;
#line 15 "ourdemo.cpp"
    cout << __LINE__
         << " " << __FILE__
         << endl;
    cout << __LINE__ << endl;
}
```

Output:

```text
CSE 309 line control
9 clinecontrol.cpp
16 ourdemo.cpp
19
```

In the original file (as run on the slide), the first `__LINE__` is on line 9 of `clinecontrol.cpp`. After `#line 15 "ourdemo.cpp"`, the line following the directive is counted as line 15 of `ourdemo.cpp`, and numbering continues from there. So the later `__LINE__`s print 16 and 19 with file name `ourdemo.cpp`, regardless of their real position in `clinecontrol.cpp`.

**Use.** It matters mostly for programs that **generate C code**: Lex (`lex.yy.c`), Yacc (`y.tab.c`) and other preprocessors insert `#line` directives so that compiler errors refer to the line in the original `.l` or `.y` file that the programmer wrote, not to the generated file. The preprocessor itself also emits line markers after `#include` expansion so that line numbers stay correct.
