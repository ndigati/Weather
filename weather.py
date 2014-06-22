import json
from urllib import response, request


def main():
    zip_code = input("Enter zip code: ")  # ask user for zip code of where they want weather

    # add given zip code to api call
    url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=' + \
          str(zip_code) + '&format=json&key=a0bc630fb843c8af5fcf433c06c7aa3f4048601d'

    # open url
    weather_response = request.urlopen(url)
    str_response = weather_response.readall().decode('utf-8')       # work around for python 3 (found on stackoverflow)
    weather_json = json.loads(str_response)

    weather = weather_json['data']['current_condition'][0]
    print('\n')

    # print out relevant weather conditions
    print('Weather Conditions: ' + weather['weatherDesc'][0]['value'] + '\n' +
          'Temperature (C): ' + weather['temp_C'] + '\n' +
          'Temperature (F): ' + weather['temp_F'] + '\n' +
          'Humidity: ' + weather['humidity'] + '%\n' +
          'Wind Speed (MpH): ' + weather['windspeedMiles'] + ' ' + weather['winddir16Point'])


if __name__ == '__main__':
    main()

