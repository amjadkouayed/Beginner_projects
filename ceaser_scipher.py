alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(text1, shift1):
#     encrypted = ""
#     for i in text1:
#         if i in alphabet:
#             index = alphabet.index(i)
#             newindex= (index + shift1)
#             encrypted+= alphabet[newindex]
#         else:
#             encrypted += i
#     print(f"your encrpyted word is {encrypted}")

# def decrypt(text1, shift2):
#     decrypted = ""
#     for i in text1:
#         if i in alphabet:
#             index = alphabet.index(i)
#             newindex= (index - shift2)
#             decrypted+= alphabet[newindex]
#         else:
#             encrypted += i
#     print(f"your decrpyted word is {decrypted}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)


def encrypt_dycript(text1, shift2, direction3):
    if direction3 == "encode":
        encrypted = ""
        for i in text1:
            if i in alphabet:
                index = alphabet.index(i)
                newindex= (index + shift2)
                encrypted+= alphabet[newindex]
            else:
                encrypted += i
        print(f"your encrpyted word is {encrypted}")

    elif direction3 == "decode":
        decrypted = ""
        for i in text1:
            if i in alphabet:
                index = alphabet.index(i)
                newindex= (index - shift2)
                decrypted+= alphabet[newindex]
            else:
                decrypted += i
        print(f"your decrpyted word is {decrypted}")

encrypt_dycript(text, shift, direction)









#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 