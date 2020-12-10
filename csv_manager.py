import csv

def write_data(path,ip_address,city,country):
    try:
        open(path)
    except:
        with open(path, "w") as new_csv:
            pass

    data=[ip_address,city,country]
    with open(path, 'r',newline='') as f:
        rows = [ line for line in csv.reader(f, delimiter=',')]
        if data not in rows:
            with open(path, 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
