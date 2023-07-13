import typing as t
import json
from datetime import datetime
from pydantic import BaseModel


class Base(BaseModel):
    @staticmethod
    def default(obj: "BaseModel"):
        if isinstance(obj, datetime):
            return str(obj)

        return {
            "_": obj.__class__.__name__,
            **{
                attr: getattr(obj, attr)
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            }
        }


    def __repr__(self) -> str:
        return json.dumps(self, indent=4, default=Base.default, ensure_ascii=False)


    def __str__(self) -> str:
        return self.__repr__()


class Preview(Base):
    id: int
    type: t.Union[str, None] = None
    date: datetime
    title: str
    image: str
    slug: t.Union[str, None] = None
    description: t.Union[str, None] = None
    web_url: str


class RecentData(Base):
    category: str
    data: t.List[Preview]


class Recent(Base):
    carousel: t.List[Preview]
    posts: t.List[RecentData]


class Search(Base):
    total: int
    total_pages: int
    result: t.Union[t.List[Preview], None] = None


class Link(Base):
    name: t.Union[str, None] = None
    link: str


class Download(Base):
    type: str
    links: t.List[Link]


class Detail(Base):
    id: int
    date: datetime
    title: str
    slug: t.Union[str, None] = None
    content: t.Union[str, None] = None
    image: str
    series: t.Union[str, None] = None
    note: t.Union[str, None] = None
    stream: t.List[Link]
    download: t.List[Download]


class Genre(Base):
    term_id: int
    name: str
    slug: str


class InfoMeta(Base):
    aliases: str
    episode: int
    status: str
    durasi: str
    skor: float
    produser: str
    tayang: datetime
    genre: t.List[Genre]


class Series(Base):
    id: int
    date: datetime
    title: str
    image: str
    slug: t.Union[str, None] = None
    web_url: str
    info_meta: InfoMeta
    episode: t.List[Preview]


class ComingSoon(Base):
    result: t.Union[str, None] = None


class AuthorComment(Base):
    id: int
    username: str
    name: str
    avatar: str


class LikeComment(Base):
    likes: int
    dislikes: int


class MessageComment(Base):
    html: str
    raw: str


class Comment(Base):
    id: int
    author: AuthorComment
    like: LikeComment
    message: MessageComment
    created_at: datetime


class ThreadComment(Base):
  thread: int
  has_next: bool
  has_previous: bool
  total: int
  result: t.Union[t.List[Comment], None] = None
