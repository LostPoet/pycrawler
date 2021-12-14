#!/usr/bin/python
# -*- coding: UTF-8 -*-

import yaml
import requests
import url_parser

with open('config.yml', 'r') as config:
    yml_data = yaml.load(config, Loader=yaml.FullLoader)

root_url = yml_data['3gpp_root_url']
dump_path = yml_data['dump_path']

for spec_item in yml_data['spec_list']:
    spec = spec_item['name']
    version = spec_item['version']

    spec_url = url_parser.build_url(root_url, spec)
    rsp = requests.get(spec_url)
    spec_file_url = url_parser.get_spec_url(rsp.text, spec, version)
    print(spec_file_url)
    
    import zipfile, io
    rsp = requests.get(spec_file_url)
    z = zipfile.ZipFile(io.BytesIO(rsp.content))
    z.extractall(dump_path + version)