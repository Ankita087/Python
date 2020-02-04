import requests
import jxmlease
import xmltodict
#####
#### documentaion  https://www.guru99.com/how-to-use-webpagetest-api.html
#### https://sites.google.com/a/webpagetest.org/docs/advanced-features/webpagetest-batch-processing-apis
#####
url = raw_input("Enter your url : ") 
api_key = raw_input("Enter your api key : ") 
#https://casengers.com
# api_key = "A.94513bd7eb254538801fe4d90384afaf"

response = requests.get('http://www.webpagetest.org/runtest.php?url='+url+'&run=1&f=xml&k='+api_key)
a=response.content
root = jxmlease.parse(a)
testid = root['response']['data']['testId'].get_cdata()

i="0"
while i=="0":
    res = requests.get('http://www.webpagetest.org/testStatus.php?f=xml&test='+testid)
    resparse = xmltodict.parse(res.content)#parse xml response
    statusCode = resparse['response']['statusCode']
    statusText = resparse['response']['statusText']
    if statusCode == '200' and statusText == 'Test Complete':
        i=1
    else:
        print statusText

res =requests.get('http://www.webpagetest.org/xmlResult/'+testid+'/')
with open('/home/ankita/Desktop/xmldata.xml', 'w+') as f:
    f.write(res.text)

