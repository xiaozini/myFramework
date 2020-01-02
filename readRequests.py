from common.readExcel import ReadExcel
import requests
import json

class SendRequests():

    def sendRequests(self,s,apiData):
        url = apiData['url']
        method = apiData['method']
        header = apiData['header']
        body = apiData['body']


        res = s.request(url = url,json = json.loads(body),headers=json.loads(header),method = method,verify=False)
        resultJson = res.json()
        print('返回数据为111:%s' % resultJson)
        return resultJson