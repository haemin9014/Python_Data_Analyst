def search_max(val):
    max = 0;
    winner = "";
    for i in val:
        saved = int(val[i]);
        if saved > max:
            max = saved;
            winner = i;
    print(f"The winnder is {winner} with a bid of {max}");   