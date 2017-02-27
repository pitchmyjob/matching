import os
from matching_job import lambda_handler


os.environ["URL_ES"] = "https://search-matching-dev-qpd5t33mknnt2p6njeyah4kvku.eu-west-1.es.amazonaws.com/"


def page_test():
    payload = {"job" : 140, "page" : 1, "size" : 20}
    ok = lambda_handler(payload, None)

    print(ok['prev'])
    print(ok['next'])
    print(ok['pages'])
    print(ok['total'])
    print (len(ok['results']))



def scroll_test():
    payload = {"job" : 140, "scroll" : True}

    ok = lambda_handler(payload, None)

    res = []
    max = ok['max_score']

    print(len(ok['results']))
    print(ok)


    while len(ok['results']) > 0 and 1 == 2 :
        break
        res = res + ok['results']
        payload = {"job": 140, "scroll": True, "scroll_id": ok['scroll']}
        ok = lambda_handler(payload, None)




    #for k in res:
        #print( int(k["_score"] / max * 100) )





scroll_test()