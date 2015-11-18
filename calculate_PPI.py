#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Calculate PPI

import math

def get_ppi():
    width = int(input("Please enter the monitors' WIDTH(in pixels): "))
    height = int(input("Please enter the monitors' HEIGHT(in pixels): "))
    diagonal = float(input("Please enter the monitors' DIAGONAL: "))
    ppi = math.sqrt((width*width+height*height))/diagonal
    print("Your PPI is: ", round(ppi,9))

get_ppi()

input("Press the enter key to exit...")
