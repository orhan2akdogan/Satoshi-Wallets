#!pip install requests
import requests

def get_block_data(block_height):
    url = f"https://blockchain.info/block-height/{block_height}?format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["blocks"][0]
    else:
        print(f"Hata: {response.status_code}")
        return None

def get_block_info(start_block=0, end_block=100):
    block_data = []
    for height in range(start_block, end_block):
        block = get_block_data(height)
        if block:
            block_info = {"block": height, "addresses": []}
            for tx in block["tx"]:
                for out in tx["out"]:
                    if "addr" in out and "script" in out:
                        address_info = {
                            "address": out["addr"],
                            "public_key": out["script"]
                        }
                        block_info["addresses"].append(address_info)
            block_data.append(block_info)
    return block_data

block_info_list = get_block_info(1, 100) # max 4800

for block_info in block_info_list:
    for address in block_info["addresses"]:
        print(f"{block_info['block']}\t" + f"{address['address']}\t"+ f"{address['public_key']}")


