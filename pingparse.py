
import subprocess
print("*"*90)       

result = subprocess.check_output(["ping", "-c", "4", "tutorialspoint.com"])
print("*"*90)
print(result)
with open("/home/ankita/Documents/Ankita/pythonPractice/parseping.txt", "wr") as myfile:
    myfile.write(result)
    print("-"*90)

file = open('/home/ankita/Documents/Ankita/pythonPractice/parseping.txt','r') 
data = file.readlines()
l = 0
for line in data:
    word = line.split()
    if l < 4:
        if(word[0]=="64"):
            print word[7]+" "+word[8]
            l = l+1    




# import os
# # file = open('/home/ankita/Desktop/parseping.txt','w+') 

# result = os.system('ping {}'.format("google.com"))
# print("*"*900)
# print(result)
# print("*"*900)
# with open("/home/ankita/Desktop/parseping.txt", "w") as myfile:
#     myfile.write(result)

# file.close() 

