import requests
import json
import os

months = ["January", "February", "March", "April", "May", "June", "July", "August," "September", "October", "November", "December", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

while True:
    MONTH = input("Input your child's month of birth: ")
    if MONTH in months:
        break      
    else: 
        print ("Hey, are you sure that month is spelled correctly? Please try again!")

while True:
    DAY = int(input("Input your child's day of birth: "))
    if MONTH == "December" or MONTH == "december":
        if DAY <=0 or DAY >=31:
            print("Are you sure that date is correct? Please try again!")
        else:
            sun_sign = "Sagittarius" if (DAY < 22) else "Capricorn"
    elif MONTH == "January" or MONTH == "january":
    	sun_sign = "Capricorn" if (DAY < 20) else "Aquarius"
    elif MONTH == "February" or MONTH == "february":
    	sun_sign = "Aquarius" if (DAY < 19) else "Pisces"
    elif MONTH == "March" or MONTH == "march":
    	sun_sign = "Pisces" if (DAY < 21) else "Aries"
    elif MONTH == "April" or MONTH == "april":
    	sun_sign = "Aries" if (DAY < 20) else "Taurus"
    elif MONTH == "May" or MONTH == "may":
    	sun_sign = "Taurus" if (DAY < 21) else "Gemini"
    elif MONTH == "June" or MONTH == "june":
    	sun_sign == "Gemini" if (DAY < 21) else "Cancer"
    elif MONTH == "July" or MONTH == "july":
    	sun_sign = "Cancer" if (DAY < 23) else "Leo"
    elif MONTH == "August" or MONTH == "august":
    	sun_sign = "Leo" if (DAY < 23) else "Virgo"
    elif MONTH == "September" or MONTH == "september":
    	sun_sign = "Virgo" if (DAY < 23) else "Libra"
    elif MONTH == "October" or MONTH == "october":
    	sun_sign = "Libra" if (DAY < 23) else "Scorpio"
    elif MONTH == "November" or MONTH == "november":
    	sun_sign = "Scorpio" if (DAY < 22) else "Sagittarius"
    break

print(sun_sign)

#print(f"Your Astrological sign is : " + astro_sign)

#request_url = "http://horoscope-api.herokuapp.com/horoscope/year/libra"

#request_url = request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}"

#response = requests.get(request_url)

#print(response)

#parsed_response = json.loads(response.text)

#print(parsed_response)