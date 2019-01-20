import datetime
import csv
lat = 0
lng = 0
count = 0
previouslat = 0
previouslng = 0
startlat = -22.131002
startlng = 16.460633
dt = str(datetime.datetime.today().strftime("-%B %d %Y "))

with open('' + dt + 'GPS creator.csv', 'a', newline='', encoding='utf8') as g:
    while count < 149770:
       print( 'starting lat run')

       if lat >= -34.833159:
           print('starting lng run')
           while lng <= 32.888957:

              if count == 0:
                  previouslat = startlat
                  previouslng = startlng
                  lat = startlat
                  lng = startlng
                  count = count + 1
                  print(count)

              gps = str(lat) + "," + str(lng)



              idprefix = 'zaid'
              code = count
              id = idprefix + str(count)
              print(id)
              print (gps)
              count = count + 1
              print(count)
              lng = previouslng + 0.04245044961
              previouslng = lng
              print(lng)
              thewriter = csv.writer(g, delimiter='|')

              thewriter.writerow([id, lat, lng, gps])

           lng = startlng
           lat = previouslat - 0.03282211111
           previouslat = lat
           print(lat)
           print(lng)
           print(count)
       print(count)


