## Implementation of an IP address Geolocator


In this repository you can find a file named ```ip_address.py``` that implements the ```get_location(ip_address)``` function.
Such function queries the [ip-api](https://ip-api.com/docs/api:json) website to fetch data about the location of the given input ```ip_address```.
If you run the program, executing the main file with: ```python main.py``` it will give you an output similar to the following: 

```
$ python main.py
IP address 153.138.24.18 is from Chiyoda, Japan 
```

The project requires ```json``` and ```requests``` modules to run. The API offers several information beyond country and city (like region, zip, latutude and longitude and so on): you can explore different options to be implemented in your projects. Note that also a "status" flag is returned to indicate the success of the request (the endpoint is limited to 45 requests per minute from an IP address).

DESCRIPTION OF THE PROJECT

The first function created is a function that questions the API and gives back the city. 
Other information provided are the country, together with the latitude and the longitude. 
The function ip_address uses the libraries json, urllib to get from the API the information needed and load them.
The function main, instead, load the function from the other file (called ip_address) and return a string that gives the IP address with the location (composed by city and country).