import docStructure
import json
import glob
import requests
from dotenv import dotenv_values
from tqdm import tqdm
corpus_jsons = sorted(glob.glob("/Users/uneet.singh1/Documents/learning_extra/vectara/small_law/*/*.json"))
config = dotenv_values(".env")
customer_id = config.get('CUSTOMER_ID')
corpus_id = config.get('CORPUS_ID')
x_api_key = config.get('X_API_KEY')
url = f"https://api.vectara.io/v1/upload?c={customer_id}&o={corpus_id}&d=true"

payload = {}
headers = {
  'Accept': 'application/json',
  'x-api-key': x_api_key
}

for i, doc_url in tqdm(enumerate(corpus_jsons[:300])):
    doc = json.load(open(doc_url, "r"))
    vectar_json_list = docStructure.convert_law_list_to_vectara_json_list(doc, i)
    # assert len(doc) == len(vectar_json_list)
    # for temp in tqdm(vectar_json_list):
    #     json.dump(temp, open(f"temp.json", "w"))
    #     files=[
    #         ('file',('file',open('temp.json','rb'),'application/octet-stream'))
    #         ]
    #     response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #     if response.status_code !=200:
    #         print(response, response.text)
    #         break