import http.client
import json
import sys

try:
    c = http.client.HTTPSConnection('api.coindesk.com')
    c.request('GET', '/v1/bpi/currentprice.json')
    resp = c.getresponse()
    if resp.status != 200:
        print('<ERROR>')
        sys.exit()
    print("1BTC={rate}€".format(rate=json.loads(resp.read())['bpi']['EUR']['rate'].split('.')[0]))
except:
    print('<ERROR>')
