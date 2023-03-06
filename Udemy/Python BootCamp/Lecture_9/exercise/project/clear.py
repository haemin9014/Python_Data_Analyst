import os;


#def clear():
    #for windows
    # if name == 'nt':
    #     _ = system('cls');
    # else:
    #     _ = system('clear');

def clear_cmd():
#for windows
    os.system('cls' if os.name =='nt' else 'clear');
