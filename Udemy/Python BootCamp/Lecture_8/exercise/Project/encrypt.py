alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text_input, shift_amount):
    encrypt = "";
    checked = True;
    for check in range(0, len(text_input)):
        checked = False;
        for number in range(0, len(alphabet)):

            if text_input[check] == alphabet[number]:
                if shift_amount + number > 25:
                    encrypt += alphabet[shift_amount + number - 26];
                    checked = True;
                else:
                    encrypt += alphabet[number + shift_amount];
                    checked = True;
        
        if checked == False:
            encrypt += text_input[check];
    print(f"{encrypt}\n");