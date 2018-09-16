import csv
import GetFriendsInfo
import itchat
def getLocation():
    friends = GetFriendsInfo.getFriendsInfo()
    headers = ['NickName','Province','City']
    with open('location.csv','w',encoding='utf-8',newline='',) as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName']
           row['Province'] = friend['Province']
           row['City'] = friend['City']
           writer.writerow(row)
    itchat.send_image("location.jpg", 'filehelper')