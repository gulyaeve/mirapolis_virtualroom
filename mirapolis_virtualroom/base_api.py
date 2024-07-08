import logging
from typing import Optional
import aiohttp
from hashlib import md5
import urllib.parse as urlparse
from urllib.parse import urlencode


class BaseAPI:
    def __init__(
            self,
            base_link: str,
            secret_key: str,
            app_id: str,
    ):
        self._link = base_link

        self.secret_key = secret_key
        self.app_id = app_id

        self.base_link = base_link
        self.base_params = {
            "appid": self.app_id,
            "secretkey": self.secret_key,
        }

        self.headers = {
            "Accept": "*/*",
        }

    def make_params(
            self,
            route: str,
    ):
        url_parts = list(urlparse.urlparse(self.base_link + route))
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

    async def get_json(self, route: str, params: Optional[dict] = None):
        if params is None:
            params = {}
        params.update(self.make_params(route))
        logging.info(f"GET JSON {self._link}{route} with {params=}")
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(
                    url=f"{self._link}{route}",
                    params=params,
                    verify_ssl=False,
                ) as resp:
                    logging.info(f"{resp=}")
                    if resp.ok:
                        logging.info(f"{resp.status=} {self._link}{route} {params=}")
                        return await resp.json()
                    else:
                        raise aiohttp.ClientError
        except aiohttp.ClientConnectionError:
            logging.warning(f"Api is unreachable {self._link}{route}")
        except Exception as e:
            logging.warning(f"Api is unreachable: {e}")

    # async def get_data(self, route: str, params: Optional[dict] = None):
    #     if params is None:
    #         params = {}
    #     params.update(self.make_params(route))
    #     logging.info(f"GET DATA {self._link}{route} with {params=}")
    #     try:
    #         async with aiohttp.ClientSession(headers=self.headers) as session:
    #             async with session.get(
    #                 url=f"{self._link}{route}",
    #                 params=params,
    #                 verify_ssl=False,
    #             ) as resp:
    #                 logging.info(f"{resp=}")
    #                 if resp.ok:
    #                     logging.info(f"{resp.status=} {self._link}{route}")
    #                     return await resp.read()
    #                 else:
    #                     raise aiohttp.ClientError
    #     except aiohttp.ClientConnectionError:
    #         logging.warning(f"Api is unreachable {self._link}{route}")
    #     except Exception as e:
    #         logging.warning(f"Api is unreachable: {e}")

    # async def post_json(self, route: str, data: Optional[dict] = None) -> dict:
    #     """
    #     Send post request to host
    #     :param route: request link
    #     :param data: json object to send
    #     :return: json object from host
    #     """
    #     headers = self.headers
    #     headers.update({"Content-Type": "application/x-www-form-urlencoded"})
    #     if data is None:
    #         data = {}
    #     logging.info(f"Sending post request to {self._link}{route} with data: {data}")
    #     try:
    #         async with aiohttp.ClientSession(headers=headers) as session:
    #             async with session.post(
    #                 f'{self._link}{route}',
    #                 data=data,
    #                 verify_ssl=False,
    #             ) as post:
    #                 logging.info(f"{post=}")
    #                 if post.ok:
    #                     logging.info(f"{post.status=} {self._link}{route} {data=}")
    #                     return await post.json()
    #                 else:
    #                     raise aiohttp.ClientError
    #     except aiohttp.ClientConnectionError:
    #         logging.warning(f"Api is unreachable {self._link}{route}")
    #     except Exception as e:
    #         logging.warning(f"Api is unreachable: {e}")
    #
    # async def put(self, route: str, data: Optional[dict] = None) -> aiohttp.ClientResponse:
    #     """
    #     Send put request to host
    #     :param route: request link
    #     :param data: json object to send
    #     :return: json object from host
    #     """
    #     headers = self.headers
    #     headers.update({"Content-Type": "application/x-www-form-urlencoded"})
    #     if data is None:
    #         data = {}
    #     logging.info(f"Sending PUT request to {self._link}{route} {data=}")
    #     try:
    #         async with aiohttp.ClientSession(headers=headers) as session:
    #             async with session.put(
    #                 f'{self._link}{route}',
    #                 data=data,
    #                 verify_ssl=False,
    #             ) as put:
    #                 logging.info(f"{put=}")
    #                 if put.ok:
    #                     logging.info(f"{put.status=} {self._link}{route} {data=}")
    #                     return put
    #                 else:
    #                     raise aiohttp.ClientError
    #     except aiohttp.ClientConnectionError:
    #         logging.warning(f"Api is unreachable {self._link}{route}")
    #     except Exception as e:
    #         logging.warning(f"Api is unreachable: {e}")
    #
    # async def delete(self, route: str, data: Optional[dict] = None) -> int:
    #     if data is None:
    #         data = {}
    #     logging.info(f"Sending DELETE request to {self._link}{route} with data={data}")
    #     try:
    #         async with aiohttp.ClientSession(headers=self.headers) as session:
    #             async with session.delete(
    #                 url=f"{self._link}{route}",
    #                 data=data,
    #                 verify_ssl=False,
    #             ) as resp:
    #                 logging.info(f"{resp=}")
    #                 if resp.ok:
    #                     logging.info(f"{resp.status=} {self._link}{route} {data=}")
    #                     return resp.status
    #                 else:
    #                     raise aiohttp.ClientError
    #     except aiohttp.ClientConnectionError:
    #         logging.warning(f"Api is unreachable {self._link}{route}")
    #     except Exception as e:
    #         logging.warning(f"Api is unreachable: {e}")


