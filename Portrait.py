import itchat
import os
import PIL.Image as Image
from os import listdir
import math
import sys
sys.path.append('../')
import GetFriendsInfo

def getPortrait():

    friends = GetFriendsInfo.getFriendsInfo()

    w = open("Wechat_friends",'a',encoding='utf-8',errors='ignore')  # 将friends列表存下来，看看内容
    for i in friends:
        w.write(str(i))


    os.mkdir('head_portrait')  # 创建文件夹用于装载所有好友头像

    num = 0

    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        fileImage = open('head_portrait' + "/" + str(num) + ".jpg",'wb')#以二进制写入
        fileImage.write(img)
        fileImage.close()
        num += 1

    pics = listdir('head_portrait')    # 得到user目录下的所有文件，即各个好友头像

    numPic = len(pics)

    eachsize = int(math.sqrt(float(1000 * 1000) / numPic))    # 先圈定每个正方形小头像的边长，如果嫌小可以加大

    print("小正方形头像边长："+ str(eachsize))

    numCol = int(1000 / eachsize)#这是列数

    numRow = int(math.ceil(numPic * 1.0 / numCol)) #math.ceil()是向上取整的方法
    toImage = Image.new('RGB', (eachsize*numCol, eachsize*numRow))  # 这是一个空白的图像


    x = 0   # 小头像拼接时的左上角横坐标
    y = 0   # 小头像拼接时的左上角纵坐标


    for i in pics:
        try:
            #打开图片
            img = Image.open('head_portrait' + "/" + i)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            #缩小图片
            img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
            #拼接图片
            toImage.paste(img, (x * eachsize, y * eachsize))
            x += 1
            if x == numCol:
                x = 0
                y += 1

    toImage.save("total_portrait.jpg")
    itchat.send_image("total_portrait.jpg", 'filehelper')