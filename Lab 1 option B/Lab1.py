'''
Author: Alexis Navarro
CS2302 -Lab 1 Option B
MW 1:30-2:50 PM
Professor: Diego Aguirre
Purpose: make a code that uses recursion to find the password of 99 users by using brute force
         and learning recursion for myself.
'''
import hashlib


'''
One of my work in progress methods to create the password, but wouldn't concatnate my salt to the empty string. WOULD LEAVE X EMPTY ALWAYS.
def random_password(x,size,salt_val, hash_val):
        #print(x+salt_val)
        #print(size)
        #print('length',len(x))
        a=int(x)
        
        if a==9:
            return a
        
            #x+=salt_val
            #print(A)
            if check_password(x,hash_val) == True:
                return x
              
        for i in range(10):
            #print(x)
            a+=i
            #print(int(x)+i)
            print(a)
            random_password(a,size,salt_val,hash_val)
            #random_password(x+str(i),size,salt_val,hash_val)
               
'''     


#Given Method to hash the passwords
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig



#working method to make the new password
def random_password(current_password, str_size, number_limit):
    
        
     if(str_size == 0): # once the values of iterations is 0 then a password is made and checks if that password is correct
        #print (current)
        check_password(current_password) #checks if the password is correct 
        
     elif(str_size > 0): 
        for i in range(number_limit):
            random_password(current_password+str(i),str_size-1,number_limit)# here I concatenate the empty string to the value i has in the for loop, I decrease the size of my string minus 1 after each recursive call 
                                                                    #to be able to get to my base case and because it means that a NEW password has been created.
            
            
   
    

#checks the password and followed the instructions that were taught in class on how to do it.
def check_password(gen_password):  
    for i in range(len(file_info)):
        x=hash_with_sha256(gen_password + file_info[i][1]) #try to concatenate like this however nothing happened
        
        #if (hash_with_sha256(gen_password + file_info[i][1])== file_info[i][2]): # if you want the results clean and only with the digits
        if (x == file_info[i][2]): # comment this if you want the cleaner results.
            
            #complete_password.append(file_info[i][0] + ' real password: ' + gen_password +" ")  
            
            
            complete_password.append(file_info[i][0] + ' real password: ' + x+" ") # prints the complete extended password with hash and salt values
           
            #print("correct password-> ",complete_password)  # prints the correct passwords
            
            del file_info[i]  # used del instead of remove cause it would output an error
            return 
        
     



#------------------------------MAIN---------------------------------------------------------------------------------------------------------------

def main():
   # hex_dig = hash_with_sha256('This is how you hash a string with sha256')
   # print(hex_dig)
    #with open('password_file.txt') as password_file:
        #for line in password_file:
        
        
#*************************THIS IS THE WORKING FUNCTION TO MAKE THE PASSWORD**********************************************************************#       
        #create variables to hold my data just like how it was taught in class
        global file_info
        global complete_password
        file_info=[] # will be used to hold to info in the text file
        complete_password=[]
        
        #while loop makes the password creation faster than using a for loop
        file = open('password_file.txt', 'r')    # Reading from file
        line = file.readline()
        while line != '':
            line = line.strip() # REMOVES THE WHITE SPACE FROM THE TEXT FILE
            parts=line.split(',')
            file_info.append(parts)
            line = file.readline()
            #print(file_info)
            
            
        #nested for loop to make the random password and then checking with each use faster 
        for i in range(3, 7):   
            random_password('', i, 10) #pass an empty string, the index, then 10 is for the digits that will be used 0-9
        
            for j in range(len(complete_password)): # prints the working/true generated passwords might be faster depending how its set up.
                print("correct password-> ",complete_password[j]) #different way to view how it prints
            
          
 #************************************************************************************************************************************************#       
           
            
        #gen_pass=random_password('00',3,parts[1],parts[2])#original and first attempt to make my program make a random password 
        # print("new password: ",gen_pass)
            
main()