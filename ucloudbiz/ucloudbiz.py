import urllib2
import urllib
import hashlib
import hmac
import base64
import urlparse
import linecache

def get_sig_request(request, secretkey, baseurl):
    request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k]).replace('+','%20').lower()])for k in sorted(request.iterkeys())])
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    return baseurl+request_str+'&signature='+sig

