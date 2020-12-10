import ip_address
import csv_manager
import databasemanager
import argparse

IP_address = "1.2.3.4"
csv_path = "data/ip_data.csv"
database_path = 'data/database.db'


databasemanager.db_creation(database_path)

def parse_arguments():
    parser=argparse.ArgumentParser(
            description="IP ADDRESS prject")
    parser.add_argument ("IP_address", type=str,
                         help= "Insert an IP Address",
                         default=None
                         
    args = parser.parse_args()
    
    return args

if name == "main":
    args = parse_arguments()
    if databasemanager.check_for_username(args.u,args.p):
        city, country = ip_address.get_location(args.IP_address)
        info = str("The IP ADDRESS "+ args.IP_address + " is located in "
                + city + " (" +  country +") ")
        print (info)
	csv_manager.write_data(csv_path,args.IP_address,city,country)
