from apex_dt.domain import api
from apex_dt.repository.base import BaseSQLiteRepository


class ApexNewsRepository(BaseSQLiteRepository[api.NewsItem]):
    pass


class ApexServerStatusRepository(BaseSQLiteRepository[api.ApexServer]):
    pass

