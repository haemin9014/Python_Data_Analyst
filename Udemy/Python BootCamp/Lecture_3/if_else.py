water_level = int(input("What is an water level?\n"));
if water_level >= 11:
    print("Water level is getting out of control");
elif water_level <= 10 and water_level >= 5:
    print("We are having enough water level")
else :
    print("We are getting out of water")