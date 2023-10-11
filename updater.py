import re
import json
import http.client


def get_version():
    client = http.client.HTTPSConnection("cu8auck2lc.3z094n2681i06q8k14w31cu4q80d5p.com")
    client.request(
        method="GET",
        url="/71b8acf33b508c7543592acd9d9eb70d/updateApp",
        headers={"user-agent": "okhttp/4.9.0"}
    )
    resp = client.getresponse()
    data = json.loads(resp.read().decode())
    return data["latestVersionCode"]

def update(version: str):
    with open("nekopoi/client.py", "r+") as f:
        text = f.read()
        f.seek(0)
        output_string = re.sub(r'"appbuildcode":\s+"(\d+)"', rf'"appbuildcode": "{version}"', text)
        f.write(output_string)


if __name__ == "__main__":
    version = get_version()
    update(version)
