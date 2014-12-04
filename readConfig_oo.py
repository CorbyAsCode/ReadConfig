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

class JsonParse(object):
    def __init__(self, env='', role=''):
        self.env  = env
        self.role = role
        self.jsonFile = 'xh_servers.json'
        
        try:
            f = open(self.jsonFile)
        except Exception, e:
            print "Could not open %s\n%s" % (self.jsonFile, e)
            os._exit(1)
            
        data = ''
        for line in f.readlines():
            m = re.search(r'^([^#$].*$)', line)
            if m:
                match = m.groups()[0]
                match = match.strip()
                data += match
                data = str(data)
                
        self.json = simplejson.loads(data)

    def getEnvs(self):
        return self.json
    
    def getRoles(self):
        try:
            if self.env in self.getEnvs():
                return self.getEnvs()[self.env]
            else:
                raise KeyError()
        except KeyError:
            if self.env == '' or type(self.env) != str:
                print "\nreturnRole() requires an environment to be passed in!\n"
                os._exit(1)
            elif type(self.env) != str:
                print "\nEnvironment variable is not a string = '%s'\n" % self.env
                os._exit(1)
            else:
                print "\nBad Environment variable:  '%s'\n" % self.env
        
    def getHosts(self):
        try:
            if self.role in self.getRoles():
                return self.getRoles()[self.role]
            else:
                raise KeyError()
        except Exception:
            if self.role == '' or type(self.role) != str:
                print "\nreturnRole() requires an environment to be passed in!\n"
                os._exit(1)
            elif type(self.role) != str:
                print "\nEnvironment variable is not a string = '%s'\n" % self.role
                os._exit(1)
            else:
                print "\nBad Environment variable:  '%s'\n" % self.role

    def returnEnvs(self):
        return sorted(self.getEnvs().keys())

    def returnRoles(self):
        return sorted(self.getRoles().keys())
       
    def returnHosts(self):
        return sorted(self.getHosts().keys())
        
'''
def returnHost(self):
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
'''