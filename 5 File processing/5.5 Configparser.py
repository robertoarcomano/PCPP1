"""
1 Configparser to read configuration from a file
2 Structure: like Windows .ini file
3 Craete a ConfigParser obj
"""
import configparser

def show_config(config, use_get = False):
    for section in config.sections():
        print(section)
        for item in config[section]:
            print(item + ":", config[section][item] if not use_get else config.get(section, item))
        print()


print("Using []")
config1 = configparser.ConfigParser()
config1.read("config.ini")
show_config(config1)

print("Using config.get")
show_config(config1, True)

my_dict = {
    "DEFAULT": {
        "host": "localhost"
    },
    "ORACLE": {
        "username": "user",
        "password": "pass"
    },
    "MYSQL": {
        "username": "user1",
        "password": "pass1"
    }
}

print("Reading from dict")
config2 = configparser.ConfigParser()
config2.read_dict(my_dict)
show_config(config2)