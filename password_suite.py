#Imports random module for password generation.

import msvcrt
import random 
lowercase=list(("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"))
uppercase=list(("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"))
digits=list(("0","1","2","3","4","5","6","7","8","9"))
symbols=list(("!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":","'",'"',",","<",".",">","/","?"))
possible_characters=[]

#Initializes password as empty string,so characters 
# can be added and displayed as a string later when printed.

generated_password=""
criteria=0
length=0

#while True statement is used because it runs loop as 
# long as conditions have been satisfied and are true since
#  the program is supposed to run until a condition is met.

while True:
   print("Simple Password Suite") #Displays title
   print ("1 Generate Password") 
   print ("2 Check Password Strength")
   print("3 Exit")

   #try-except loop prvent program from crashing 
   # when user enters an invalid input(any input except an intiger)
   
   try:
     
     #User can only input integers.

     option=int(input("Select an option:")) 
   except ValueError:
        print("Invalid input")

        #restarts loop if input is invalid.

        continue
   if option == 1:
     
     #Start of loop for password generation:length of password

     while True: 
            try:
              length=int(input("Enter password length(8-64):"))
              if length<8 or length>64:
                  print("Invalid length") 
                  continue 
            except ValueError:
              print("Invalid input")  
              continue

            #proceeds to the next part of the code if input is valid.

            break 
     #Character selction loop

     while True:
         
         #Resets possible characters in an empty list,
         #  so chosen characters will be added to this new list.

         possible_characters=[] 
         criteria=0
         #Loop for uppercase letters

         while True: 
              upper=str(input("Include Uppercase Letters?(y/n):"))
               #.lower() method converts any 
               # uppercase N or Y so that program can still read Y or N inputs.

              if upper.lower() == "y":
                  
                  #if user chooses y, adds uppercase to possible_characters list. 
                  # += adds more than 1 item instead of append(), so it's prefered in this case.

                  possible_characters+=uppercase 

                  #Increases criteria by 1 anytime y is chosen

                  criteria+=1 
                  break
              elif upper.lower() == "n":
                 break
              else:
                 print("Invalid input")
              continue
         
         #Start of loop for lowercase letters
         
         while True:
          lower=str(input("Include lowercase letters?(y/n):"))
          if lower.lower() == "y":
              possible_characters+=lowercase
              criteria+=1
              break
          elif lower.lower() == "n":
              break
          else:
              print("Invalid input")
              continue
          
          #Start of loop for symbols

         while True:
          symbol=str(input("Include symbols letters?(y/n):"))
          if symbol.lower() == "y":
              possible_characters+=symbols
              criteria+=1
              break
          elif symbol.lower() == "n":
              break
          else:
              print("Invalid input")
              continue
          
          #Loop for digits

         while True:
           digit=str(input("Include digits?(y/n):"))
           if digit.lower() =="y":
              possible_characters+=digits
              criteria+=1
              break
           elif digit.lower()=="n":
              break
           else:
                print("Invalid input")
                continue
         if  criteria < 2:
            print("You must select 2 or more character types")   

            #Restarts loop from choosing uppercase letters when criteria is less than 2  

            continue  
         else: 

            #Generates password based on user's choices and the length will be lenghth 
            # chosen by user above

            generated_password="".join(random.choices(possible_characters, k=length))
            print("Generated Password:", generated_password)
            break
     while True:
            again=str(input("Generate another with the same settings?(y/n):"))
            if again.lower() == "y":

                #Generate password based on user's choices and the length will be lenghth
                #  chosen by user above

                generated_password="".join(random.choices(possible_characters, k=length))
                print("Generated Password:", generated_password)
            elif again.lower() == "n":
             break
            else:
                print("Invalid input")

                #Restarts loop

                continue               
   elif option == 2:   
          while True: 
            password1=str(input("Do you want to evaluate strength of password generated from option 1?(y/n):"))
            if password1.lower() == "y":
               if generated_password=="":
                    print("No previously generated password found, type 'n' to proceed.")
                    continue

               #Evaluates generated password from option 1 instead of "y/n" input 
               # also .strip() removes any space at the beginning or end of password
               # that will affect password length.

               password1=generated_password.strip()
               length=len(generated_password)
               print("Generated Password:", generated_password)
               #1.Checking Lenghth of Password
              
               strength=0
               if length<=8:
                  strength=0
               elif length>=40:
                  strength=20
               else:
                  
                  #linear formula to calculate strenghth of password based on length 

                  strength=(length-8)*20/(40-8) 

              #2.Checking for Variety of Characters

               variety=0 

              # For statement iterates over the sequence of thecharacters in the password,
              # therefore checking it can check if any character is present in the sequence and give a score.

               for i in password1: 
                  if i in uppercase:
                      variety+=5
                      break
               for i in password1:
                  if i in lowercase:
                       variety+=5
                       break
               for i in password1:
                  if i in digits:
                        variety+=5
                        break
               for i in password1:
                  if i in symbols:
                        variety+=5
                        break
                  
              #3.Checking for Digits Presence

               digit_count = 0       
               for i in password1:
                  if i in digits:
                      digit_count += 1
               if digit_count == 1:
                      Digits=10
               elif digit_count > 1:
                      Digits = 20
               else:
                   Digits = 0  

              #4.Checking for Symbols Presence

               symbol_score=0
               Symbols=0    
               for i in password1:
                  if i in symbols:
                      symbol_score += 1
               if symbol_score==1:
                      Symbols=10
               elif symbol_score > 1:
                      Symbols = 20  
               else :
                      Symbols = 0       

              #5.Checking Uniqueness of Characters
                
              #Sets have no repeated characters.
              #  If length of password is equal to length of set password,it means all characters are unique.

               if len(password1)== len(set(password1)): 
                      unique_score=20
               else:
                      unique_score=(len(set(password1)))*20/len(password1) 

              #Final Label

               Score=strength+variety+Digits+Symbols+unique_score   
               if Score<=24:
                    label="The password is Very Weak"
               elif Score>=25 and Score<=44:
                    label="The password is Weak"
               elif Score>=45 and Score<=64:
                    label="The password is Moderate"
               elif Score>=65 and Score<=84:
                    label="The password is Strong"
               elif Score>=85 and Score<=100:
                    label="The password is Very Strong"    
               print("The Length score of the password is:", float(strength))
               print("The Variety score of the password is:", variety)
               print("The Digit score of the passowrd is:", Digits)
               print("The Symbols score of the password is:", Symbols)
               print("The Uniqueness score of the passoword is:", float(unique_score))
               print("The Total Score of the password is:", int(Score))
               print("Label:", label) 
               break
            
            #Evaluates user's input instead of generated password.

            elif password1.lower() == "n":
             password=str(input("Enter password to evaluate:"))
             length=len(password) 
             password1=password.strip()
              #1.Checking Lenghth of Password
              
             strength=0
             if length<=8:
                  strength=0
             elif length>=40:
                  strength=20
             else:
                  
                  #linear formula to calculate strenghth of password based on length 

                  strength=(length-8)*20/(40-8) 

              #2.Checking for Variety of Characters

             variety=0 

              # For statement iterates over the sequence of thecharacters in the password,
              # therefore checking it can check if any character is present in the sequence and give a score.

             for i in password: 
                  if i in uppercase:
                      variety+=5
                      break
             for i in password:
                  if i in lowercase:
                       variety+=5
                       break
             for i in password:
                  if i in digits:
                        variety+=5
                        break
             for i in password:
                  if i in symbols:
                        variety+=5
                        break
                  
              #3.Checking for Digits Presence

             digit_count=0       
             for i in password1:
                  if i in digits:
                      digit_count+=1
             if digit_count==1:
                      Digits=10
             elif digit_count>1:
                      Digits=20
             else:
                   Digits=0  

              #4.Checking for Symbols Presence

             symbol_score=0
             Symbols=0    
             for i in password:
                  if i in symbols:
                      symbol_score+=1
             if symbol_score==1:
                      Symbols=10
             elif symbol_score>1:
                      Symbols=20  
             else :
                      Symbols=0       

              #5.Checking Uniqueness of Characters
                
              #Sets have no repeated characters.
              #  If length of password is equal to length of set password,it means all characters are unique.

             if len(password)== len(set(password)): 
                      unique_score=20
             else:
                      unique_score=(len(set(password)))*20/len(password) 

              #Final Label

             Score=strength+variety+Digits+Symbols+unique_score   
             if Score<=24:
                    label="The password is Very Weak"
             elif Score>=25 and Score<=44:
                    label="The password is Weak"
             elif Score>=45 and Score<=64:
                    label="The password is Moderate"
             elif Score>=65 and Score<=84:
                    label="The password is Strong"
             elif Score>=85 and Score<=100:
                    label="The password is Very Strong"    
             print("The Length score of the password is:", float(strength))
             print("The Variety score of the password is:", variety)
             print("The Digit score of the password is:", Digits)
             print("The Symbols score of the password is:", Symbols)
             print("The Uniqueness score of the password is:", float(unique_score))
             print("The Total Score of the password is:", int(Score))
             print("Label:", label)
             break
            else:
                print("Invalid input")
                continue
              
              #Windows only, imports msvcrt module to wait till a key is pressed,
              # then exists to main menu.

          import msvcrt 
          print("Press any key to exit")
          msvcrt.getch() 
          continue
   elif option == 3:
     print("Exit")
     break      
   else:
    print("Invalid input")
    continue     
              