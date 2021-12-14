#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from bs4 import BeautifulSoup

def build_url(base_url:str, spec_name: str) -> str:
    num_splits = spec_name.split('.')
    return base_url + num_splits[0] + "_series/" + spec_name

def get_spec_url(html_text: str, spec_name: str, spec_version: str) -> str:
    soup = BeautifulSoup(html_text, 'html.parser')
    file_name = spec_name.split('.')[0] + spec_name.split('.')[1] + '-' + spec_version
    latest_href = None
    links = soup.findAll('a')
    for link_node in links:
        match = re.search(file_name, link_node['href'])
        if match:
            latest_href = link_node['href']
    return latest_href