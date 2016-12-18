import sys
import os
sys.path.append(os.path.abspath("C:\Users\Suhas Aggarwal\Downloads\FacebookCampaignCode-master\FacebookCampaignCode-master"))
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec

from facebookads.adobjects.advideo import AdVideo
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebookads.adobjects.adcreativevideodata import AdCreativeVideoData

from fb_app_config import *
from facebookads.api import FacebookAdsApi
from facebookads import objects


class Creative:

    def __init__(self, creative_detail, obj, click_tracker):
        #app_obj = AppConf()
        #FacebookAdsApi.init(app_obj.my_app_id, app_obj.my_app_secret, app_obj.my_access_token)
        '''
        self.me = camp_object.me
        self.my_accounts = list(self.me.get_ad_accounts())
        self.my_account = self.my_accounts[0]
        '''
        self.obj = obj
        self.creative_detail = creative_detail
        self.c_type = 'None'
        self.c_title = 'None'
        self.file_path = 'None'
        self.click_tracker = click_tracker

    def ad_video(self, video_path):
        video = AdVideo(parent_id=self.obj.act_id)
        video[AdVideo.Field.filepath] = video_path
        video.remote_create()

    def ad_image(self, image_path):
        image = AdImage(parent_id=self.obj.act_id)
        image[AdImage.Field.filename] = image_path
        image.remote_create()

        # Output image Hash
        print(image[AdImage.Field.hash])

        return image[AdImage.Field.hash]

    def create_creative(self):

        for row in self.creative_detail:
            c_type = row[20]

            if c_type == 'newsfeed':
                self.c_title = row[2]
                self.file_path = row[3]

            elif c_type == 'video':
                self.c_title = row[12]
                self.file_path = row[11]

            elif c_type == 'mobile':
                self.c_title = row[8]
                self.file_path = row[9]

            elif c_type == 'RHS':
                self.c_title = row[4]
                self.file_path = row[7]

            elif c_type == 'images':
                self.c_title = 'Slide Show'
                self.file_path = row[10]

            else:
                print 'Creative Error. Please provide correct detail for the creative.'

            print self.obj.act_id

            #self.file_path = 'https://creativedata.s3.amazonaws.com/b36248286-snowflake.swf'
            #image_hash = self.ad_image(self.file_path)

            link_data = AdCreativeLinkData()
            link_data[AdCreativeLinkData.Field.message] = 'No Message.'

            #if self.obj.campaign_objective == 'LINK_CLICKS':
            link_data[AdCreativeLinkData.Field.link] = self.file_path           #self.click_tracker

            link_data[AdCreativeLinkData.Field.caption] = self.c_title
            #link_data[AdCreativeLinkData.Field.image_hash] = image_hash

            object_story_spec = AdCreativeObjectStorySpec()
            object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = '349224428539835'
            object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

            creative = AdCreative(parent_id=self.obj.act_id)
            creative[AdCreative.Field.name] = 'AdCreative for Campaign'
            creative[AdCreative.Field.object_story_spec] = object_story_spec
            creative.remote_create()

            print(creative)

            #print creative.get_id()

        '''
        elif self.c_type == 'video':
            video_path = ''
            video_hash = self.ad_video(video_path)

            video_data = AdCreativeVideoData()
            video_data[AdCreativeVideoData.Field.description] = 'My video description'
            video_data[AdCreativeVideoData.Field.video_id] = video_hash
            #video_data[AdCreativeVideoData.Field.image_url] = '<IMAGE_URL>'
            #video_data[AdCreativeVideoData.Field.call_to_action] = {'type': 'LIKE_PAGE','value':{'page': '<PAGE_ID>',},}

            object_story_spec = AdCreativeObjectStorySpec()
            object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = '507270992665963'
            object_story_spec[AdCreativeObjectStorySpec.Field.video_data] = video_data

            creative = AdCreative(parent_id='act_<AD_ACCOUNT_ID>')
            creative[AdCreative.Field.name] = 'Video Ad Creative'
            creative[AdCreative.Field.object_story_spec] = object_story_spec
        '''

        return creative

