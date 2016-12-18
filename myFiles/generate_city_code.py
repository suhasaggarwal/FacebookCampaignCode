import urllib
import sys
import os
import json
sys.path.append(os.path.abspath("C:\Users\Suhas Aggarwal\Downloads\FacebookCampaignCode-master\FacebookCampaignCode-master"))
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.targetingsearch import TargetingSearch

my_app_id = '140038042803966'
my_app_secret = 'c93321dac3181da22adf9b67c6572e24'
my_access_token = 'EAABZCXSXL3v4BAEZCDXGpUvkdEReybnruE75ByPRurgyukYhsJurz4Lrxa4F2rA3ZBvvm3dkMk8Vclr37ANIKExJzCWz3QRvt87XiuZCwN6Dxf0zZAq0ay0sYwPZBNyiaeVolcOifdIhaz6gvuuV5e3zlG0qRJc6oLC9iYBGSJoAZDZD'
account_id = 'act_310419005'

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
        j = i['id']
        print v
        print j

def get_interest_List(interest):

    interest_map = {'62:64':{'id': 6003940339466,'name': 'Entertainment/Games/Video games'},'68:69':{'id': 6002839660079,'name': 'Shopping and fashion/Beauty/Cosmetics'}}

    return interest_map[interest]


if __name__ == '__main__':
    #city_list = ['Delhi','Gurgaon','Mumbai','Bangalore','Noida','Chennai','Guwahati','Ahmedabad','Kochi','Jaipur','Lucknow','Calcutta','Agra','Jammu','Manipal','Puducherry','Gwalior','Malda','Solapur','Panjim','Palakkad','Gandhinagar','Raipur','Mehsana','Kurnool','Namakkal','Eluru','Tezpur','Ulhasnagar','Kottayam','Cuttack','Rourkela','Anand','Erode','Kolhapur','Kozhikode','Kannur','Howrah']
    city_list = ['Entertainment/Movies/Musical theatre']
    #city_list = (('Mumbai',), ('Bangalore',), ('Noida',), ('Chennai',), ('Guwahati',))
    key_list = []
    for name in city_list:
        v = get_interest_code(name[0])
        key_list.append(v)
    print key_list
    print get_interest_List('Tech : gaming')