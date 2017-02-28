#!/usr/bin/env python3

def max_of_three(one,two,three):
    if(one > two and one >three):
        return one
    elif(two > one and two > three):
        return two 
    else:
        return three
