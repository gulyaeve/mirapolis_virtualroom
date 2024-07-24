from .base_api import BaseAPI
from .models import Measure, Person


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
        if persons:
            return [Person(**person) for person in persons]

    async def get_person(self, person_id: int):
        person = await self.get_json(
            route=f"/service/v2/persons/{person_id}"
        )
        if person:
            return Person(**person)

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

    async def get_measure(self, measure_id: int):
        measure = await self.get_json(
            route=f"/service/v2/measures/{measure_id}"
        )
        if measure:
            return Measure(**measure)

    async def get_measures_info(self):
        measures_info = await self.get_json(
            route="/service/v2/measures/info"
        )
        return measures_info
