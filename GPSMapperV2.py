
import datetime
import csv
import time
import tkinter as tk
from tkinter import simpledialog
lat = 0
lng = 0
count = 0


filename = "GPS ONLY ZIMBABWE FINAL 150000"
startlat = -15.6170402
startlng = 25.265084
dt = str(datetime.datetime.today().strftime("-%B %d %Y "))
with open('' + dt + filename + '.csv', 'a', newline='', encoding='utf8') as g:

        while lat >= -22.407937:
            if count == 0:
                lat = startlat
                lng = startlng
                print(lat,",", lng)
                previouslat = startlat
                previouslng = startlng
                count = count + 1
                print(count)

            while lng <= 33.058303 and count < 150000:
                lng = previouslng + 0.02012200493
                previouslng = lng
                #print(previouslng, "previous lng")
                print(count, " ", lat, ",", lng)

                if lng > 33.058303:
                    previouslng = startlng
                    lng = previouslng
                    print(previouslat, ": previous lat")
                    lat = previouslat - 0.01753402014
                    previouslat = lat
                gps = str(lat) + "," + str(lng)
                thewriter = csv.writer(g, delimiter='|')

                thewriter.writerow([gps])
                count = count + 1



