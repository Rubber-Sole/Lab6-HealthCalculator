#!/usr/bin/env python3

# Lab 6 - Youngdahl-HealthCalculator.py
# A calculator that will calculate the user's BMI as well as their heart rate at varying levels of physical exertion.
# Dylan Youngdahl CSCI-1103-W03 (WORKS REFERENCED BELOW)
# Date - 4 August, 2022


"""
- calculating 2 values, BMI & Max Heart Rate values at specific exertion intensity using Karavoen formula
- protect against invalid numeric data entry using while loops

define 2 functions:
1. calc and return BMI value based on metrics passed into its function
2. calc and return Karavoen max heart rate given the intensity, resting heart rate, and age passed into funct
"""

import numpy as np

print('\nPlease enter the following values for the user . . .\n')

ht, wt, age, hrate = 0, 0, 0, 0
metrics = [ht, wt, age, hrate]

while metrics[0 or 1 or 2 or 3] == 0:  # still need to figure out how to make this less clunky...
    try:
        ht = int(input('Height, in inches: '))
    except ValueError:
        print('Please only enter a whole number!')
        continue
    try:
        wt = int(input('Weight, in pounds: '))
    except ValueError:
        print('Please only enter a whole number!')
        continue
    try:
        age = int(input('Your age: '))
    except ValueError:
        print('Please only enter a whole number!')
        continue
    try:
        hrate = int(input('Your resting heart rate: '))
    except ValueError:
        print('Please only enter a whole number!')
        continue
    else:
        break

metrics = [ht, wt, age, hrate]


def bmi():  # final_bmi = weight(kg) / height(m^2)
    meters = ht * 0.0254  # convert inches to meters
    meters_sq = meters ** 2  # square our value in compliance with BMI formula
    kg = wt * 0.45359237  # convert pounds to kilograms
    bmi.final_bmi = kg / meters_sq
    bmi.final_bmi = round(bmi.final_bmi, 2)

    bmi.finalmetrics = [bmi.final_bmi]

    if bmi.final_bmi < 18.5:
        bmi.underweight = 'Underweight', True
        list.append(bmi.finalmetrics, bmi.underweight[1])
        print('\nResults...\nYour BMI is:', bmi.final_bmi, '--', bmi.underweight[0])
    elif 18.5 <= bmi.final_bmi <= 24.9:
        bmi.normal = 'Normal weight', True
        list.append(bmi.finalmetrics, bmi.normal[1])
        print('\nResults...\nYour BMI is:', bmi.final_bmi, '--', bmi.normal[0])
    elif 25 <= bmi.final_bmi <= 29.9:
        bmi.overweight = 'Overweight', True
        list.append(bmi.finalmetrics, bmi.overweight[1])
        print('\nResults...\nYour BMI is:', bmi.final_bmi, '--', bmi.overweight[0])
    elif bmi.final_bmi > 30:
        bmi.obese = 'Obese', True
        list.append(bmi.finalmetrics, bmi.obese[1])
        print('\nResults...\nYour BMI is:', bmi.final_bmi, '--', bmi.obese[0])
    else:
        print('\nAn unknown error has occurred, try running again.')


bmi()


"""
mhr = 220 - age         (mhr = max heart rate)
hrr = mhr - hrate       (hrr = heart rate reserve)
mtz = hrr * tr%         (mtz = max target zone // tr% = intensity percent)
ttz = mtz + hrate       (ttz = target training zone)
"""


def karvonen():
    mhr = 220 - metrics[2]  # max heart rate & age
    hrr = 0  # heart rate reserve
    hrr = mhr - metrics[3]  # hrate
    tr = .50  # target rate
    print('\nExercise intensity heart rates:\n', 'Intensity level:\tMax heart rate', )

    for tr in np.arange(.50, 1, .05):  # () Utilize numpy to increment the TR by 5% until all values are found
        mtz = hrr * tr  # max target zone
        ttz = 0  # target training zone
        ttz = mtz + metrics[3]  # hrate
        print(round(tr, 2), '%\t\t---\t\t', int(ttz), 'BPM')


karvonen()


"""
() https://www.w3schools.com/python/python_try_except.asp
() https://www.w3schools.com/python/python_variables_global.asp
() https://stackoverflow.com/questions/477486/how-do-i-use-a-decimal-step-value-for-range
"""
