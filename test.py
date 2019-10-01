'''
# Python3 code to demonstrate working of 
# Converting String to binary 
# Using join() + ord() + format() 

# initializing string  
test_str = "GeeksforGeeks"
  
# printing original string  
print("The original string is : " + str(test_str)) 

# using join() + ord() + format() 
# Converting String to binary 
res = ''.join(format(ord(i), 'b') for i in test_str)
  

# printing result  
print("The string after binary conversion : " + res)
'''



a = "00001000"
b = "0101101"
#y = int(a, 2)^int(b, 2)
#print(bin(y)[2:].zfill(len(a)))

#[output: 00010100000000001110000101010001001]



print(bin(int(a, 2)^int(b, 2))[2:].zfill(len(a)))

print(type(bin(int(a, 2)^int(b, 2))[2:].zfill(len(a))))