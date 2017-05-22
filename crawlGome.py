#-*-encoding:utf-8-*-
import urllib
import pymongo
import json

def get_html(line,db,url):
    try:
        html = urllib.urlopen(url)
        html_source = html.read()
        res_html = html_source[35:len(html_source)-2]
        html_json = json.loads(res_html)
        answers = []
        for i in range(0,len(html_json['robot']['list']['item'])):
            answers.append(html_json['robot']['list']['item'][i]['answer'])
        document = ({'question':line,'answer':answers})
        db_count = db.gomeIntQA.count()
        if db_count == 0:
            db.gomeIntQA.insert(document)
        else:
            detail_count = db.gomeIntQA.find({'question':line}).count()
            if detail_count == 0:
                db.gomeIntQA.insert(document)
    except:
        pass


if __name__ == '__main__':
    try:
        conn = pymongo.Connection('10.58.222.112',19753)
        db = conn.test
    except:
        pass
    file = open('C:\Users\huangyong\Desktop\\111.txt')
    lines = file.readlines()
    for line in lines:
        #print line
        url = 'http://chatrobot.gome.com.cn/robot/common?cmd=chatting&callbackParam=Live800Robot.inner.successCallback&uniqueKey=204447E512AC350D2957BFA8C6A5D6D9_1488782390761_3&question='+str(line)+'&_=1488782426680'
        get_html(line,db,url)
