---
marks: 20
topics: [lex-tool]
kind: analysis
source: {page: 41}
note: "The figure shows the Flex file in two columns; the right column (the main function) follows the closing %% line here. 'JamesBondLex.1' is printed in the question text while the figure title reads JamesBondLex.l."
---
James Bond was one of the best spies in the history of British Secret Intelligence Service MI6. MI6 are searching for their next James Bond. To check a candidate potential, MI6 are giving the Flex code named "JamesBondLex.1" (Given in the figure for Question 1(b)) to the candidate to explore. They are asking the candidate to write the contents of a text file named "DecByPotentialNextJamesBond.txt", that is produced when the generated scanner from the Flex code is run over the input file named "EncByMI6.txt" (Given in the figure for Question 1(b)).

**JamesBondLex.l**

```text
%option noyywrap
%s JESPYSTATE
%{
#include<stdio.h>
#include<stdlib.h>
FILE *decOut;
%}
whitespace [ \t\n]
JamesBond [JamesBond]
AlphaNumeric [a-zA-Z0-9$]
%%
[James]{3} { fprintf(decOut,"<James,%s>\r\n",yytext);}
Bond { fprintf(decOut,"<Bond,%s>\r\n",yytext); }
{JamesBond}+ { fprintf(decOut,"<JamesBond,%s>\r\n",yytext); }
(best)* { fprintf(decOut,"<(best)*,%s>\r\n",yytext); }
best* { fprintf(decOut,"<best*,%s>\r\n",yytext); }
(Johnny|Eng) { BEGIN JESPYSTATE;
               fprintf(decOut,"<JESPYBEGIN,%s>\r\n",yytext);}
<JESPYSTATE>English { fprintf(decOut,"<JESPYS,%s>\r\n",yytext); }
<JESPYSTATE>("just"|"average") { fprintf(decOut,"<TrCompare,%s>\r\n",yytext); }
<JESPYSTATE>{whitespace}* { }
<JESPYSTATE>[^-just \t\naverage]* { BEGIN INITIAL;
                                    fprintf(decOut,"<JESPYEND,%s>\r\n",yytext); }

{AlphaNumeric}* { fprintf(decOut,"<AN,%s>\r\n",yytext); }

<JESPYSTATE>. { }
. { }

%%
int main(int argc,char *argv[])
{
    if(argc!=2)
    {
        printf("Please provide input file name and try again\n");
        return 0;
    }

    FILE *fin=fopen(argv[1],"r");
    if(fin==NULL)
    {
        printf("Cannot open the specified file\n");
        return 0;
    }
    decOut=
fopen("DecByPotentialNextJamesBond.txt","w");

    yyin= fin;
    yylex();
    fclose(yyin);
    fclose(decOut);
    return 0;
}
```

**EncByMI6.txt**

```text
JamesBond JamesBond British spy...
Johnny-English-just average pBritish spy...
```

*Figure for Question 1(b)*

Now, write down the correct and complete answer that a potential candidate should provide in reply to MI6's tricky (!) question.
