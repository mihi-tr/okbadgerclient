"""
A Client for the OKFN Badging service...
"""
import urllib2
import json
import hashlib
from urllib import quote


class Client():
    """ The client for Badging:
        
        Usage: 
            c=Client(url, id, api_key)
        """

    def __init__(self, url, id, api_key):
        self.url=url
        self.id=id
        self.api_key=api_key

    def issue(self, badge, recipient, evidence=None):
        """ Issue a badge to recipient """
        parameters={
            "id": str(self.id),
            "badge": badge,
            "recipient": recipient,
            "signature": hashlib.sha256(badge + recipient +
                                        self.api_key).hexdigest(),
            }
        if evidence:
            parameters['evidence']=evidence
        print parameters    
        parameters="&".join(("%s=%s" % (k, quote(v)) for (k, v) in
                                parameters.items()))
        url="%s/api/issue?%s" % (self.url, parameters)
        print url
        u=urllib2.urlopen(url)
        return json.load(u)

