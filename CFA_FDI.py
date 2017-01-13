# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:47:43 2016

@author: johnsom
"""


import requests, warnings, datetime, re
from lxml import etree
from pandas import DataFrame, date_range
from dateutil import parser

def get_FDI(region):
    
    url = 'http://www.cfa.vic.gov.au/restrictions/%s-firedistrict_rss.xml' % region
    
    response = requests.get(url)
    
    root = etree.fromstring(response.content)
    
    run_date = datetime.datetime.now()
    pub_date = root.findall('.//dc:date', root.nsmap)[0].text
    pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%dT%H:%M:%SZ').date()
    
    n = 0
    
    columns = ['region','pub_date','predtype', 'FDI', 'TFB']
    index = date_range(run_date, periods=4, freq='D').date
    df = DataFrame(index=index, columns=columns)
    df.pub_date = pub_date
    df.region = region
    
    for e in root.iter('item'):
        if n < 4:
    
            desc = e.find('description').text
            FDI = re.compile(r'<p>Central: (.*?)</p>').search(desc).group(1)
            TFB = 'is <strong>not</strong> currently a day of Total Fire Ban' not in desc
            
            date = e.find('title').text
            for x,y in {'Today, ': '', 'Tomorrow, ': ''}.items():
                date = date.replace(x, y)
            date = parser.parse(date).date()
            
            #e.find('link').text
            #e.find('guid').text
            
            df.ix[n, 'FDI'] = FDI
            df.ix[n, 'TFB'] = TFB
            df.ix[n, 'predtype'] = (date - pub_date).days
            
            n += 1
        else:
            pass

    return(df)
    
region = ['central','']