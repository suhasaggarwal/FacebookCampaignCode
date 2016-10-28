import urllib
import sys
import os
import json
sys.path.append(os.path.abspath("/home/subhash/facebook-python-ads-sdk-master"))
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.targetingsearch import TargetingSearch



my_app_id = '839000112895379'
my_app_secret = '1bc9adcdfbdc6da9bb313868b2308289'
my_access_token = 'EAAL7EOZByFZAMBAK595vfvEwGOl6CWX9LuRpdD0JZBU9aURsBxpNbZAFDZAaGffHtDH85L2ux0Xp0b1dfCgM17vziIrQHOy5RA3W\
nQxM4Dn8n2l0w1YFzVQTJmhugLp7v7jMf4QxC9eDZAmgvScwHfIrpuY2oAflcZD'
account_id = 'act_1615161972081611'

def get_code(city):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    city_name = city + ", India"
    params = {
        'q': city_name,
        'type': 'adgeolocation',
        'location_types': ['city'],
    }
    try:
        resp1 = TargetingSearch.search(params=params)
        #print resp1
        resp = resp1[0]
        #print resp['key']
        #print city_name+'==='+str(resp['key'])+'==='+str(resp['name'])+'==='+str(resp['region'])+'==='+str(resp['region_id'])
        d = {'key': resp['key'], 'radius': '50', 'distance_unit': 'mile',}
        return d

    except Exception as e:
        print e
        print 'None','None','None','None'


def get_interest_code(interest):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    #interest = interest + ', India'

    params = {
        'type': 'adTargetingCategory',
        'class': 'interests',
    }

    '''
    params = {
        'q': interest,
        'type': 'adinterest',
    }

    params = {
        'type': 'adinterestvalid',
        'interest_list': ['Cricket'],
    }
    '''
    resp = TargetingSearch.search(params=params)
    for i in resp:
        v = '/'.join(i['path'])
        print v

if __name__ == '__main__':
    #city_list = ['Delhi','Gurgaon','Mumbai','Bangalore','Noida','Chennai','Guwahati','Ahmedabad','Kochi','Jaipur','Lucknow','Calcutta','Agra','Jammu','Manipal','Puducherry','Gwalior','Malda','Solapur','Panjim','Palakkad','Gandhinagar','Raipur','Mehsana','Kurnool','Namakkal','Eluru','Tezpur','Ulhasnagar','Kottayam','Cuttack','Rourkela','Anand','Erode','Kolhapur','Kozhikode','Kannur','Howrah']
    city_list = ['Cricket']
    #city_list = (('Mumbai',), ('Bangalore',), ('Noida',), ('Chennai',), ('Guwahati',))
    key_list = []
    for name in city_list:
        v = get_interest_code(name[0])
        key_list.append(v)
    print key_list
