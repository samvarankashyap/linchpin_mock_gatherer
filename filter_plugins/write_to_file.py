#!/usr/bin/env python
import os
import json

def write_to_file(data, path, filename, extn='.output'):

    filename = filename.replace(' ', '_').lower()
    path = os.path.expanduser(path)
    fd = open(path + filename + extn, "w")
    fd.write(json.dumps(data))
    fd.close()
    return data

class FilterModule(object):
    ''' A filter to write variables to file '''
    def filters(self):
        return {
            'write_to_file': write_to_file
        }
