

### IP ADDRESS GEO-LOCATION :globe_with_meridians:

In this repository you can find a file named ```main.py``` that triggers the ip-api.com API and return the city where the ip address is from. 

If you run the program, executing the main file with: ```$ python main.py 1.2.3.4 -u test -p test``` it will  give you results similar to the following: 

```
$ python main.py 1.2.3.4 -u admin -p admin
The IP ADDRESS 1.2.3.4 is located in South Brisbane (Australia)
```

A user can choose an IP Address they need the geo location. Once a user has asked for the ip address, their information will be registered in a csv file named ip_data.csv. This is done through an internal function in the csv_manager.py.

### Command line parameters :computer:
In order to execute the ```main.py``` file, a few command line parameters must be passed.
#### Positional arguments
- **ip address**: The ip address the user needs the information. **Only one** ip address can be chosen.

#### Optional Argument
- **-h, --help**: displays all the possible options for each parameter; 
- **-v**:  displays the output with different levels of verbosity (at the moment only one level of verbosity is supported);
- **-u U [required]:** the username (requires *-p*).  
- **-p P [required]:** the user's password.

### How to manage the database :busts_in_silhouette:
In order to run ```main.py``` you will need a **username** and a **password**. The package comes with a **default user** with the following credenentials:
- *username*: **test**
- *password*: **test**

There is the possibility to add new users. You can find a helper module ```dbmanager.py``` in the parent directory that allows you to populate the database.

#### Adding a new user
Use the parameter ```-a```. Requires the following:
 - **-a:** username 
 - **-p:** password
```
$ python databasemanager.py -a admin -p admin 
The registration has been successful
```

### References :green_book:
The API we use is offered by [ip-api](https://ip-api.com/docs/api:json)

### Authors and acknowledgment :busts_in_silhouette:
- **Bottacini Riccardo**
- **Cardone Lorenzo**
- **Cosimo Borelli**
- **Galiazzo Sofia Irene**
- **Scuccato Alberto**

### License :page_facing_up:
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)


