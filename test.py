# class Solution:
#     def singleNumber(self, nums: [int]) -> int:
        

# for i in range(0,9 +1):
#     print(i)

# Using readline() 
file1 = open('text.txt', 'r') 
count = 0
  
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("case Token::{:10}: out << {:13} break;".format(line.strip()[:-1], '"'+line.strip()[:-1]+'";'))
  
file1.close() 