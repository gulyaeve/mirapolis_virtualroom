from .base_api import BaseAPI


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

    async def get_measures(self):
        measures = await self.get_json(
            route="/service/v2/measures"
        )
        return measures

    async def get_measures_info(self):
        measures_info = await self.get_json(
            route="/service/v2/measures/info"
        )
        return measures_info

