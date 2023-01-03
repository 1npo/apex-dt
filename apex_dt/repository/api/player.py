from apex_dt.domain import api
from apex_dt.repository.base import BaseSQLiteRepository


class PlayerRepository(BaseSQLiteRepository[api.ApexLegendsPlayer]):
    pass


