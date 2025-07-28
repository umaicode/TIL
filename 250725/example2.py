import requests

def get_seoul_weather():
    # API KEY
    API_KEY = 

    city_name = "Seoul, KR"
    # city_name = "Tokyo, JP"
    # city_name = "New York, US"

    url = 

    # 캘빈 온도 출력
    temperature = response["main"]["temp"]
    print(f"캘빈 온도 : {temperature}")

    response = requests.get(url).json()
    return response

