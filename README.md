# Python-Huffman-Coding

## Task Description
The Huffman Coding is a lossless data compression algorithm.
There are two phases - encoding and decoding.
You will have to implement the logic for both encoding and decoding. Also, you will need to create the sizing schemas to present a summary.


## Explanation
First, each letter of a provided string is counted. The number of times a letter repeats is also counted. 
Second, most repeated letter of a string is encoded with a code length of 1 (minimum code length). The next most repeated letter as 01 and after that 001 and so on. 

Multiple For Loops are being used, so that makes the overall Time and Space Complexity Big O(n)
