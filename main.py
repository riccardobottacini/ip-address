import ip_address
IP_address = "1.2.3.4"

if __name__ == "__main__":
    city, country = ip_address.get_location(IP_address)
    info = str("The IP ADDRESS "+ IP_address + " is located in "
                + city + " (" +  country +") ")
    print (info)
