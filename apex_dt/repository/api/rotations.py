from apex_dt.domain import api
from apex_dt.repository.base import BaseSQLiteRepository


class MapRotationRepository(BaseSQLiteRepository[api.MapRotation]):
    pass


class CraftingRotationRepository(BaseSQLiteRepository[api.CraftingRotation]):
    pass


