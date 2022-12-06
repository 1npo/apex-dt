__version__ = '0.0.1'


import pprint
from apex_dt.client import ApexAPIClient


pp = pprint.PrettyPrinter(indent=2)


def main():
    client = ApexAPIClient()
    #player = client.get_player_stats('oswaldisaacs', 'PC')
    #rotation = client.get_map_rotation()
    #predator = client.get_predator_info()
    #crafting = client.get_crafting_rotation()
    #news = client.get_apex_news()
    #uid = client.get_player_uid('oswaldisaacs', 'PC')
    #status = client.get_server_status()
    
    #uid = client.get_player_uid('oswaldisaacs', 'PC').get('uid')
    #new_history = client.get_match_history_new(uid, limit=3) 
    #old_history = client.get_match_history_legacy(uid, 'PC', 'info')
    
    #tracked_users = client.get_tracked_users()
    #new_player_uid = client.get_player_uid('HisWattsonTwitch', 'PC').get('uid')
    #new_tracked_player = client.add_tracked_player(new_player_uid, 'PC')
    #del_tracked_player = client.del_tracked_player(new_player_uid, 'PC')

    #hw_stats = client.get_player_stats('HisWattsonTwitch', 'PC', by='name')
    #pp.pprint(hw_stats)

