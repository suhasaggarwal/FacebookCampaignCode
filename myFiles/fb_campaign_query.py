from db_connect import *


class DBQuery:

    def __init__(self):
        self.result = ''
        self.budget_query_result = ''
        self.target_camp_query_result = ''
        self.geography_query_result = ''
        self.os_target_query_result = ''
        self.get_os_query_result = ''
        self.device_target_query_result = ''
        self.get_device_query_result = ''
        self.error = ''

    def execute_queries(self):
        db_obj = DBConnect()

        sql_query_camp_id = 'select t.CampaignId from CampaignChannel t where  t.CreatedTime > date_sub(now(), interval 5 minute)'
        print sql_query_camp_id
        self.result1, self.error = db_obj.db_connect_query(sql_query_camp_id)
        print self.result1
        print self.error
        cid =  self.result1[0][0]
        print cid
        sql_query_camp = 'SELECT * FROM Campaign WHERE Id =' + str(390878926)
        self.result, self.error = db_obj.db_connect_query(sql_query_camp)

        print sql_query_camp

        if not self.error and len(self.result) > 0:
            camp_id = camp_id = self.result[0][0]

            budget_query = 'SELECT * FROM BudgetCampaign bc WHERE bc.CampaignId =' + str(camp_id)

            print budget_query
            self.budget_query_result, self.error = db_obj.db_connect_query(budget_query)

            target_camp_query = 'SELECT * FROM TargetCampaign tc, CampaignChannel cd WHERE cd.CampaignId =' + str(
                camp_id) + ' AND cd.TargetCampaignChannelId = tc.Id' + ' AND cd.ChannelId = 1'

            print 'Target query: ', target_camp_query

            self.target_camp_query_result, self.error = db_obj.db_connect_query(target_camp_query)
            target_camp_query_result = self.target_camp_query_result

            print self.target_camp_query_result

            if not self.error and len(self.target_camp_query_result) > 0:
                target_camp_id = target_camp_query_result[0][0]
                interest_segment_id = target_camp_query_result[0][4]
                geography_id = str(target_camp_query_result[0][5])
                age_range = target_camp_query_result[0][6]
                gender = target_camp_query_result[0][7]
                income_range = target_camp_query_result[0][8]

                geography_id = geography_id.replace(' ', '')
                geo_list = geography_id.split(',')
                geo_tuple = tuple(geo_list)

                print geo_tuple

                geography_query = 'SELECT g.City FROM Geography g WHERE g.Id IN ' + str(geo_tuple).rstrip(',')
                print geography_query
                self.geography_query_result, self.error = db_obj.db_connect_query(geography_query)

                if self.error or len(self.geography_query_result) == 0:

                    print 'Error in fetching geolocation. Detail : ', self.error, '\n', self.geography_query_result
                    self.error = True

                else:

                    os_target_query = 'SELECT * FROM TargetCampaignOS WHERE TargetCampaignId =' + str(target_camp_id)
                    self.os_target_query_result, self.error = db_obj.db_connect_query(os_target_query)

                    if not self.error and len(self.os_target_query_result) > 0:
                        os_id = str(self.os_target_query_result[0][1]).replace(' ', '').split(',')
                        os_tuple = tuple(os_id)

                        print os_tuple
                        get_os_query = 'SELECT os.Name as os_name FROM OperatingSystems os Where os.Id IN ' + str(os_tuple).rstrip(',')

                        print  get_os_query

                        self.get_os_query_result, self.error = db_obj.db_connect_query(get_os_query)

                        device_target_query = 'SELECT * FROM TargetCampaignDevice WHERE TargetCampaignId =' + str(target_camp_id)
                        self.device_target_query_result, self.error = db_obj.db_connect_query(device_target_query)
                    else:
                        print 'Error in fetching OS target detail: ', self.error, self.os_target_query_result
                        self.error = True

                    if not self.error and len(self.device_target_query_result) > 0:
                        print str(self.device_target_query_result[0][1])
                        device_id = str(self.device_target_query_result[0][1]).replace(' ', '').split(',')
                        print device_id

                        device_tuple = tuple(device_id)
                        print device_tuple
                        get_device_query = 'SELECT device.Name as device_name FROM Device device Where device.Id IN ' + str(device_tuple).rstrip(',')
                        print get_device_query

                        self.get_device_query_result, self.error = db_obj.db_connect_query(get_device_query)

                    else:
                        print 'Error in fetching OS target detail: ', self.error, self.device_target_query_result
                        self.error = True

                    channel_creative_query = 'SELECT * FROM CampaignChannel WHERE CampaignId = ' + str(
                        camp_id) + ' AND ChannelId = "1"'
                    self.channel_creative_query_result, self.error = db_obj.db_connect_query(channel_creative_query)

                    if not self.error and len(self.channel_creative_query_result) > 0:
                        print str(self.channel_creative_query_result[0][2])
                        creative_id = (str(self.channel_creative_query_result[0][2])+str(',')).replace(' ', '').split(',')
                        budget_campaign_id = self.channel_creative_query_result[0][3]

                        print creative_id
                        creative_id_tuple = tuple(creative_id)
                        print creative_id_tuple
                        get_creative_detail_query = 'SELECT * FROM FacebookCreative WHERE id IN ' + str(creative_id_tuple)
                        print get_creative_detail_query
                        self.get_creative_detail_query_result, self.error = db_obj.db_connect_query(get_creative_detail_query)

                    else:
                        print 'Error in fetching creative detail. This is blocker. Error: ',self.error, self.get_creative_detail_query_result
                        self.error = True

            else:
                print 'Error in fetching targeting parameters. This is blocker. Error: ', self.error, len(self.target_camp_query_result)
                self.error = True
        else:
            print 'Error in fetching the data for campaign is :', self.error, self.result
            self.error = True

        return self
