---
marks: 10
topics: [led-matrix]
kind: code
source: {page: 67}
---
Suppose you have 64 bits of information in the character array ***char arr[8]***, that defines the contents of an 8x8 LED matrix. Here, arr[0] is the data for the leftmost column, arr[7] is the data for the rightmost column. The LSB of arr[0] is the data for the bottom-left LED of the matrix, whereas MSB of arr[7] is the top-right LED of the matrix.

Now, write necessary code to be written in MDA-8086 processor so that the pattern saved in the character array is shown in the LED matrix of the MDA board. The pattern is shown for two seconds in **green**, and the next two seconds in **red**; and this alternating pattern repeats forever.
