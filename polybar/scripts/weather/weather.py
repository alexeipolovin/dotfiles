from pyowm import OWM
KEY = 'TOKEN'

def main():
    owm = OWM(KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Moscow')
    w = observation.weather
    weather = w.temperature('celsius')
    print("Moscow %.1f °C" % weather['temp'])

if __name__ == '__main__':
    main()

