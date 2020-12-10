import ip_address
import csv_manager
IP_address = "1.2.3.4"
csv_path = "data/ip_data.csv"

if __name__ == "__main__":
    city, country = ip_address.get_location(IP_address)
    info = str("The IP ADDRESS "+ IP_address + " is located in "
                + city + " (" +  country +") ")
    print (info)
	csv_manager.write_data(csv_path,IP_address,city,country)