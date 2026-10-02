---
marks: 10
topics: [activation-records]
kind: analysis
source: {page: 13}
---
Consider that the following code computes the binomial coefficient recursively.

```cpp
int binCoeff(int n, int r)
{
    if (r == 0 || r == n) //base cases
        return 1;

    return binCoeff(n - 1, r - 1) + binCoeff(n - 1, r);
}

int main()
{
    cout << binCoeff(5, 3);
    return 0;
}
```

Now, answer the questions below.

(i) Show the complete activation tree for it.

(ii) What is the maximum number of activation records that will reside in the stack during execution of the program? Explain your answer using your activation tree.

(iii) What does the control stack and its activation records look like when the base cases is satisfied for the first time and the function is about to return. Show only the arguments in an activation record.
