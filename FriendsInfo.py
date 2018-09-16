#用于获取好友的性别，签名，地域等等信息
import GetFriendsinfo
def getInfo(var):
    variable = []
    friends = GetFriendsinfo.getFriendsInfo()
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
NickName  = getInfo('NickName')
Sex = getInfo('Sex')
Province = getInfo('Province')
City = getInfo('City')
Signature = getInfo('Signature')

from pandas import DataFrame
data = {'NickName':NickName,'Sex':Sex,'City':City,'Province':Province,'Signature':Signature}
frame = DataFrame(data)
frame.to_csv('detailData.cvs',index=True)
