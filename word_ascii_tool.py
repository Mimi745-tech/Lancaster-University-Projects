# Functions to clean text(remove punctuations and convert to lowercase)
# Parameter text- Text file content.

def clean_text(text):
    symbols=("!","@","#","$","%","^","&","*","(",")","-",
    "_","=","+","[","]","{","}",";",":","'",'"',",","<",".",">","/","?")
    no_symbols=text
    for symbol in symbols:
     no_symbols=no_symbols.replace(symbol, "")  # Removes symbols by replacing them with nothing.
    return no_symbols.lower()  # Returns all lower-case strings when the function is called .

# Function to count words
# Parameter text_string- Text contents in text file.

def count_words(text_string):
  words=text_string.split()  # Splits strings into an iterable list
  count={}
  for word in words:
    if word in count:
     count[word]+=1  # Counts each word and adds 1 if word already exists/is repeated.
    else:
     count[word]=1  # If a word only appears once it's value is 1.
  return count

# Function to show top words.
# Sorts the words according to the dictionary's values 
# in reverse meaning from largest to smallest.
# Parameter word_counts- Dictionary (from count_words(text_string)) containing word:word[count].
# Paramter top_n- Number of individual word:word[count] to be displayed in this case 1st 10.
 

def show_top_words(word_counts, top_n=10):
   sorted_counts=sorted(word_counts.items(),key=lambda x: x[1], reverse=True)
   top_list=dict(sorted_counts[:top_n])
   for word,count in top_list.items():
       print(f"{word}:{count}")
   print()  
   return top_list 

# Function to encode text to ASCII.(Text → ASCII)
# Parameter text- Text (string) to be encoded to ascii.

def encode_to_ascii(text):
  if text.strip() == "":
   raise ValueError("Empty input not allowed")
  ascii_list=[]
  for character in text:
    ascii_value=ord(character)
    ascii_list.append(str(ascii_value))  # Turns ascii into a string to use .join string format.
  return " ".join(ascii_list)  # Joins ascii code of each character with a space between.

# Function to decode ASCII to text.(ASCII → Text).
# Function ensures ascii values are numbers and are within range of 0-127.
# Parameter ascii_string- Ascii codes to be decoded into strings. 

def decode_from_ascii(ascii_string):
  if ascii_string.strip() == "":
   raise ValueError("Empty input not allowed")
  string_list=[]
  numbers=ascii_string.split()
  for number in numbers:
      if not number.isdigit(): # Ensures input is anumber since ascii values are only numbers.
        raise ValueError("Invalid ASCII code detected.Please try again")
      num=int(number)
      if num<0 or num>255:
       raise ValueError("Ascii value out of range. Value must be between 0-255")
      string=chr(num)  # Turns input to an integer which can then be decoded.
      string_list.append(str(string))
  return "".join(string_list)  # Joins individual chatacters into a word. 

    
# Part A-Word Frequency Analyser.

while True:
   try:
    print("Word Frequency and ASCII Tool\n 1 Analyze word frequency from file \n 2. Encode text to ASCII \n 3. Decode ASCII to text \n 4.Exit")
    option=int(input("Select an option: "))
    print(option)
    if option==1:
      while True:  
  
        # Make sure file is in same folder as python file.

        filename=input("Enter file path (or Filename if file in same folder as python file): ")
        import pathlib
        file_path=pathlib.Path(filename)  # Finds file path of input file.
       
        try:
             if filename.strip()=="":
              raise ValueError("Empty input not allowed")

             with open(file_path,"r") as file:
                content=file.read()
             print("Reading file......\n\n")
          # Removes punctuation and converts to lowercase.

             cleaned_text=clean_text(content)

          # Splits text and stores word counts in a dictionary.

             word_count=count_words(cleaned_text)

          # Calculations.

             total_words=sum(word_count.values())  # Sums up number of each word.
             unique_words=len(word_count)  # Counts individual dictinary items(dictionary items never have duplicates keys).

        
             print(f"Total number of words:{total_words} ")
             print(f"Total number of unique:{unique_words}")
             print(f"Top 10 words:")
             top_words=show_top_words(word_count)
          
          # Block to save results if an existing file is read.
             while True:

              save_result=str(input("Save results to wordcount.txt?(y/n):")).lower()
              if save_result == "y":
                  with open("wordcount.txt","a") as file:
                      file.write(f"\n{filename} cotents:\n \nTotal number of words:{total_words}\nTotal number of unique:{unique_words}\nTop 10 words:\n")
                      
                      # Loops through dictionary and writes individual items wordcount.txt file.

                      for word,count in top_words.items():
                        file.write(f"{word}:{count}\n")
                      print()
                  print("Results saved successfully!") 
                  break  # Breaks from loop to main menu.
              
              elif save_result == "n":
                break # Exits save result loop to main menu.
              else:
               print("Pick y/n")
               continue
             break # Exits (save result)loop to main menu.    
          
        except  FileNotFoundError:
            print("Error: File not found.Please check the name and try again.")   
        except Exception as error:
            print("Error :", error)    

        # Part B   — ASCII Encoder and Decoder.     

        # Text To ASCII.
         
    elif option==2:
      while True:  
        try:
          text=input("Enter text to encode: ")
          print(text)

          # Text to ascii converter.
      
          text_to_ascii= encode_to_ascii(text)
          print("ASCII codes: \n", text_to_ascii)

          # Loop to save results in encoded.txt file until valid text is enetered(y/n).

          while True:
            save_result=str(input("Save output in encode.txt? (y/n): ")).lower()

            if save_result=="y":
             with open("encoded.txt","a") as file:
              file.write(f"\nASCII codes of {text}:\n{text_to_ascii}\n")
             print("Encoded text saved successfully!") 
             break

            elif save_result == "n":
             exit_to_main=True 
             break  

            else:
             print("Pick y/n")
            continue
          break # Exits (save result)loop to main menu. 
        except Exception as error:
          print("Error: ",error)

      # ASCII To Text.
       
    elif option==3:
      while True:  
       try:
           asccii_sequence=input("Enter ASCII sequence to decode: ")
           print(asccii_sequence)
           

           # Ascii to text converter.

           ascii_to_text= decode_from_ascii(asccii_sequence)
           print(f"Decoded ascii to text: \n",ascii_to_text)   

           # Loop to save results in decoded.txt file until valid text is entered(y/n).

           while True:  

               save_results=str(input("Save output in decode.txt? (y/n): ")).lower()

               if save_results=="y":
                   with open("decoded.txt","a") as file:
                       file.write(f"\nDecoded ascii {asccii_sequence} to text:\n{ascii_to_text}\n")
                   print("Decoded text saved successfully!") 
                   break

               elif save_results == "n":
                  break   

               else:
                  print("Pick y/n")
                  continue
           break # Exits to main menu.
              
       except Exception as error:
          print("Error: ",error)
         
           
       
    elif option==4:
     print("Goodbye!!!")
     break  # Exits program.
    elif option<1 or option>4:
     print("Invalid input! Enter either 1, 2, 3 or 4.")
    continue # If user inputs values > 4 or values < 1 , user is asked to
             # enter values between 1-4.

   except ValueError:
    print("Invalid input! Enter either 1, 2, 3 or 4.")
   except Exception as error:
     print("Error:", error)

    