#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    #step1 remove all special1 characters
    word1 = re.sub(f"[{special1}]", "", para);
    
    #step2 reverse, print up to 70
    rword2 = word1[:70][::-1];
    print(rword2);
    
    #step3 replace and join special2
    removeSpace = rword2.replace(" ", "");
    removeSpace = special2.join(removeSpace);
    print(removeSpace);
    
    #step4 check does para has list1
    if all(element in para for element in list1):
        print(f"Every string in {list1} were present");
    else:
        print(f"Every string in {list1} were not present");
        
    #step5 plist and print upto 20
    splitWord = word1.split();
    print(splitWord[:20]);
    
    #step6
    unique = [];
    result = [];
    #check splitWord list is in the unique list, if not save it
    for element in splitWord:
        if element not in unique:
            unique.append(element);
    
    #count how many time splitWord have element in their list. if it is <3 save in result list.
    for element in unique:
        if splitWord.count(element) < 3:
            result.append(element);
    #print last 20.
    print(result[-20:]);
    
    #step7
    print(word1.rindex(strfind));