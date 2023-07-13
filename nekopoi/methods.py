import typing as t

import nekopoi
from nekopoi import filters
from nekopoi.utils import slugified, slugified_web_url, parse_date
from nekopoi.models import (
    Recent, Search, Detail,
    Series, ComingSoon, ThreadComment
)


class Methods:
    async def get_recent(self: "nekopoi.NekoPoi") -> Recent:
        res = await self._request("/recent")
        data: dict = res.json()
        carousel = data["carousel"]
        posts = data["posts"]

        for c in carousel:
            c["web_url"] = slugified_web_url(c["title"], c["slug"])

        for post in posts:
            for d in post["data"]:
                d["web_url"] = slugified_web_url(d["title"], d["slug"])

        return Recent(**data)


    async def search(self: "nekopoi.NekoPoi", query: str, page: int = 1) -> Search:
        res = await self._request("/search", params={"q": query, "page": page})
        data: dict = res.json()
        data["total_pages"] = data.pop("totalPages")

        if data["result"]:
            for d in data["result"]:
                d["date"] = parse_date(d["date"])
                d["web_url"] = slugified_web_url(d['title'])

        return Search(**data)


    async def search_by_genre(
        self: "nekopoi.NekoPoi",
        term_id: t.Union[int, t.List[int]]
    ) -> Search:
        if isinstance(term_id, list):
            params = ""
            for term in term_id:
                params += f"term={term}&"
            params = params[0:-1]
        else:
            params = term_id
        res = await self._request("/searchByGenre", params={"term": term_id})
        data: dict = res.json()
        data["total_pages"] = data.pop("totalPages")

        for d in data["result"]:
            d["date"] = parse_date(d["date"])
            d["web_url"] = slugified_web_url(d['title'])

        return Search(**data)


    async def get_detail(
        self: "nekopoi.NekoPoi",
        id: int
    ) -> t.Union[Detail, Exception]:
        res = await self._request("/post", params={"id": id})
        data: dict = res.json()

        if data.get("error"):
            return Exception(data["error"])

        data["date"] = parse_date(data["date"])
        return Detail(**data)


    async def get_by_index(
        self: "nekopoi.NekoPoi",
        letter: str = "0-9",
        filter: str = filters.TYPE_HENTAI
    ) -> t.Union[Search, Exception]:
        res = await self._request(
            "/listall",
            params={"letter": letter, "type": filter, "page": 1}
        )
        data: dict = res.json()

        if data.get("error"):
            return Exception(data["error"])

        data["total_pages"] = data.pop("totalPages")

        for d in data["result"]:
            d["date"] = parse_date(d["date"])
            d["web_url"] = slugified_web_url(d['title'])

        return Search(**data)


    async def get_series(self: "nekopoi.NekoPoi", id: int) -> Series:
        res = await self._request("/series", params={"id": id})
        data: dict = res.json()

        data["date"] = parse_date(data["date"])
        data["slug"] = slugified(data["title"])
        data["web_url"] = slugified_web_url(data["title"], data["slug"])
        data["info_meta"]["tayang"] = parse_date(data["info_meta"]["tayang"])

        for eps in data["episode"]:
            eps["date"] = parse_date(eps["date"])
            eps["slug"] = slugified(eps["title"])
            eps["web_url"] = slugified_web_url(eps["title"], eps["slug"])

        return Series(**data)


    async def get_coming_soon(self: "nekopoi.NekoPoi") -> ComingSoon:
        res = await self._request("/comingsoon")
        data: dict = res.json()

        return ComingSoon(**data)


    async def get_comments(
        self: "nekopoi.NekoPoi",
        slug: str
    ) -> t.Union[ThreadComment, None]:
        res = await self._request("/service/disqus/post", params={"slug": slug})
        data: dict = res.json()

        if data.get("error"):
            return Exception(data["error"])

        data["has_next"] = data.pop("hasNext")
        data["has_previous"] = data.pop("hasPrev")

        for res in data["result"]:
            res["created_at"] = parse_date(res["created_at"])

        return ThreadComment(**data)
