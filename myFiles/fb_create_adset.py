import sys
import os
sys.path.append(os.path.abspath("C:\Users\Suhas Aggarwal\Downloads\FacebookCampaignCode-master\FacebookCampaignCode-master"))
from facebookads.adobjects.adset import AdSet

class CreateAdSet:

    def __init__(self, name, bid, daily_budget):
        self.adset_name = name
        self.bid_amount = bid
        self.daily_budget = daily_budget

    def gettargeting(self):
        objective = self.campaign_objective

        if objective == '':
            a = 1

        elif objective == '':
            b = 1

        elif objective == '':
            c = 1

        else:
            d = 1

        return {
            'geo_locations': {'countries': ['IN'], 'cities': ['Delhi', 'Mumbai']},
            'user_device': ['galaxy s6', 'one plus', ],
            'user_os': ['android'],
        }

    def createadset(self, campaign, bid_amount, daily_budget, adset_name):
        adset = AdSet(parent_id=self.my_account.get_id_assured())
        adset.update({
            AdSet.Field.name: adset_name,
            # AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
            # AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
            AdSet.Field.bid_amount: bid_amount,
            AdSet.Field.daily_budget: daily_budget,
            AdSet.Field.campaign_id: campaign.get_id(),
            AdSet.Field.targeting: self.gettargeting()
        })
        adset.remote_create(params={'status': AdSet.Status.paused,})
        return adset
