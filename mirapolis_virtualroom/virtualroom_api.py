from .base_api import BaseAPI
from hashlib import md5
import urllib.parse as urlparse
from urllib.parse import urlencode


class VirtualRoom(BaseAPI):
    def __init__(
            self,
            secret_key: str,
            app_id: str,
            base_link: str
    ):
        super().__init__(base_link)
        self.secret_key = secret_key
        self.app_id = app_id

        self.base_link = base_link
        self.base_params = {
            "appid": self.app_id,
            "secretkey": self.secret_key,
        }

    def make_params(
            self,
            path: str,
    ):
        url_parts = list(urlparse.urlparse(self.base_link + path))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(self.base_params)

        url_parts[4] = urlencode(query)

        legacy_url = urlparse.urlunparse(url_parts)

        md5_hash = md5(legacy_url.encode())
        sign = md5_hash.hexdigest().upper()

        params = {
            "appid": self.app_id,
            "sign": sign
        }
        return params

    async def get_measures(self):
        path = "/service/v2/measures"
        measures = await self.get_json(
            route=path,
            params=self.make_params(path)
        )
        return measures
