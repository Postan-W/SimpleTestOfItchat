import itchat
def getFriendsInfo():
    return itchat.get_friends(update=True)[0:]