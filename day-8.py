# def greet(name):
#   print("Salut! "+ name)
#   print("Konichiwa! " + name)
#   print("Hello! " + name)

# name = input("What is your name? ")

# greet(name)

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"You live in {location}?")

# greet_with(location="Bucuresti", name="Alex")

#Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#   print(f"You'll need  {math.ceil((height * width) / cover)} cans of paint.")


# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇
# def prime_checker(number):
#     is_Prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_Prime = False
  
#     if is_Prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
    

#  #

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
#     new_text = ""
#     for i in range(len(text)):
#         char = text[i]
#         index_of_char = alphabet.index(char) + shift
#         if index_of_char >= len(alphabet):
#             out_index = index_of_char - len(alphabet)
#             new_text += alphabet[out_index]
#         else:   
#             new_text += alphabet[index_of_char]
#     print(f"The encoded message is: {new_text}")

# def decrypt(text, shift):
#     new_text = ""
#     for i in range(len(text)):
#         char = text[i]
#         index_of_char = alphabet.index(char) - shift
#         if index_of_char >= len(alphabet):
#             out_index = index_of_char - len(alphabet)
#             new_text -= alphabet[out_index]
#         else:   
#             new_text += alphabet[index_of_char]
#     print(f"The decoded message is: {new_text}")

# if direction == "encode":
#     encrypt(text=text, shift=shift)
# elif direction == "decode":
#     decrypt(text=text, shift=shift)
# else:
#     print("Please select 'encode' to encrypt, type 'decode' to decrypt")

# def caesar(direction, text, shift):
#     new_text = ""
#     for i in range(len(text)):
#          char = text[i]
#          if direction == "encode":
#             index_of_char = alphabet.index(char) + shift
#             if index_of_char >= len(alphabet):
#                 out_index = index_of_char - len(alphabet)
#                 new_text += alphabet[out_index]
#             else:   
#                 new_text += alphabet[index_of_char]
#          elif direction == "decode":
#             index_of_char = alphabet.index(char) - shift
#             if index_of_char >= len(alphabet):
#                 out_index = index_of_char - len(alphabet)
#                 new_text -= alphabet[out_index]
#             else:   
#                 new_text += alphabet[index_of_char]
#          else:
#             print("Please select 'encode' to encrypt, type 'decode' to decrypt")

#     print(f"The {direction}d message is: {new_text}")
    


# caesar(direction,text,shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position >= len(alphabet):
                out_index = new_position - len(alphabet)
                end_text += alphabet[out_index]
      else:
         end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

from caesar_cipher_art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
should_continue = True
while should_continue:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  play_again = input('\nType "yes" if you want to run again or "no" to stop program.\n').lower()
  if play_again =="yes":
    continue
  elif play_again == "no":
    should_continue = False
  else:
    print("Please type only yes or no")
    continue

# def brute_force_caesar_cipher(ciphertext):
#     decrypted_texts = []
#     for shift in range(26):  # There are 26 possible shifts
#         plaintext = ""
#         for char in ciphertext:
#             if char.isalpha():
#                 is_upper = char.isupper()
#                 char = char.lower()
#                 decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
#                 if is_upper:
#                     decrypted_char = decrypted_char.upper()
#                 plaintext += decrypted_char
#             else:
#                 plaintext += char
#         decrypted_texts.append(plaintext)
#     return decrypted_texts

# text ="owhqp znwcehkn, wyaopw aopa lnkcnwiqh iaq za ynelpwna"
# print(brute_force_caesar_cipher(text))