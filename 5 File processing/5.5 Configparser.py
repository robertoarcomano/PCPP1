"""
1 Configparser to read configuration from a file
2 Structure: like Windows .ini file
3 Create a ConfigParser obj
4 read from file
5 write to file descriptor
6 interpolation (templating)
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

print("Writing")
config3 = configparser.ConfigParser()
config3["DEFAULT"] = {"host": "localhost"}
config3["ORACLE"] = {
    "username": "user",
    "password": "pass"
}
config3["MYSQL"] = {
    "username": "user1",
    "password": "pass1",
    "test_host": "%(host)s"
}
show_config(config3)
with open("config1.ini", "w") as configfile:
    config3.write(configfile)
print()

print("Reading the interpolated value")
config4 = configparser.ConfigParser()
config4.read("config1.ini")
show_config(config4)


