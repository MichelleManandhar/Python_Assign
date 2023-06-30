# 3) Remove Duplicates from given Array 
# Example 1:
# Input: 1,2,3,2,5,4,1,4,5
# Output: 1,2,3,5,4
# Example 2:
# Input: 1,5,8,6,5,1,2,4,2,4,8
# Output: 1,5,8,6,2,4
# AWS EC2 to practice Linux commands

#METHOD I
num1 = [1,2,3,2,5,4,1,4,5]
num1 = list(set(num1))
print(num1)

#METHOD II
num2 = [1,5,8,6,5,1,2,4,2,4,8]
num2 = [*set(num2)]
print(num2)