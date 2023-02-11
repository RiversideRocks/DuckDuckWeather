import requests


def weather(lat, long, time):
    r = requests.get("https://duckduckgo.com/js/spice/forecast_daily/" + str(lat) + "/" + str(long) + "/" + str(time))
    return {"hourly": {"sum": r.json()["hourly"]["summary"], "image": "https://duckduckgo.com/assets/weather/icons/" + r.json()["hourly"]["icon"] + ".svg"}}

def weatherMultipleDays(lat, long, startTime, count, interval):
    bucket = []
    for x in range(count):
        bucket.append(weather(lat, long, startTime + (interval * x)))
    return bucket