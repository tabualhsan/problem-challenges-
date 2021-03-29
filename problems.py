
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        
#         given 2 strings check if the strings have the same letters 
#         if they do return True else Return False
#         need to loop through all the letters in string 1 one and see if they match all the letter in string 2 


        
#         if count of letters in n == letter in t = count == True 
        
#         key = letter 
#         value = number of time that letter is in the string 
        
        number_dict = {}
        number_dict_2 = {}
        
        
        for n in s:
            if n in number_dict:
                number_dict[n] = number_dict[n] + 1 
            else:
                number_dict[n] = 1 
                
        for o in t:
            if o in number_dict_2:
                number_dict_2[o] = number_dict_2[o] + 1 
            else:
                number_dict_2[o] = 1 
        if number_dict == number_dict_2:
            return True  
        else:    
            return False
               
runtime = 0(n)


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count_right = 0 
        count_left = 0

        if root is None:
            return 0




        count_right = self.maxDepth(root.right) + 1 
        count_left = self.maxDepth(root.left ) + 1
        
        if count_right > count_left:
            return count_right
        else:
            return count_left



Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        
        
# if multiple of 3 output is "FIZZ"
# if multiplke of 5 output is "BUZZ"
# If multiple of 3 & 5 (15) output "fizzbuzz"

        result = []

        for num in range(1, n+1):

            if num % 15 == 0:
                result.append("FizzBuzz")
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result 


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
#         L = len(s) 
#         #take the string of letters in a list and reverse the order 
#         #start one from leeft and swap values 
         
#         for i in range(L/2):
#             s[i], s[L-i-1] = s[L-i-1], s[i]
      
            
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


    or s.reverse()