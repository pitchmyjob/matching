import os
import json
from matching_job import lambda_handler


os.environ["URL_ES"] = "https://search-matching-dev-qpd5t33mknnt2p6njeyah4kvku.eu-west-1.es.amazonaws.com/"


def page_test():

    payload = {"job" : 160, "page" : 1, "search" : "Mathieu"}

    ok = lambda_handler(payload, None)

    print(ok)



def scroll_test():
    payload = {"job" : 150, "scroll" : True}

    ok = lambda_handler(payload, None)

    res = []
    max = ok['max_score']


    res = res + ok['results']

    print(len(res))


    while len(ok['results']) > 0 and 1 == 2 :
        break
        res = res + ok['results']
        payload = {"job": 140, "scroll": True, "scroll_id": ok['scroll']}
        ok = lambda_handler(payload, None)




    #for k in res:
        #print( int(k["_score"] / max * 100) )






page_test()

#scroll_test()