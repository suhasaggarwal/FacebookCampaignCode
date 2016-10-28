import sys
import os
sys.path.append(os.path.abspath("/home/subhash/facebook-python-ads-sdk-master"))
from facebookads.objects import AdAccount, AdSet
from facebookads.api import FacebookAdsApi
from facebookads import objects

my_app_id = '839000112895379'
my_app_secret = '1bc9adcdfbdc6da9bb313868b2308289'
my_access_token = 'EAAL7EOZByFZAMBAK595vfvEwGOl6CWX9LuRpdD0JZBU9aURsBxpNbZAFDZAaGffHtDH85L2ux0Xp0b1dfCgM17vziIrQHOy5RA3W\
nQxM4Dn8n2l0w1YFzVQTJmhugLp7v7jMf4QxC9eDZAmgvScwHfIrpuY2oAflcZD'

#FacebookAdsApi.init(access_token= fb_access_token)

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

account = AdAccount('act_1615161972081611')
adsets = account.get_ad_sets([
    AdSet.Field.name,
    AdSet.Field.status,
])

# This will output the name of all fetched ad sets.
for adset in adsets:
    print adset[AdSet.Field.name]
