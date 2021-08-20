import base64
import requests
import json
import time

from . import config
from .cachehandler import CacheHandler

class BillToBoxAPI:

    def __init__(self, clientId, clientSecret, demo=False):

        self.clientId = clientId
        self.clientSecret = clientSecret
        self.demo = demo
        self.headers = {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
        }

        self.baseUrl = config.DEMO_URL if demo else config.BASE_URL
        self.cacheHandler = CacheHandler()
    
    def setTokenHeader(self, token):
        bearerStr = 'Bearer {token}'.format(token=token)
        self.headers.update({'Authorization' : bearerStr})

    def checkHeaderTokens(self):

        # If no authorization header is found, we need to include the token
        if 'Authorization' not in self.headers:
            
            # Check if we have a token stored in cache, if not, acquire one
            # If we do, set it in the header
            cachedAccessToken = self.cacheHandler.getCache(self.clientId)
            if cachedAccessToken is None:
                self.acquireAccessToken()
            else:
                self.setTokenHeader(cachedAccessToken)

    def acquireAccessToken(self):

        data = { 'grant_type' : 'client_credentials' }
        req = requests.post(config.ACCESS_TOKEN_URL, data=data, allow_redirects=False, auth=(self.clientId, self.clientSecret))

        status = req.status_code
        response = req.json()

        if status == 200:
            accessToken = response['access_token']
            self.cacheHandler.setCache(self.clientId, accessToken)
            self.setTokenHeader(accessToken)

            return accessToken

    def doRequest(self, method, url, data=None, headers=None):

        if headers:
            mergedHeaders = self.headers
            mergedHeaders.update(headers)
            headers = mergedHeaders
        else: headers = self.headers

        reqUrl = '{base}/{url}'.format(base=self.baseUrl, url=url)

        if method == 'GET':
            response = requests.get(reqUrl, params=data, headers=headers)
        elif method == 'POST':
            response = requests.post(reqUrl, data=json.dumps(data), headers=headers)
        elif method == 'PUT':
            response = requests.put(reqUrl, data=json.dumps(data), headers=headers)
        
        return response

    def request(self, method, url, data=None, headers=None):

        self.checkHeaderTokens()
        response = self.doRequest(method, url, data, headers)

        if 'json' in response.headers['Content-Type']:
            respContent = response.json()
        elif 'pdf' in response.headers['Content-Type']:
            respContent = response.content
        
        return response.status_code, response.headers, respContent
    
    def get(self, url, data=None, headers=None):
        status, headers, response = self.request('GET', url, data, headers)
        return status, headers, response
    
    def post(self, url, data=None, headers=None):
        status, headers, response = self.request('POST', url, data, headers)
        return status, headers, response
    
    def put(self, url, data=None, headers=None):
        status, headers, response = self.request('PUT', url, data, headers)
        return status, headers, response