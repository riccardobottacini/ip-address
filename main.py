from scripts import ip_address
from scripts import csv_manager
import databasemanager
import argparse

IP_address = '1.2.3.4'
csv_path = 'data/ip_data.csv'
database_path = 'data/database.db'

databasemanager.db_creation(database_path)


def parse_arguments():
    """parse the user arguments"""

    parser = argparse.ArgumentParser(description='IP ADDRESS prject')
    parser.add_argument('IP_address', type=str,
                        help='Insert an IP Address', default=None)
    parser.add_argument('-u', help='username name (requires -p)',
                        default=None)
    parser.add_argument('-p', help='username password', default=None)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true',
                       help='print quiet')
    group.add_argument('-v', '--verbose', action='store_true',
                       help='print verbose')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_arguments()
    if databasemanager.check_for_username(args.u, args.p):
        (city, country) = ip_address.get_location(args.IP_address)
        info = str('The IP ADDRESS ' + args.IP_address
                   + ' is located in ' + city + ' (' + country + ') ')
        print (info)
        csv_manager.write_data(csv_path, args.IP_address, city, country)
    else:
        print ('Something goes wrong!')
