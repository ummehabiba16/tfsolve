---
marks: 11
topics: [symbol-table-management, scope-access]
kind: diagram
source: {page: 51}
note: "Marks printed as (3+8=11)."
---
In the context of semantic analysis, what is scope? Draw the spaghetti stack interpretation of symbol tables to disambiguate scopes explicitly for the following code snippet.

```java
public class Base {
    public int a = 0;
}

public class Derived extends Base {
    public int b = 10;
}

public class Test extends Derived {
    public int a = 20;
    public void show ( ) {
        int a = 30;
        System.out.println(a);
        System.out.println(this.a);
        System.out.println(super.a);
    }
}
```
