#
# Aaron Deaver

# Air Quality Classifier
#

# Get the AQI.
aqi = int(input('Enter the Air Quality Index (AQI): '))

# Determine the classification of the AQI
# and display the result.
if aqi <= 50:
    print('Good')
elif aqi >= 51 and aqi <= 100:
    print('Moderate')
elif aqi >= 101 and aqi <= 150:
    print('Unhealthy for Sensitive Groups')
elif aqi >= 151 and aqi <= 200:
    print('Unhealthy')
elif aqi >= 201 and aqi <= 300:
    print('Very Unhealthy')
else:
    if aqi >= 301:
     print('Hazardous')
