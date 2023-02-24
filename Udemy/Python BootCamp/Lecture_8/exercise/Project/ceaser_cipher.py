alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt = "a z a";
checked = False;
for check in range(0, len(text)):

    for number in range(0, len(alphabet)):

        if text[check] == alphabet[number]:
            if shift + number > 25:
                encrypt += alphabet[shift + number - 26];
                checked = True;
            else:
                encrypt += alphabet[number + shift];
                checked = True;
    
    if checked == True:
        checked = False;
        encrypt += text[check];

print(encrypt);