"""
1. Shelve module is used to organise your data when using pickle
2. Flag parameter:
    'r'	Open existing database for reading only
    'w'	Open existing database for reading and writing
    'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
    'n'	Always create a new, empty database, open for reading and writing
3. The keys must be strings
4. Use sync() to force the buffer flushing
5. You can use these dictionary utilities:
    5.1 the len() function;
    5.2 the in operator;
    5.3 the keys() anditems() methods;
    5.4 the update operation, which works the same as when applied to a Python dictionary;
    5.5 the del instruction, used to delete a key-value pair.
6. Because the shelve module is backed by pickle, it isn’t safe to load a shelve from an untrusted source. As with pickle, loading a shelve can execute arbitrary code.
"""
import shelve
DATAFILE = "datafile1"
myshelve = shelve.open(DATAFILE, flag="c")
myshelve["id"] = 1
myshelve["name"] = "Roberto"
myshelve["list"] = ["Roberto", 48]
myshelve.close()

myshelve = shelve.open(DATAFILE, flag="r")
for key in myshelve:
    print(key, ":", myshelve[key])

