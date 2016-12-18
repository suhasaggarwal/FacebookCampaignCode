import urllib
import sys
import os
import json
sys.path.append(os.path.abspath("C:\Users\Suhas Aggarwal\Downloads\FacebookCampaignCode-master\FacebookCampaignCode-master"))
from facebookads.adobjects.campaign import Campaign
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.targetingsearch import TargetingSearch

my_app_id = '140038042803966'
my_app_secret = 'c93321dac3181da22adf9b67c6572e24'
my_access_token = 'EAABZCXSXL3v4BAEZCDXGpUvkdEReybnruE75ByPRurgyukYhsJurz4Lrxa4F2rA3ZBvvm3dkMk8Vclr37ANIKExJzCWz3QRvt87XiuZCwN6Dxf0zZAq0ay0sYwPZBNyiaeVolcOifdIhaz6gvuuV5e3zlG0qRJc6oLC9iYBGSJoAZDZD'
account_id = 'act_310419005'

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
