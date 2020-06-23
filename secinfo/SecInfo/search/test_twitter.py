import requests
import json
import re
import utils
proxies={
'http':'127.0.0.1:1087',
'https':'127.0.0.1:1087'
}

@utils.loadSearch("Twitter")
class TwitterSearch():
    def __init__(self):
        pass
    def _FetchToken(self):
        token_url = "https://mobile.twitter.com/search"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'
        }
        req = requests.get(token_url,verify=False,headers=headers,proxies=proxies)
        token = re.findall("gt=(\d+)",req.content)[0]
        return token
    def _FormatOutput(self,output):
        newoutput = []
        for item in output:
            newoutput.append({"time":output[item]["created_at"],"content":output[item]["full_text"]})
        return newoutput
    def Search(self,query_str):
        search_url = "https://api.twitter.com/2/search/adaptive.json"
        data = {
            "include_profile_interstitial_type" : "1",
            "include_blocking" : "1",
            "include_blocked_by" : "1",
            "include_followed_by" : "1",
            "include_want_retweets" : "1",
            "include_mute_edge" : "1",
            "include_can_dm" : "1",
            "include_can_media_tag" : "1",
            "skip_status" : "1",
            "cards_platform" : "Web-12",
            "include_cards" : "1",
            "include_ext_alt_text" : "true",
            "include_reply_count" : "1",
            "tweet_mode" : "extended",
            "include_entities" : "true",
            "include_user_entities" : "true",
            "include_ext_media_color" : "true",
            "include_ext_media_availability" : "true",
            "send_error_codes" : "true",
            "simple_quoted_tweet" : "true",
            "q" : query_str,
            "tweet_search_mode" : "live",
            "count" : "20",
            "query_source" : "typed_query",
            "pc" : "1",
            "spelling_corrections" : "1",
            "ext" : "mediaStats,highlightedLabel",
            "include_quote_count" : "true"
        }
        headers = {
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
            "x-guest-token": self._FetchToken()
        }
        req = requests.get(search_url,params=data,headers=headers,verify=False,proxies=proxies)
        try:
            req_json = json.loads(req.content)
            tweets = req_json["globalObjects"]["tweets"]
        except:
            raise Exception("[-] json loads failed or dict key missing , at class:TwitterSearch func:Search")
        # :created_at ,:full_text
        return self._FormatOutput(tweets)

if __name__ == '__main__':
    print(TwitterSearch().Search("cve and -"))