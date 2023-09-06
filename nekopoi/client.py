import httpx
from httpx import Response

from nekopoi.methods import Methods


class NekoPoi(Methods):
    NEKOPOI_URL: str = "https://nekopoi.care"
    BASE_URL: str = "https://cu8auck2lc.3z094n2681i06q8k14w31cu4q80d5p.com/330cceade91a6a9cd30fb8042222ed56/71b8acf33b508c7543592acd9d9eb70d"
    HEADERS = {
        "appbuildcode": "25032",
        "appsignature": "pOplm8IDEDGXN55IaYohQ8CzJFvWsfXyhGvwPRD9kWgzYSRuuvAOPfsE0AJbHVbAJyWGsGCNUIuQLJ7HbMbuFLMWwDgHNwxOrYMH",
        "token": "XbGSFkQsJYbFC6pcUMCFL4oNHULvHU7WdDAXYgpmqYlh7p5ZCQ4QZ13GDgowiOGvAejz9X5H6DYvEQBMrc3A17SO3qwLwVkbn6YY",
        "user-agent": "okhttp/4.9.0"
    }


    def __init__(self) -> None:
        self._client = httpx.AsyncClient()


    async def _request(self, endpoint: str = "/", *args, **kwargs) -> Response:
        async with self._client as client:
            res = await client.get(
                self.BASE_URL + endpoint,
                headers=self.HEADERS,
                *args,
                **kwargs
            )
            return res
