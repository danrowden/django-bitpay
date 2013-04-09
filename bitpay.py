#!/usr/bin/env python

# Bitpay's API for use in a Django project

import requests, urllib2, base64, json

from django.conf import settings

class Bitpay:
    
    API_ENDPOINT = ""
    API_KEY = ""
    
    def __init__(self):
        self.API_ENDPOINT = "https://bitpay.com/api/invoice"
        self.API_KEY = settings.BITPAY_API_KEY
        
    # API METHOD
    def CreateInvoice(self, amount, currency, return_url, item_desc, **kwargs):
        params = {
            'price' : amount,
            'currency': currency,
            'redirectURL' : return_url,
            'itemDesc': item_desc
        }
        params.update(kwargs)
        post = json.dumps(params)
        
        # help from https://github.com/bitpay/php-client/blob/master/bp_lib.php        
        req = urllib2.Request(self.API_ENDPOINT)
        base64string = base64.encodestring(self.API_KEY).replace('\n', '')
        req.add_header("Authorization", "Basic %s" % base64string)
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", len(post))

        json_response = urllib2.urlopen(req, post)
        response = json.load(json_response)
        
        return response