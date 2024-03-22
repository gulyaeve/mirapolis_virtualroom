from .base_api import BaseAPI


class VirtualRoom(BaseAPI):
    def __init__(
            self,
            token: str,
            app_id: str,
            base_link: str = ""
    ):
        super().__init__(base_link)
        self.headers = {
            "appid": app_id,
        }
