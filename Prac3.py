import requests
from bs4 import BeautifulSoup
import html.parser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab
import datetime
import json
import csv

FILENAME = "C:\\GitHub\\SiAOD\\Weather.csv"
NEWFILENAME = "C:\\GitHub\\SiAOD\\NewWeather.csv"
def parcerData(start_date, end_date, station, city):
    url = 'https://api.meteostat.net/v1/history/daily?station=' + str(station) +'&start=' + str(start_date) + '&end=' + str(end_date) + '&key=HOmpes1N'

    r = requests.get(url)
    dictdata = json.loads(r.text)

    with open(FILENAME, 'w', newline='') as file:
        columns = ("date","temperature","temperature_min","temperature_max","precipitation","snowfall","snowdepth","winddirection","windspeed","peakgust","sunshine","pressure")
        writer = csv.DictWriter(file, columns)
        writer.writeheader()

        writer.writerows(dictdata["data"])

    with open(FILENAME, 'r') as f:
        incl_col = [0, 1]
        new_csv = []
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            col = list(row[i] for i in incl_col)
            new_csv.append(col)

    with open(NEWFILENAME, 'w') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(new_csv)
            
    dataset = pd.read_csv(NEWFILENAME, sep=',', index_col=['date'], parse_dates=['date'])

    plt.plot(dataset,'b', label = 'main')
    plt.title('Weather of ' + str(city))
    plt.ylabel('Temperature')
    plt.xlabel('Dates')
    plt.show()

# main
print("Погода в Минске")

        parcerData('2010-01-01', '2020-03-03', '24944', 'Minsk')
    elif(answer2 == '2'):
        print("Введите начальную дату(гггг-мм-дд)")
        req = input()

        print("Введите конечную дату(гггг-мм-дд)")
        req2 = input()

  parcerData(req, req2, '24944', 'Minsk')
