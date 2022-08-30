import json
from typing import Any

import httpx

GET_MEMES_URL = "https://api.imgflip.com/get_memes"


def fetch_data(num_of_results: int) -> Any:
    request = httpx.get(GET_MEMES_URL)
    if request.status_code != httpx.codes.OK:
        raise Exception("Failed to process request")
    else:
        data = json.loads(request.text).get("data")
        data_snap = data.get("memes")[:num_of_results]

        remove_keys_list = ["width", "height", "box_count"]
        data_snap = [{key: i[key] for key in i if key not in remove_keys_list} for i in data_snap]

    return data_snap
