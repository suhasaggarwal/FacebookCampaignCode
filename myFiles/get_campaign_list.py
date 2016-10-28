import urllib
import sys
import os
import json
sys.path.append(os.path.abspath("/home/subhash/facebook-python-ads-sdk-master"))
from facebookads.adobjects.campaign import Campaign
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.targetingsearch import TargetingSearch


my_app_id = '839000112895379'
my_app_secret = '1bc9adcdfbdc6da9bb313868b2308289'
my_access_token = 'EAAL7EOZByFZAMBAK595vfvEwGOl6CWX9LuRpdD0JZBU9aURsBxpNbZAFDZAaGffHtDH85L2ux0Xp0b1dfCgM17vziIrQHOy5RA3W\
nQxM4Dn8n2l0w1YFzVQTJmhugLp7v7jMf4QxC9eDZAmgvScwHfIrpuY2oAflcZD'
account_id = 'act_1615161972081611'

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

'''
url = 'https://graph.facebook.com/v2.8/'+account_id+'/campaigns?access_token='+my_access_token

resp = urllib.urlopen(url).read()
data = json.loads(resp)['data']
#print resp
'''

params = {
    'q': 'allahabad, India',
    'type': 'adgeolocation',
    'location_types': ['city'],
}

resp = TargetingSearch.search(params=params)
print(resp)

'''
print data

for id in data:
    c_id = id['id']
    camp = Campaign(c_id)
    print camp[Campaign.Field.id]
    print camp.get_ad_sets()

'''
