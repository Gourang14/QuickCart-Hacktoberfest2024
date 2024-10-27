import requests
from selenium import webdriver
import folium
import datetime
import time

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
        # return lat, long
    except:
        # Displaying ther error message
        print(&quot;Internet Not avialable&quot;)
        # closing the program
        exit()
        return False

# of the map
def gps_locator():

    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print(&quot;You Are in {},{}&quot;.format(city, state))
        print(&quot;Your latitude = {} and longitude = {}&quot;.format(lat, long))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        fileName = &quot;C:/screengfg/Location&quot; + \
            str(datetime.date.today()) + &quot;.html&quot;

        obj.save(fileName)

        return fileName

    except:
        return False


# Main method
if __name__ == &quot;__main__&quot;:

    print(&quot;---------------GPS Using Python---------------\n&quot;)

    # function Calling
    page = gps_locator()
    print(&quot;\nOpening File.............&quot;)
    dr = webdriver.Chrome()
    dr.get(page)
    time.sleep(4)
    dr.quit()
    print(&quot;\nBrowser Closed..............&quot;)
