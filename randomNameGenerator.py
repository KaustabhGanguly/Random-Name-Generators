# -*- coding: utf-8 -*-
"""
Author : Kaustabh Ganguly

10 th Ian , 2018 

copyright : 2018

License : | OPEN SOURCE |
          Author : Kaustabh Ganguly
          linkedin.com/in/kaustabh
          Anyone can use it , modify it , distribute it 
          under the condition that it can't be used for
          money making of any kind and a person or organization 
          using it in a project of anykind should mention the 
          license clearly with Author's name.
          
"""

import random

v = ['a','e','i','o','u'] #all kinds of character sets
c = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','z']
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

MAX_A = 10    #change values for changing length of name an lists but anything >11 messes up the right_margin
MAX_N = 200

print ("-----------------------------------------------------------------------------\n\n\n                    WELCOME TO THE COOL NAMES GENERATOR !\n            (Make your terminal screen big for proper margin)\n                   \n\n\n----------------------------------------------------------------------------- \n\n")
inp = int(input("Enter the no. of alphabets : ( Max is 12 and input -1 for random ) : "))

if inp <= 1 and inp != -1 :

    raise ValueError(" To get unrealistic names go back to school ")
    
if inp == -1 :
    input_range = input("Give the range of no. of alphabets separated by comma \n\t\t(  e.g  lower_value,upper_value  )  : ")
    t = []
    bounds = input_range.split(",") 
    
num = int(input("Enter the no. of names you want : ( Max is 200 at a time )  :"))   

#all kinds of input scanning and bound checking 

def randomNameGenerator(inp): # main function with layers of fine tuning
    
    f=[]
    #random string
    for i in range (inp):
        random.shuffle(c)
        f.append(c[random.randint(0,len(c)-1)])
        
    random.shuffle(v)
    
    #replacing vowels in even places    
    for j in range(len(f)):
          if j%2 == 1 :
              f.pop(j)
              f.insert(j , v[random.randint(0,len(v) - 1)])
          else:
              continue
    
    n = random.randint(1,10) # generating a random number to randomly modify few things
    
    if n == 1 or n == 2 or f[-1] == 'q' :
        f.pop(-1)
        f.append(v[random.randint(0,len(v)-1)])    #randomly changing last letter to vowel     
    if inp > 5 and n == 5 or n == 9 :
        f.pop(-2)
        f.insert(-2,(v[random.randint(0,len(v)-1)]))   #randomly changing 2nd last element to vowel
    if n==3 or n==5 or n== 7:
        if inp%2 == 0 and inp > 2:
            f[-1] , f[-2] = f[-2] , f[-1]    #randomly swapping last two letters

    if n==1 or n==2 or n==4 or n==5 or n==7 or n==8 or n==9 :
        for i in range(inp-3):
          for j in range(4):
            if f[i] == v[j] and f[i+1] == f[j] and f[i+2] == f[j]:  #randomly changing consecutive 3 vowels
                f[i+1] = c[random.randint(0,len(c)-1)]
                
        for k in range(len(cons)):          #if last 2 letters are consonants , change them .
            if f[-1] == cons[k] and inp > 3 and f[-2] == cons[k] :
                if f[-3] == cons[k] :
                    f[-2] = v[random.randint(0,len(v)-1)]  #if 3rd last letter is consonant then 2nd last is vowel
                else :
                    f[-2] = c[random.randint(0,len(c)-1)]  #if 3rd last is vowel , then 2nd last is anthing

    for i in range(inp-3):
        if f[i] == f[i+1] and f[i+1] == f[i+2] :
            f[i+1] = cons[random.randint(0,len(cons)-1)] #changing consecutive 3 vowels as a result of random operations before
        else :
            pass
        
    if inp > 1 :    
        if f[0] == f[1] and f[0] != 'a' or f[0] != 'i' or f[0] != 'u' : #changing if 1st two are vowels except AA or II or UU
            f[0] = c[random.randint(0,len(c)-1)] 
    else :
        pass
        
    if inp == 3 :
        random.shuffle(v)
        f[1] = v[random.randint(0,len(v)-1)] #to remove 3 letter garbage names

    final = ' '.join(f)
    return str(final.upper()) 

def right_margin(out): # corrects the right margin in the right-side of output list
    
    l = len(out)
    t = []
    for i in range(15-l): #15 is random . if MAX_A >= 12 , then right_margin messes up , irrespective of the value inside range
       t.append(' ')
    out = list(out)
    out.extend(t)
    out = ''.join(out)

    return out

if inp <= MAX_A and num <= MAX_N :  # name limits , list limits
    
   if int(bounds[0]) <= 1 :

         raise ValueError(" To get unrealistic names go back to school ")

     
   print ("\nChoose from the "+str(num)+" names below :\n\n ")

   if inp == -1 :  # if user chooses random no. of letters
      for i in range(num):
            inp = int(random.randint(int(bounds[0]),int(bounds[1])))
            out = right_margin(randomNameGenerator(inp))
            print ("Here is your name no. "+ str(i+1) + " : \t~~~\t " + out+"\t\t~~~\n") #prints right_margin aligned list
   else :
       for i in range(num):
            out = randomNameGenerator(inp)
            print ("Here is your name no. "+ str(i+1) + " : \t~~~\t " + out+"\t\t~~~\n") #prints static list
else :
        raise  IOError("\n\nBE REALISTIC\n\n\n\nInput bound is : name must be greater than 1 alphabet and  max "+str(MAX_A)+" alphabets long and no. of name is max "+str(MAX_N)+" line long\n\nRerun the program\n")







          
          
            