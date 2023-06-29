# Get location data from IP Address

# Import library 
import ipdata
import sys

# Get API key and IP address from terminal
ipdata.api_key = sys.argv[1]
ip = sys.argv[2]

# Lookup IP address and store response object
data = ipdata.lookup(ip)

# Get values from data object
country = data.country_name
city = data.city
state = data.region
country_code = data.country_code
continent = data.continent_name

# Print values
print(f"Country: {country}")
print(f"City: {city}")
print(f"State: {state}")
print(f"Country Code: {country_code}")
print(f"Continent: {continent}")

