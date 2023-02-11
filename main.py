import requests


def weather(lat, long, time):
    r = requests.get("https://duckduckgo.com/js/spice/forecast_daily/" + str(lat) + "/" + str(long) + "/" + str(time))
    return {"hourly": {"sum": r.json()["hourly"]["summary"], "image": "https://duckduckgo.com/assets/weather/icons/" + r.json()["hourly"]["icon"] + ".svg"}}

def weatherMultipleDays(lat, long, startTime, count, interval):
    # count: how many weather times to fetch
    # interval: how much the weather times should be split apart
    # ie. weatherMultipleDays(0, 0, int(time.time()), 5, 3600)
    # Would get the hourly weather for five hours
    bucket = []
    for x in range(count):
        bucket.append(weather(lat, long, startTime + (interval * x)))
    return bucket