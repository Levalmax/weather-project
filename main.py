
import requests
openMeteo = "https://api.open-meteo.com/v1/forecast?latitude=55.7558&longitude=37.6176&daily=temperature_2m_max,temperature_2m_min,windspeed_10m_max&current_weather=true&timezone=Europe%2FMoscow"
res = requests.get(openMeteo) # получаем нужные данные с open-meteo.com

#Взвращается json вида:
#{
#'latitude': 52.52,
#'longitude': 13.419998,
#'generationtime_ms': 0.6150007247924805,
#'utc_offset_seconds': 10800,
#'timezone': 'Europe/Moscow',
#'timezone_abbreviation': 'MSK',
#'elevation': 38.0, 
#'daily_units': {
#                   'time': 'iso8601',
#                   'temperature_2m_max': '°C',
#                   'temperature_2m_min': '°C',
#                   'windspeed_10m_max': 'km/h'
#               }, 
#'daily': {
#           'time': ['2022-11-01', '2022-11-02', '2022-11-03', '2022-11-04', '2022-11-05','2022-11-06', '2022-11-07'],
#           'temperature_2m_max': [16.2, 14.1, 13.5, 14.0, 10.8,11.1, 13.4],
#		    'temperature_2m_min': [10.8, 6.9, 4.8, 7.5, 5.4, 5.5, 6.5],'windspeed_10m_max':[11.4, 20.4, 11.5, 11.3, 19.1, 14.2, 14.3]
#         }
#}
    
    


    
def weatherShow():   
    json = res.json()                            #создаем переменную с данными в формате Json 
    daily = json['daily']                        #обращаемся к ежедневным данным
    windspeed = daily['windspeed_10m_max']       #скорость ветра
    dateWeather = daily['time']                  #дата погоды
    tempMax = daily['temperature_2m_max']        #максимальная температура
    tempMin = daily['temperature_2m_min']        #минимальная температура
    for i in range(7):                          #выводим данные погоды за 7 дней 
        print("Дата : ", dateWeather[i])
        print("- максимальная скорость ветра: ", windspeed[i], "Км/ч")
        print("- максимальная температурв в течении суток: ", tempMax[i], "°C")
        print("- минимальная температурв в течении суток: ", tempMin[i], "°C")

if res:
    weatherShow()
else:
    print("Ошибка сервера")

