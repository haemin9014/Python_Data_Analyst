alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decode(text_input, shift_amount):
    decripy = "";
    checked = True;
    for check in range(0, len(text_input)):
        checked = False;
        for number in range(0, len(alphabet)):

            if text_input[check] == alphabet[number]:
                if number - shift_amount < 0:
                    decripy += alphabet[(26 + number) - shift_amount];
                    checked = True;
                else:
                    decripy += alphabet[number - shift_amount];
                    checked = True;
        
        if checked == False:
            decripy += text_input[check];
    print(f"{decripy}\n");