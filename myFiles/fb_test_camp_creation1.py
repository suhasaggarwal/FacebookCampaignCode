import sys
import os

from fb_campaign_query import *
from generate_city_code import *
from fb_ad_creative import *
from fb_app_config import *


sys.path.append(os.path.abspath("/home/subhash/facebook-python-ads-sdk-master"))
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.ad import Ad


objective_mapping = {'1': 'LINK_CLICKS', '5': 'MOBILE_APP_INSTALLS', '4': 'PRODUCT_CATALOG_SALES', '3': 'VIDEO_VIEWS',
                     '6': 'LEAD_GENERATION', '2': 'BRAND_AWARENESS'}

'''
In adset targeting section we have not implemented interest segment,age range and income range based targeting.
Also objective and billing event mapping is not defined
Page ID
'''


class CreateCamp:

    def __init__(self, campaign_name, campaign_objective, campaign_status):

        app_obj = AppConf()
        FacebookAdsApi.init(app_obj.my_app_id, app_obj.my_app_secret, app_obj.my_access_token)
        self.campaign_name = campaign_name
        self.campaign_objective = objective_mapping[campaign_objective]
        self.campaign_status = campaign_status
        self.billing_event = 'impressions'              #initialized with impressions will change according to objective

        #self.me = objects.AdUser(fbid='me')
        #self.my_accounts = list(self.me.get_ad_accounts())
        #self.my_account = self.my_accounts[0]
        self.act_id = 'act_1615161972081611'

    def createcampaign(self):
        campaign = None
        try:
            campaign = objects.Campaign(parent_id=self.act_id)

            campaign[Campaign.Field.name] = self.campaign_name
            campaign[Campaign.Field.status] = self.campaign_status
            campaign[Campaign.Field.objective] = self.campaign_objective

            campaign.remote_create()
        except Exception as e:
            print 'Error while creating campaign. Error Detail : '+str(e)
        return campaign

    def gettargeting(self, adset_obj):
        objective = self.campaign_objective

        if objective == '':
            self.billing_event = 1

        elif objective == '':
            self.billing_event = 1

        elif objective == '':
            self.billing_event = 1

        else:
            self.billing_event = 1

        d = dict()
        d["geo_locations"] = {'cities': adset_obj.city_key_list}

        if len(adset_obj.os_list) > 0:
            d["user_os"] = adset_obj.os_list[0:2]

        #if len(adset_obj.device_list) > 0:
        #   d["user_device"] = adset_obj.device_list

        if len(adset_obj.gender) > 0:
            d["genders"] = adset_obj.gender

        '''
        d = {'geo_locations': {'cities': adset_obj.city_key_list},
             #'user_device': adset_obj.device_list,
             'user_os': adset_obj.os_list[0:2],
             #'user_os': ["iOS","Android_ver_4.4"]
        }
        '''
        return d

    def createadset(self, ads_obj, campaign):
        adset = AdSet(parent_id=self.act_id)
        adset.update({
                         AdSet.Field.name: ads_obj.adset_name,
                         #AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
                         AdSet.Field.billing_event: AdSet.BillingEvent.link_clicks,
                         AdSet.Field.bid_amount: ads_obj.bid_amount,
                         AdSet.Field.daily_budget: ads_obj.daily_budget,
                         AdSet.Field.campaign_id: campaign.get_id(),
                         AdSet.Field.targeting: ads_obj.targeting_dict
        })
        adset.remote_create(params={'status': AdSet.Status.paused, })
        return adset


class CreateAdSet:

    def __init__(self, name, bid, daily_budget, key_list, os_list, device_list, gender, targeting=None):
        self.adset_name = name
        self.bid_amount = bid
        self.daily_budget = daily_budget
        self.city_key_list = key_list
        self.os_list = os_list
        self.device_list = device_list
        self.targeting_dict = targeting
        self.gender = map(int, gender.strip().split(',')[0:-1])

if __name__ == '__main__':

    db_query_obj = DBQuery()
    result_obj = db_query_obj.execute_queries()

    result, error = result_obj.result, result_obj.error

    print result, error

    if (error == True) and len(result) > 0:
        print 'Error while executing query set : ', str(error), str(result)
        #return error

    else:
        print result[0][0], result[0][1], result[0][2], result[0][5]
        camp_id = result[0][0]
        camp_name = str(result[0][1])
        objective = str(result[0][2])
        status = str(result[0][5])
        status = status.upper()
        if status in ['PAUSE', 'NONE', 'STOP']:
            status = 'PAUSED'
        obj = CreateCamp(camp_name, objective, status)

        #camp_name = 'General Brand Awareness1'
        #objective = '1'
        #status = 'PAUSED'

        print camp_id,'/t', camp_name, '/t', objective, '/t', status

        #campaign = obj.createcampaign()
        #print campaign

        budget_query_result = result_obj.budget_query_result

        if len(budget_query_result) > 0:
            #print 'Budget : ',budget_query_result
            total_budget = budget_query_result[0][1]
            daily_budget = budget_query_result[0][3]
            bid_amount = budget_query_result[0][6]
            click_tracker = budget_query_result[0][7]

            adset_name = camp_name + '_adset'

            print adset_name, '/t', bid_amount

            target_camp_query_result = result_obj.target_camp_query_result
            gender = '1,2'
            if len(target_camp_query_result) > 0:
                target_camp_id = target_camp_query_result[0][0]
                interest_segment_id = target_camp_query_result[0][4]
                geography_id = str(target_camp_query_result[0][5])
                age_range = target_camp_query_result[0][6]
                gender = target_camp_query_result[0][7]
                income_range = target_camp_query_result[0][8]

            geography_query_result = result_obj.geography_query_result
            key_list = []
            if not error and len(geography_query_result) > 0:
                #print geography_query_result
                city_list = geography_query_result
                for name in city_list:
                    v = get_code(name[0])
                    key_list.append(v)

                print key_list

            else:
                print 'Error while fetching data of geolocation. This is a blocker. Error is: '+str(error)

            ########### Calculate Targeting OS list ###################################

            get_os_query_result = result_obj.get_os_query_result
            os_list = []
            if len(get_os_query_result) > 0:
                #print get_os_query_result
                for name in get_os_query_result:
                    #v = get_code(name[0]
                    os_list.append(name[0].strip().replace(' ','_ver_'))
                print os_list

            ############################# Calculate Targeting Device list #########################

            device_list = []

            get_device_query_result = result_obj.get_device_query_result
            if len(get_device_query_result) > 0:
                #print get_device_query_result
                for name in get_device_query_result:
                    device_list.append(name[0])
                print device_list

            ###################### Calculate Interest Segment list ############################


            ###################### Create campaign ############################################

            obj = CreateCamp(camp_name, objective, status)
            campaign = obj.createcampaign()
            print campaign

            #adsetobj = CreateAdSet(adset_name, bid_amount, daily_budget, key_list, os_list, device_list )
            # Creating adset is accepting a certain amount as daily budget. Here in this case > 9100

            adsetobj = CreateAdSet(adset_name, bid_amount, '10000', key_list, os_list, device_list, gender)
            adsetobj.targeting_dict = obj.gettargeting(adsetobj)
            adset = obj.createadset(adsetobj, campaign)

            print adset.get_id()
            if not result_obj.error:
                creative_obj = Creative(result_obj.get_creative_detail_query_result, obj, click_tracker)
                try:
                    creative = creative_obj.create_creative()

                    ad = Ad(parent_id= obj.act_id)
                    ad[Ad.Field.name] = obj.campaign_name + 'Adset_ad'
                    ad[Ad.Field.adset_id] = adset.get_id()
                    ad[Ad.Field.creative] = {
                                                'creative_id': creative.get_id()
                    }
                    ad.remote_create(params={
                        'status': Ad.Status.paused,
                    })
                except Exception as e:
                    print str(e)
            else:
                print 'Error :'+result_obj.error

            #creative_obj = ''
