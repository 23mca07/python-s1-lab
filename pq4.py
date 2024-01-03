text=input("enter a line of text:")
character_count=len(text)
print(f"the number of character in the input text is:{character_count}")
if character_count>=2:
   second_character=text[1]
   print(f"The second character is:{second_character}")
else:
    print("there is no second character in the input text:")
       
