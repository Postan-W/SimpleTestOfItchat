import GetFriendsInfo
import re
import numpy
import itchat
import jieba
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import ImageColorGenerator
from wordcloud import WordCloud
def getSignature():
    signature = ''
    friends = GetFriendsInfo.getFriendsInfo()
    siglist = []
    for friend in friends:
        signature = friend['Signature']
        if(signature != None):
            signature = signature.strip().replace('span','').replace('emoji','').replace('class','')
            signature = re.sub(r'1f(\d.+)', '', signature)
            siglist.append(signature)
    wordlist = jieba.cut(''.join(siglist),cut_all=False)
    word_list_split = ''.join(wordlist)
    print(word_list_split)
    back_coloring = numpy.array(Image.open('timg.jpg'))
    wordcloud = WordCloud(
        font_path='STXINGKA.TTF',
        background_color="white",
        max_words=5000,
        mask=back_coloring,
        max_font_size=100,
        min_font_size=20,
        random_state=20,
        width=1000,
        height=1000,
        margin=10
    )
    wordcloud.generate(word_list_split)

    # image_color = ImageColorGenerator(back_coloring)
    # wordcloud.recolor(color_func=image_color)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('signatures.jpg')
    itchat.send_image("signatures.jpg", 'filehelper')

