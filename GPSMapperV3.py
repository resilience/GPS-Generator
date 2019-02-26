
import datetime
import csv
import time
import tkinter as tk
from tkinter import simpledialog
lat = 0
lng = 0
count = 0
root = tk.Tk()
root.geometry('240x850+200+100')
root.withdraw()
leftTop = simpledialog.askstring(title='Top Left Lat/Long?: ',prompt=root)
RightBottom = simpledialog.askstring(title='Bottom Right Lat/Long?: ',prompt=root)
mapName = simpledialog.askstring(title='What am I mapping?: ',prompt=root)

leftTopLat = float(leftTop.split(',', 1)[0])
leftTopLng = float(leftTop.split(',', 1)[1])


rightBottomLat = float(RightBottom.split(',', 1)[0])
rightBottomLng = float(RightBottom.split(',', 1)[1])

startlat = leftTopLat
print('Starting Latitude: ', startlat)
time.sleep(1)

startlng = leftTopLng
print('Starting Longitude: ', startlng)
time.sleep(1)
searchAmount = 150000
sqrt = searchAmount**(1/2.0)
print('sqrt used: ', sqrt)
time.sleep(1)
latDiff = (leftTopLat-rightBottomLat)/sqrt
print('Difference between latitudes: ', latDiff)
time.sleep(1)
lngDiff = (rightBottomLng-leftTopLng)/sqrt
print('Difference between longitudes: ', lngDiff)
time.sleep(1)

dt = str(datetime.datetime.today().strftime("-%B %d %Y "))
with open('' + dt + 'GPS ' + str(mapName) + ' '+ str(searchAmount)+'.csv', 'a', newline='', encoding='utf8') as g:

        while lat >= rightBottomLat:
            time.sleep(1)
            if count == 0:
                lat = startlat
                lng = startlng
                print(lat,",", lng)
                previouslat = startlat
                previouslng = startlng
                count = count + 1
                print(count)

            while lng <= rightBottomLng and count < searchAmount:
                lng = previouslng + lngDiff
                previouslng = lng
                #print(previouslng, "previous lng")


                if lng > rightBottomLng:
                    previouslng = startlng
                    lng = previouslng
                    print(previouslat, ": previous lat")
                    lat = previouslat - latDiff
                    previouslat = lat
                gps = str(lat) + "," + str(lng)
                thewriter = csv.writer(g, delimiter='|')

                thewriter.writerow([gps])
                count = count + 1



