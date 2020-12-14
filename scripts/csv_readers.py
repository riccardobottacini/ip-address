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
