import requests
import time

from apex_dt.api.session import ApexAPISession
from apex_dt.api.exceptions import gen_api_error_response, MissingRequiredArgument
from apex_dt.config import API_REQ_TIMEOUT


class ApexAPIClient:
    """A class for getting content from ALS API endpoints.
    """

    def __init__(self):
        self.session = ApexAPISession()

    def _url(self, endpoint: str) -> str:
        return f'https://api.mozambiquehe.re/{endpoint}'

    def _request(self, endpoint: str, params: dict = None) -> dict:
        res = self.session.get(self._url(endpoint), params=params)
        res_content_type = res.headers['content-type'].strip()

        if res.status_code >= 400:
            gen_api_error_response(res)
        
        try:
            res_out = res.json()
        except requests.exceptions.JSONDecodeError:
            res_out = res.text
        
        time.sleep(API_REQ_TIMEOUT)

        return res_out

    def get_player_uid(self, player_name: str = None, platform: str = None) -> dict:
        if not player_name:
            raise MissingRequiredArgument('Please provide a player_name to "get_player_uid_console".')
        if not platform:
            raise MissingRequiredArgument('Please provide a platform to "get_player_uid_console".')

        params = {'player': player_name, 'platform': platform}
        return self._request('nametouid', params)

    def get_player_stats(
        self,
        player_name: str = None,
        platform: str = None,
        by: str = None,
        enable_clubs: bool = False,
        skip_rank: bool = False,
        merge: bool = False,
        remove_merged: bool = False) -> dict:
        
        if not player_name:
            raise MissingRequiredArgument('Please provide a player_name to "get_player_stats".')
        if not platform:
            raise MissingRequiredArgument('Please provide a platform to "get_player_stats".')
        if not by:
            raise MissingRequiredArgument('Please indicate to "get_player_stats" whether to search by "uid" or "name".')

        params = {'platform': platform}

        if by == 'uid':
            params.update({'uid': player_name})
        elif by == 'name':
            params.update({'player': player_name})
        else:
            raise InvalidArgument(f'Invalid option provided for "by": {by}. Allowed options are "uid" or "name".')
        
        if enable_clubs:
            params.update({'enableClubsBeta': True})
        if skip_rank:
            params.update({'skipRank': True})
        if merge:
            params.update({'merge': True})
        if remove_merged:
            params.update({'removeMerged': True})

        return self._request('bridge', params)

    def get_map_rotation(self) -> dict:
        params = {'version': '2'}
        return self._request('maprotation', params)

    def get_crafting_rotation(self) -> dict:
        return self._request('crafting')

    def get_predator_info(self) -> dict:
        return self._request('predator')

    def get_apex_news(self) -> dict:
        return self._request('news')

    def get_server_status(self) -> dict:
        return self._request('servers')

    def get_match_history_new(
        self,
        uid: str = None,
        mode: str = None,
        start: int = None,
        end: int = None,
        limit: int = None) -> dict:

        if not uid:
            raise MissingRequiredArgument('Please provide a player\'s UID to "get_match_history_new".')
        
        params = {'uid': uid}

        if mode:
            params.update({'mode': mode})
        if start:
            params.update({'start': start})
        if end:
            params.update({'end': end})
        if limit:
            params.update({'limit': limit})

        return self._request('games', params)
    
    def get_match_history_legacy(
        self,
        uid: str = None,
        platform: str = None,
        action: str = None) -> dict:
        
        if not uid:
            raise MissingRequiredArgument('Please provide a player\'s UID to "get_match_history_legacy".')
        if not platform:
            raise MissingRequiredArgument('Please provide a platform name to "get_match_history_legacy".')
        if not action:
            raise MissingRequiredArgument('Please provide an action to "get_match_history_legacy".')

        params = {
            'uid': uid,
            'platform': platform,
            'history': 1,
            'action': action
        }
        
        return self._request('bridge', params)
    
    def get_tracked_users(self, uid: str = None, platform: str = None) -> dict:
        params = {'history': 1, 'action': 'info'}
        return self._request('bridge', params)

    def add_tracked_player(self, uid: str = None, platform: str = None) -> dict:
        return self.get_match_history_legacy(uid, platform, 'add')

    def del_tracked_player(self, uid: str = None, platform: str = None) -> dict:
        return self.get_match_history_legacy(uid, platform, 'delete')


