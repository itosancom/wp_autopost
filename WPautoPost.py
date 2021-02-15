#coding=utf8
from jinja2 import Template
from wordpress_ctrl import WordPressCtrl,WordPressError
import os

wpctrl = WordPressCtrl('https://example.com', 'AutoPostTool', '****key*****')
picDir = os.getcwd() + "/"

files = os.listdir(picDir+i)
dirname = [f for f in files if os.path.isdir(os.path.join(picDir, f))]
img_url = []
imgTitle = []
print(dirname)

for data in dirname:
    # Upload Picture
    pathTmp = picDir + data
    picFile = os.listdir(pathTmp)
    print(picFile)

    for j in picFile:
        img_url = []
        picPath = picDir + i + '/' + j
        wpres = wpctrl.upload_png(item['picPath'])
        img_url.append(wpres['source_url'])

    for j in picFile:
        imgTitle = []
        tmptitle = picFile[j].split(".")
        imgTitle.append(tmptitle[0])

    
    # Post kiji
    html = """
    {% for item in img_url %}
    <!-- wp:image {"id":29,"sizeSlug":"large"} -->
    <figure class="wp-block-image size-large"><img src="{{ img_url | e }}" alt="" class="wp-image-29"/></figure>
    <!-- /wp:image -->

    <!-- wp:heading -->
    <h2>{{ imgTitle | e }}</h2>
    <!-- /wp:heading -->
    {% endfor %}
    """
    # 新規投稿
    wpres = wpctrl.add_post(i, Template(html).render(data), [1], [3])
    print("POST!:"+ wpres['id'])