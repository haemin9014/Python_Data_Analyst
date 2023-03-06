import art;
import clear;
import max_bit;

check_bidder = True
bids = {};

while check_bidder:
    print(art.logo);
    print("Welcome to the secret auction program.");
    key = input("What is your name?: ");
    value = input("What's your bid?: $");
    next = input("Are there any other bidders? Type 'yes' or 'no'.");
    bids[key] = value;
    if next == "no":
        check_bidder = False;
        max_bit.search_max(bids);
    elif next == "yes":
        clear.clear_cmd();



