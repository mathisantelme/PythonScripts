#!/bin/python

# TODO: cleanup the code

# used to check if the input file exists
import os

# used to parse options from the command line
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input")

# default input file path
DEFAULT_INPUT_FILEPATH="input.txt"

# the different options and their corresponding OIDs
OPTIONS_LIST={
    'full': "1.3.6.1.4.1.8072.1.3.2.3.1.2",
    'line': "1.3.6.1.4.1.8072.1.3.2.3.1.1",
    'command': "1.3.6.1.4.1.8072.1.3.2.2.1.2",
    'args': "1.3.6.1.4.1.8072.1.3.2.2.1.3"
}

def textToOID (txt, opt="full"):
    # checking the option selected
    if opt in OPTIONS_LIST:
        print "[status]: converting \"{}\" to OID using the \"{}\" option".format(txt, opt)
        
        # we catch the length of the string
        res = str(len(txt)) 

        # for each character of the string
        for c in txt:
            res += ('.' + str(ord(c))) # appending a dot + the ASCII value of the character

        # returning the OID corresponding to the option and the string
        return str(OPTIONS_LIST[opt] + '.' + res);

    else:
        print "[error]: wrong option called: \"{}\"".format(opt)

def fileContentToOIDs (filepath):

    # if the file exists
    if os.path.isfile(filepath):
        # openning the file
        file = open(filepath, 'r')

        for line in file:
            
            name = line.split(" ")[0].rstrip("\n\r") # catching the name

            try:
                arg = line.split(" ")[1].rstrip("\n\r") # trying to catch the arg
            except IndexError:
                # if no arg found, calling the function without arg
                res = "[full]: {} -> {}\n".format(name, textToOID(name))
            else:
                res = "[{}]: {} -> {}\n".format(arg, name, textToOID(name, arg))

            print res
        file.close()

    # if the file doesn't exist
    else:
        print "[error]: the file {} doesn't exist, quitting".format(filepath)
        exit()

if __name__ == "__main__":
    (options, args) = parser.parse_args() # parsing the options of the command line

    fileContentToOIDs((DEFAULT_INPUT_FILEPATH, options.input)[options.input != None])
