import encrypt
import decrypt
exit = False;

while exit == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: type 'exit' to exit: \n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "encode":
            encrypt.encode(text, shift);
        elif direction == "decode":
            decrypt.decode(text, shift);
    elif direction == "exit":
        print("ending the program....\n")
        exit = True;
    else:
        print("you had type in wrong, please chose the correct option.")



