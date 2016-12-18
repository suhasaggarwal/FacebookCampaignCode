import sys
from db_connect import *
fp = open('C:\Users\Suhas Aggarwal\Downloads\FacebookCampaignCode-master\FacebookCampaignCode-master\facebookads\myFiles\interest_segment.txt')
lines = fp.readlines()

db_obj = DBConnect()
search_query = 'SELECT * FROM category WHERE parent_id <> 0'
search_query_result, error = db_obj.db_connect_query(search_query)

if not error and len(search_query_result) > 0:
    for res in search_query_result:
        name = str(res[2]).lower()
        flag = 0
        line1 = ''
        for line in lines:
            if name in line:
                #print '1/'+str(res[0]) +','+ str(res[1]) +','+ res[2] +'/'+name +','+ line
                flag += 1
                line1 = line


        if flag == 1:
            print '1/' + str(res[0]) + ',' + str(res[1]) + ',' + res[2] + '/' + name + ',' + line1
        elif flag > 1:
            print str(flag)+'/' + str(res[0]) + ',' + str(res[1]) + ',' + res[2] + '/' + name + ',' + line1
        else:
            print '0/' + str(None) + ',' + str(None) + ',' + 'None' + '/' + name + ',' + 'None'