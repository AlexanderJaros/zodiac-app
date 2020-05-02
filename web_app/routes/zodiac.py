import requests

def get_sign(sun_sign):
    request_url = f"https://zodiacal.herokuapp.com/{sun_sign}"
    #params = {"sun_sign": sun_sign)
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return print(parsed_response)