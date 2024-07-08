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
        path = "/service/v2/measures"
        measures = await self.get_json(
            route=path
        )
        return measures
