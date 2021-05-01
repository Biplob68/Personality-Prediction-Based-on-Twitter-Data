import base64
import requests
from enum import Enum
from urllib import parse
from typing import List, Optional, Tuple
from pykson import Pykson, JsonObject, StringField, IntegerField, DateTimeField, BooleanField, ListField, ObjectField, ObjectListField, EnumStringField


class TwitterUserUrlEntity(JsonObject):
    indices = ListField(item_type=int, serialized_name='indices', null=False)
    url = StringField(serialized_name='url', null=False)
    display_url = StringField(serialized_name='display_url', null=False)
    expanded_url = StringField(serialized_name='expanded_url', null=False)


class TwitterUserEntityItem(JsonObject):
    urls = ObjectListField(item_type=TwitterUserUrlEntity, serialized_name='urls', null=False)


class TwitterUserEntities(JsonObject):
    url = ObjectField(item_type=TwitterUserEntityItem, serialized_name='url', null=True)
    description = ObjectField(item_type=TwitterUserEntityItem, serialized_name='description', null=True)


class TwitterUser(JsonObject):
    user_id = IntegerField(serialized_name='id', null=False)
    user_id_str = StringField(serialized_name='id_str', null=False)
    name = StringField(serialized_name='name', null=False)
    screen_name = StringField(serialized_name='screen_name', null=False)
    location = StringField(serialized_name='location', null=True)
    url = StringField(serialized_name='url', null=True)
    description = StringField(serialized_name='description', null=True)
    protected = BooleanField(serialized_name='protected', null=False)
    verified = BooleanField(serialized_name='verified', null=False)
    followers_count = IntegerField(serialized_name='followers_count', null=False)
    followings_count = IntegerField(serialized_name='friends_count', null=False)
    listed_count = IntegerField(serialized_name='listed_count', null=False)
    favourites_count = IntegerField(serialized_name='favourites_count', null=False)
    statuses_count = IntegerField(serialized_name='statuses_count', null=False)
    created_at = DateTimeField(datetime_format='%a %b %d %H:%M:%S %z %Y',serialized_name='created_at', null=False)
    profile_banner_url = StringField(serialized_name='profile_banner_url', null=True)
    profile_image_url_https = StringField(serialized_name='profile_image_url_https', null=False)
    default_profile = BooleanField(serialized_name='default_profile', null=False)
    default_profile_image = BooleanField(serialized_name='default_profile_image', null=False)
    withheld_in_countries = ListField(item_type=str, serialized_name='withheld_in_countries', null=False)
    withheld_scope = StringField(serialized_name='withheld_scope', null=True)
    entities = ObjectField(item_type=TwitterUserEntities, serialized_name='entities', null=True)


class TweetHashTagEntity(JsonObject):
    indices = ListField(item_type=int, serialized_name='indices', null=False)
    text = StringField(serialized_name='text', null=False)


class TweetUrlEntityUnwound(JsonObject):
    url = StringField(serialized_name='url', null=False)
    status = IntegerField(serialized_name='status', null=False)
    title = StringField(serialized_name='title', null=False)
    description = StringField(serialized_name='description', null=False)


class TweetUrlEntity(JsonObject):
    indices = ListField(item_type=int, serialized_name='indices', null=False)
    url = StringField(serialized_name='url', null=False)
    display_url = StringField(serialized_name='display_url', null=False)
    expanded_url = StringField(serialized_name='expanded_url', null=False)
    enriched_info = ObjectField(item_type=TweetUrlEntityUnwound, serialized_name='unwound', null=True)


class TweetUserMentionEntity(JsonObject):
    indices = ListField(item_type=int, serialized_name='indices', null=False)
    name = StringField(serialized_name='name', null=False)
    screen_name = StringField(serialized_name='screen_name', null=False)
    user_id = IntegerField(serialized_name='id', null=False)
    user_id_str = StringField(serialized_name='id_str', null=False)


class TweetMediaEntitySizeResizeType(Enum):
    FIT = 'fit'
    CROP = 'crop'


class TweetMediaEntitySizeItem(JsonObject):
    height = IntegerField(serialized_name='h', null=False)
    width = IntegerField(serialized_name='w', null=False)
    resize = EnumStringField(enum=TweetMediaEntitySizeResizeType, serialized_name='resize', null=False)


class TweetMediaEntitySizes(JsonObject):
    thumb = ObjectField(item_type=TweetMediaEntitySizeItem, serialized_name='thumb', null=False)
    large = ObjectField(item_type=TweetMediaEntitySizeItem, serialized_name='large', null=False)
    medium = ObjectField(item_type=TweetMediaEntitySizeItem, serialized_name='medium', null=False)
    small = ObjectField(item_type=TweetMediaEntitySizeItem, serialized_name='small', null=False)


class TweetMediaEntityType(Enum):
    PHOTO = 'photo'
    VIDEO = 'video'


class TweetMediaEntity(JsonObject):
    indices = ListField(item_type=int, serialized_name='indices', null=False)
    display_url = StringField(serialized_name='display_url', null=False)
    expanded_url = StringField(serialized_name='expanded_url', null=False)
    media_id = IntegerField(serialized_name='id', null=False)
    media_id_str = StringField(serialized_name='id_str', null=False)
    media_url = StringField(serialized_name='media_url', null=False)
    media_url_https = StringField(serialized_name='media_url_https', null=False)
    media_type = EnumStringField(enum=TweetMediaEntityType,serialized_name='type', null=False)
    url = StringField(serialized_name='url', null=False)
    source_status_id = IntegerField(serialized_name='source_status_id', null=True)
    source_status_id_str = StringField(serialized_name='source_status_id_str', null=True)


class TweetSymbolEntity(JsonObject):
    indices = ListField(item_type=int, serialized_name='indices', null=False)
    text = StringField(serialized_name='text', null=False)


class TweetPollEntityOption(JsonObject):
    position = IntegerField(serialized_name='position', null=False)
    text = StringField(serialized_name='text', null=False)


class TweetPollEntity(JsonObject):
    options = ObjectListField(item_type=TweetPollEntityOption, serialized_name='options', null=False)
    end_datetime = DateTimeField(datetime_format='%a %b %d %H:%M:%S %z %Y', serialized_name='end_datetime', null=False)
    duration_minutes = IntegerField(serialized_name='duration_minutes', null=False)


class TweetEntities(JsonObject):
    hashtags = ObjectListField(item_type=TweetHashTagEntity, serialized_name='hashtags', null=False)
    urls = ObjectListField(item_type=TweetUrlEntity, serialized_name='urls', null=False)
    user_mentions = ObjectListField(item_type=TweetUserMentionEntity, serialized_name='user_mentions', null=False)
    media = ObjectListField(item_type=TweetMediaEntity, serialized_name='media', null=False)
    symbols = ObjectListField(item_type=TweetSymbolEntity, serialized_name='symbols', null=False)
    polls = ObjectListField(item_type=TweetSymbolEntity, serialized_name='polls', null=False)


class TweetObject(JsonObject):
    created_at = DateTimeField(datetime_format='%a %b %d %H:%M:%S %z %Y', serialized_name='created_at', null=False)  # Sat Apr 06 00:48:16 +0000 2019
    tweet_id = IntegerField(serialized_name='id', null=False)
    tweet_id_str = StringField(serialized_name='id_str', null=False)
    text = StringField(serialized_name='text', null=False)
    user = ObjectField(item_type=TwitterUser, serialized_name='user', null=False)


class UserData(JsonObject):
    created_at = DateTimeField(datetime_format='%a %b %d %H:%M:%S %z %Y',serialized_name='created_at', null=True)
    description = StringField(serialized_name='description', null=True)
    user_id = StringField(serialized_name='id', null=False)
    name = StringField(serialized_name='name', null=False)
    username = StringField(serialized_name='username', null=False)
    pinned_tweet_id = StringField(serialized_name='pinned_tweet_id', null=True)


class UserInfoResponse(JsonObject):
    data = ObjectListField(item_type=UserData, serialized_name='data', null=False)


class TwitterApp:

    def __init__(self, api_key: str, api_secret_key: str, app_name: str = 'default app', bearer_token: str = None, ):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.app_name = app_name
        self.pykson = Pykson()
        self.proxies = {'http': "socks5h://localhost:1080", 'https': "socks5h://localhost:1080"}
        # self.session = requests.Session()
        if bearer_token is None:
            self.token_type = None
            self.access_token = None
            if self.__authenticate() is False:
                raise Exception('Cannot authenticate to twitter api')
        else:
            self.token_type = 'bearer'
            self.access_token = bearer_token

    def __is_authenticated(self):
        return self.token_type is not None and self.access_token is not None

    def __get_basic_token(self) -> str:
        return base64.b64encode((parse.quote(self.api_key) + ':' + parse.quote(self.api_secret_key)).encode('utf-8')).decode('utf-8')
        # return str(base64.b64encode(bytes(parse.quote(self.api_key) + ':' + parse.quote(self.api_secret_key), "utf-8")))

    def __get_full_access_token(self):
        return '' + self.token_type + ' ' + self.access_token

    def __authenticate(self) -> bool:
        url = 'https://api.twitter.com/oauth2/token'
        basic_token = self.__get_basic_token()
        headers = {
            'User-Agent': self.app_name,
            'Accept-Encoding': 'gzip',
            'Authorization': 'Basic ' + basic_token,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        try:
            response = requests.post(url=url, headers=headers, data={'grant_type': 'client_credentials'}, timeout=60, proxies=self.proxies)
            if response.status_code != 200:
                raise Exception('Cannot authenticate (Erro ' + str(response.status_code) + ', ' + str(response.text) + ')')
            response_json = response.json()
            self.token_type = response_json['token_type']
            self.access_token = response_json['access_token']
            return True
        except Exception as ex:
            raise Exception('Cannot connect to twitter api' + str(ex))

    def invalidate_access_token(self) -> bool:
        if not self.__is_authenticated():
            return False
        url = 'https://api.twitter.com/oauth2/invalidate_token'
        basic_token = self.__get_basic_token()
        headers = {
            'User-Agent': self.app_name,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip',
            'Authorization': 'Basic ' + basic_token,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        try:
            response = requests.post(url=url, headers=headers, data={'access_token': self.__get_full_access_token()}, timeout=60, proxies=self.proxies)
            if response.status_code != 200:
                raise Exception('Cannot authenticate (Erro ' + str(response.status_code) + ', ' + str(response.text) + ')')
            response_json = response.json()
            self.token_type = response_json['token_type']
            self.access_token = response_json['access_token']
        except Exception as ex:
            raise Exception('Cannot connect to twitter api' + str(ex))

    def standard_search_tweets(self, keywords: List[str]) -> List[TweetObject]:
        if keywords is None or len(keywords) == 0:
            return []
        url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + '%20'.join([parse.quote(keyword) for keyword in keywords])
        headers = {
            'User-Agent': self.app_name,
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': self.__get_full_access_token(),
            # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        try:
            response = requests.get(url=url, headers=headers, timeout=60, proxies=self.proxies)
            if response.status_code != 200:
                raise Exception('Cannot authenticate (Erro ' + str(response.status_code) + ', ' + str(response.text) + ')')
            response_json = response.json()
            statuses = response_json['statuses']
            return self.pykson.from_json(data=statuses, cls=TweetObject, accept_unknown=True)
        except Exception as ex:
            raise Exception('Cannot connect to twitter api: ' + str(ex))

    def search_tweets_30_days(self, environment_name: str, query_items: List[str], max_results: Optional[int] = None) -> Tuple[str, List[TweetObject]]:
        url = 'https://api.twitter.com/1.1/tweets/search/30day/' + environment_name + '.json?lang:fa'
        headers = {
            'User-Agent': self.app_name,
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': self.__get_full_access_token(),
            # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        try:
            data = {
                'query': '('+' OR '.join([query_item for query_item in query_items]) + ')' if len(query_items) > 0 else query_items[0]
            }
            if max_results:
                data['maxResults'] = max_results
            response = requests.post(url=url, headers=headers, json=data, timeout=60, proxies=self.proxies)
            if response.status_code != 200:
                raise Exception('Cannot authenticate (Error ' + str(response.status_code) + ', ' + str(response.text) + ')')
            response_json = response.json()
            results = response_json['results']
            next_key = response_json.get('next', None)
            return next_key, self.pykson.from_json(data=results, cls=TweetObject, accept_unknown=True)
        except Exception as ex:
            raise Exception('Cannot connect to twitter api: ' + str(ex))

    def get_user_by_username(self, username: str) -> UserInfoResponse:
        url = 'https://api.twitter.com/labs/2/users/by?usernames=' + username
        headers = {
            'User-Agent': self.app_name,
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': self.__get_full_access_token(),
            # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        try:
            response = requests.get(url=url, headers=headers, timeout=60, proxies=self.proxies)
            response_json = response.json()
            return self.pykson.from_json(data=response_json, cls=UserInfoResponse, accept_unknown=True)
        except Exception as ex:
            raise Exception('Cannot connect to twitter api: ' + str(ex))

    def get_user_statuses_timeline(self, user_id: str, count: Optional[int] = 100, max_id: Optional[int] = None):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=' + user_id + '&count=200&include_rts=false'
        headers = {
            'User-Agent': self.app_name,
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': self.__get_full_access_token(),
            # 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        responses: List[TweetObject] = []
        try:
            while True:
                req_url = url
                if max_id is not None:
                    req_url = req_url + '&max_id=' + str(max_id)
                response = requests.get(url=req_url, headers=headers, timeout=60, proxies=self.proxies)
                if response.status_code != 200:
                    raise Exception('Cannot authenticate (Error ' + str(response.status_code) + ', ' + str(response.text) + ')')
                response_json = response.json()
                results = response_json
                res = self.pykson.from_json(data=results, cls=TweetObject, accept_unknown=True)
                if len(res) > 0 and len(responses) > 0:
                    res = res[1:]
                responses.extend(res)
                if len(res) == 0 or len(responses) >= count:
                    return responses
                elif len(res) > 0:
                    max_id = res[-1].tweet_id
                else:
                    raise Exception('Impossible Exception? ' + str(res))
        except Exception as ex:
            raise Exception('Cannot connect to twitter api: ' + str(ex))
