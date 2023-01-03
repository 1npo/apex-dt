import requests

from apex_dt.main import __version__
from apex_dt.config import USER_API_KEY


class ApexAPISession(requests.Session):
    def __init__(self):
        super().__init__()
        self.headers.update({
            'User-Agent': f'apex-dt v{__version__} by 1npo <https://github.com/1npo/apex-dt>',
            'Authorization': USER_API_KEY,
            })

