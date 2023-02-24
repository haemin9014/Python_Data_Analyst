test_h = int(input("Height of wall: "));
test_w = int(input("Width of wall: "));
coverage = 5;

def paint_calc(height, width, cover):
    numb_of_can = round((height * width) / cover);
    print(f"You'll need {numb_of_can} cans of paints.")

paint_calc(height = test_h, width =test_w, cover = coverage);

