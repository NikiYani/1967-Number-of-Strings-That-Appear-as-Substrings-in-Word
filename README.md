# 1967. Number of Strings That Appear as Substrings in Word

Given an array of strings patterns and a string word, return the number </br>
of strings in patterns that exist as a substring in word. </br>

A substring is a contiguous sequence of characters within a string. </br>

## Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc" </br> 
Output: 3 </br>
Explanation: </br>
- "a" appears as a substring in "abc". </br>
- "abc" appears as a substring in "abc". </br>
- "bc" appears as a substring in "abc". </br>
- "d" does not appear as a substring in "abc". </br>
3 of the strings in patterns appear as a substring in word. </br>

## Example 2:

Input: patterns = ["a","b","c"], word = "aaaaabbbbb" </br>
Output: 2 </br>
Explanation: </br>
- "a" appears as a substring in "aaaaabbbbb". </br>
- "b" appears as a substring in "aaaaabbbbb". </br>
- "c" does not appear as a substring in "aaaaabbbbb". </br>
2 of the strings in patterns appear as a substring in word. </br>

## Example 3:

Input: patterns = ["a","a","a"], word = "ab" </br>
Output: 3 </br>
Explanation: Each of the patterns appears as a substring in word "ab". </br>

## Constraints:

1 <= patterns.length <= 100 </br>
1 <= patterns[i].length <= 100 </br>
1 <= word.length <= 100 </br>
patterns[i] and word consist of lowercase English letters. </br>
