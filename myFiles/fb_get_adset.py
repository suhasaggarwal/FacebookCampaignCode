import sys
import os
sys.path.append(os.path.abspath("C:\Users\Suhas Aggarwal\Downloads\FacebookCampaignCode-master\FacebookCampaignCode-master"))
from facebookads.objects import AdAccount, AdSet
from facebookads.api import FacebookAdsApi
from facebookads import objects

my_app_id = '140038042803966'
my_app_secret = 'c93321dac3181da22adf9b67c6572e24'
my_access_token = 'EAABZCXSXL3v4BAEZCDXGpUvkdEReybnruE75ByPRurgyukYhsJurz4Lrxa4F2rA3ZBvvm3dkMk8Vclr37ANIKExJzCWz3QRvt87XiuZCwN6Dxf0zZAq0ay0sYwPZBNyiaeVolcOifdIhaz6gvuuV5e3zlG0qRJc6oLC9iYBGSJoAZDZD'

#FacebookAdsApi.init(access_token= fb_access_token)

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

account = AdAccount('act_310419005')
adsets = account.get_ad_sets([
    AdSet.Field.name,
    AdSet.Field.status,
])

# This will output the name of all fetched ad sets.
for adset in adsets:
    print adset[AdSet.Field.name]
