from .base_api import BaseAPI
from .models import Measure


class VirtualRoom(BaseAPI):
    def __init__(
            self,
            base_link: str,
            secret_key: str,
            app_id: str
    ):
        super().__init__(
            base_link,
            secret_key,
            app_id
        )

    async def get_persons(self, limit: int = 200, offset: int = 0):
        persons = await self.get_json(
            route="/service/v2/persons",
            params={
                "limit": limit,
                "offset": offset,
            }
        )
        return persons

    async def get_measures(self, limit: int = 200, offset: int = 0):
        measures = await self.get_json(
            route="/service/v2/measures",
            params={
                "limit": limit,
                "offset": offset,
            }
        )
        if measures:
            return [Measure(**measure) for measure in measures]

    async def get_measures_info(self):
        measures_info = await self.get_json(
            route="/service/v2/measures/info"
        )
        return measures_info
