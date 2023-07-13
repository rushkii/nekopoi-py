# nekopoi-py
A NekoPoi direct API without scraping written in Python.

### Installation
```sh
git clone https://github.com/rushkii/nekopoi-py.git
cd nekopoi-py
pip install -r requirements.txt
```

### Example
- Get Recent Hentai
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.get_recent()
    print(result)

asyncio.run(main())
```
- Search Hentai
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.search(query="loli", page=1)
    print(result)

asyncio.run(main())
```
- Search Hentai By Genre
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.search_by_genre(term_id=51)

    # multiple genre selection
    # result = await client.search_by_genre(term_id=[544, 36])

    print(result)

asyncio.run(main())
```
- Hentai Detail
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.get_detail(id=19169)
    print(result)

asyncio.run(main())
```
- Get Hentai By Index
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi, filters


async def main():
    client = NekoPoi()
    result = await client.get_by_index(letter="0-9", filter=filters.TYPE_3D_HENTAI) # default: letter="0-9", filter=filters.TYPE_HENTAI
    print(result)

asyncio.run(main())
```
- Get Hentai Series
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.get_series(id=9690)
    print(result)

asyncio.run(main())
```
- Get Hentai Coming Soon or Schedule
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.get_coming_soon()
    # sadly, the result is an HTML element
    print(result)

asyncio.run(main())
```
- Get Comment Discussion From Specific Hentai
```py
# main.py (root directory)
import asyncio
from nekopoi import NekoPoi


async def main():
    client = NekoPoi()
    result = await client.get_comments(slug="3dmotion-anime-mikopako-sex-life-with-fluffy-loli")
    # sadly, the result is an HTML element
    print(result)

asyncio.run(main())
```

### FAQ
Q: How do you get their API?<br>
A: Simple, through reverse engineering concepts.<br><br>
Q: How do you do that?<br>
A: Sorry, it's secret 😅.<br><br>
Q: Is the headers affecting my account?<br>
A: So far, no, NekoPoi does not use an account login except for chat using Chatango and the headers is not include for Chatango. Any headers are the responsibility of the NekoPoi developer.

### LICENSE
[MIT License](LICENSE)

### DISCLAIMER
I'm not a NekoPoi developer nor the author, any copyrights goes to NekoPoi themselves, I just creating the API wrapper.
