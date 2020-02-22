import time
import requests
import json


def _main_iter(data: dict):
    response = requests.get(
        F'https://{data["server_address"]}/{data["secret_key"]}')

    if not response.content:
        return

    server_response = json.loads(response.content)
    print("dfssssssss", server_response)
    msg = F"Request: http://{server_response.get('req')}"
    if server_response.get("req", '').split('/')[0] not in data["possible"]:
        print(F"{msg}: FAILED")
        return
    requests.get(F"http://{server_response.get('req')}")
    print(F"{msg}: OK")


def _load_config():
    with open('config.json') as json_file:
        data = json.load(json_file)
    msg = []
    for required_key in ["interval", "secret_key", "server_address", "possible"]:
        if required_key not in data.keys():
            msg.append(F"The is no {required_key} in config")
    if msg:
        raise Exception(str(msg))
    return data


def main():
    data = _load_config()
    while True:
        _main_iter(data)
        time.sleep(data["interval"])
    pass


if __name__ == "__main__":
    main()
