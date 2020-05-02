import requests
import json
import os

def get_sign(sun_sign):
    request_url = f"https://zodiacal.herokuapp.com/{sun_sign}"
    #params = {"sun_sign": sun_sign)
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return print(parsed_response)

months = ["January", "February", "March", "April", "May", "June", "July", "August," "September", "October", "November", "December", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

while True:
    MONTH = input("Input your child's month of birth: ")
    if MONTH in months:
        break      
    else: 
        print ("Hey, are you sure that month is spelled correctly? Please try again!")

while True:
    DAY = int(input("Input your child's day of birth: "))
    if MONTH == "December" or MONTH == "december" or MONTH == "DECEMBER":
        if DAY <=0 or DAY >=32:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
            sun_sign = "Sagittarius" if (DAY < 22) else "Capricorn"
    elif MONTH == "January" or MONTH == "january" or MONTH == "JANUARY":
        if DAY <=0 or DAY >=32:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Capricorn" if (DAY < 20) else "Aquarius"
    elif MONTH == "February" or MONTH == "february" or MONTH == "FEBRUARY":
        if DAY <=0 or DAY >=30:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Aquarius" if (DAY < 19) else "Pisces"
    elif MONTH == "March" or MONTH == "march" or MONTH == "MARCH":
        if DAY <=0 or DAY >=32:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Pisces" if (DAY < 19) else "Aries"
    elif MONTH == "April" or MONTH == "april" or MONTH == "APRIL":
        if DAY <=0 or DAY >=31:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Aries" if (DAY < 20) else "Taurus"
    elif MONTH == "May" or MONTH == "may" or MONTH == "MAY":
        if DAY <=0 or DAY >=32:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Taurus" if (DAY < 21) else "Gemini"
    elif MONTH == "June" or MONTH == "june" or MONTH == "JUNE":
        if DAY <=0 or DAY >=31:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign == "Gemini" if (DAY < 21) else "Cancer"
    elif MONTH == "July" or MONTH == "july" or MONTH == "JULY":
        if DAY <=0 or DAY >=32:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Cancer" if (DAY < 23) else "Leo"
    elif MONTH == "August" or MONTH == "august" or MONTH == "AUGUST":
        if DAY <=0 or DAY >=31:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Leo" if (DAY < 23) else "Virgo"
    elif MONTH == "September" or MONTH == "september" or MONTH == "SEPTEMBER":
        if DAY <=0 or DAY >=31:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Virgo" if (DAY < 23) else "Libra"
    elif MONTH == "October" or MONTH == "october" or MONTH == "OCTOBER":
        if DAY <=0 or DAY >=32:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Libra" if (DAY < 23) else "Scorpio"
    elif MONTH == "November" or MONTH == "november" or MONTH == "NOVEMBER":
        if DAY <=0 or DAY >=31:
            print("Are you sure that date is correct? Please start again!")
            exit()
        else:
    	    sun_sign = "Scorpio" if (DAY < 22) else "Sagittarius"
    break

get_sign(sun_sign)

#request_url = f"https://zodiacal.herokuapp.com/{sun_sign}"
#response = requests.get(request_url)
#parsed_response = json.loads(response.text)
#print(parsed_response)