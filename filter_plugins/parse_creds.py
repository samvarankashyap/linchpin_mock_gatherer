#!/usr/bin/env python

import os
import yaml
import json
import configparser as ConfigParser

class ConfigDict(ConfigParser.ConfigParser):

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

def parse_creds(creds_folder, file_name, creds_type):
    creds_path = os.path.abspath(creds_folder+"/"+file_name)
    if creds_type == "cfg":
        config = ConfigDict()
        f = open(creds_path)
        config.readfp(f)
        creds = config.as_dict()
        f.close()
        return creds
    if creds_type == "yaml":
        f = open(creds_path)
        creds = yaml.load(f.read())
        f.close()
        return creds
    if creds_type == "json":
        f = open(creds_path)
        creds = json.loads(f.read())
        f.close()
        return creds
    return creds_path

class FilterModule(object):
    ''' filter to parse credentials '''
    def filters(self):
        return {
            'parse_creds': parse_creds
        }
