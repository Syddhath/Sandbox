"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



def getScore(score):
    if score < 0:
        return("Invalid score")
    elif score > 100:
        return("Invalid score")
    elif score > 90:
        return ("Excellent")
    elif score >= 50:
        return ("Passable")
    else:
        return ("Bad")
score = float(input("Enter score: "))

print(getScore(score))