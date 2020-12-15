""" it prints a new line in the csv file, if some errors are find it prints 
3 different error allerts: 1) File not found (if csv file does not exist
2) Value error (if values are not readable 3) UnicodeDecodeError (if the machine is not able
to decode the value) """
import csv

def read_csv(path):

    try:
        with open(path, 'r', newline='') as f:
            for line in csv.reader(f, delimiter=','):
                print(line)

    except FileNotFoundError:
        print ('The file does not exist')
        return

    except ValueError:
        print ('File has a wrong encoding')
        return

    except UnicodeDecodeError:
        print ('File has a wrong encoding')
        return

if __name__ == '__main__':
    path = 'data/ip_data.csv'
    read_csv(path)
