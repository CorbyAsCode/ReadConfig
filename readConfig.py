#!/usr/bin/python
# Uncomment previous line for virtual Python environs

###################################################################
#
#  Author: Corby Shaner
#  Date  : 30-01-2014
#  
#  json_parser.py is an importable module that parses JSON files
#  and returns the data structure as a dictionary.
#
###################################################################


import re, simplejson, os

def jsonParser():
    # Initialize variables
    json = ''
    filename = 'xh_servers.json'

    # Get a read-only filehandle pass exceptions to scripts
    # that import this module
    try:
        f = open(filename)
    except Exception, e:
        print "Could not open %s\n%s" % (filename, e)
        os._exit(1)

    # Put each line of the file into an array
    text = f.readlines()

    # Iterate over the array
    for line in text:

        # Use a regex to eliminate lines that start with '#' or '$'
        # In python, the parenthesis can be used to store 
        # match results in a match object that you can then store in
        # a variable.
        # The caret inside the [] means NOT...so we're searching
        # for anything where the line doesn't start with '#' or '$'
        m = re.search(r'^([^#$].*$)', line)

        # If there's a match
        if m:
            # For simplicity, store the match in a variable
            match = m.groups()[0]
            # Remove whitespace and the newline characters
            match = match.strip()
            # Append the match to the json variable.  
            json += match

        # Print out No Match for debugging purposes
        #else:
            #print "No match"
      
    # Convert the json variable to a string because simplejson expects
    # a string instead of a raw data structure
    json = str(json)

    # Print out the value of json for debugging purposes
    #print "json = " + json

    # Load the json variable into memory as a dictionary (hash) data structure
    data_structure = simplejson.loads(json)

    return data_structure
    

def returnEnv(data=''):
    #if not data:
        #err = "returnEnv needs 1 variable passed in"
        #raise NameError(err)
        #pass
    #else:
        #return sorted(data.keys())
    try:
        return sorted(data.keys())
    except AttributeError:
         if data == '':
             print "\nreturnEnv() requires a JSON object to be passed in!\n"
             os._exit(1)
         else:
             print "\nValue of variable passed into returnEnv() =\n%s\n" % data
             os._exit(1)

def returnRole(data='', env=''):
    try:
        return sorted(data[env].keys())
    except AttributeError:
        if env == '':
            print "\nreturnRole() requires a string to be passed in!\n"
            os._exit(1)
        else:
            print "\nValue of variable passed into returnRole() =\n%s\n" % env
            os._exit(1)
       

def returnHost(data='', env='', role=''):
    try:
        return sorted(data[env][role].keys())
    except AttributeError:
        if role == '':
            print "\nreturnHost() requires a string to be passed in!\n"
            os._exit(1)
        else:
            print "\nValue of variable passed into returnRole() =\n%s\n" % role
            os._exit(1)
        
def returnHostdict(data='', env='', role=''):
    try:
        return data[env][role]
    except Exception, e:
        print "Path does not exist"
        
        
if __name__ == '__main__':
    data = jsonParser()
    
    print '\n\n'
    print data['Production']['Primary Application Server']
    print '\n\n'
