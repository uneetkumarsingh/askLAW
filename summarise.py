import requests
import json
import glob
from tqdm import tqdm
url = "https://api.endpoints.anyscale.com/v1/chat/completions"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer esecret_hanjm9lbkdr62f7csy3fem5fvy'
}

cases = glob.glob("/Users/uneet.singh1/Documents/learning_extra/vectara/vectara2/*.json")
for case in tqdm(sorted(cases)):
    case_json = json.load(open(case, "r"))
    case_text = case_json['section'][0]['text']
    payload = json.dumps({
    "model": "meta-llama/Llama-2-70b-chat-hf",
    "messages": [
        {
        "role": "system",
        "content": "You are legal expert who is an expert in Indian Jurisprudence. \
            You are aware how the Indian Court orders are structured. They often \
            quote a large part of previous judgements which need not deal with\
            the case in hand directly. The operative part of \
            the judgement is at the end of the judgement order. Your task is \
            to summarise the case by including the generic \
            case facts, provisions of the law/articles of constituion relied \
            by the court while arriving at the judgement and the final judgement."
        },
        {
        "role": "user",
        "content": f"Text of the Order starts from here: {case_text}"
        }
    ],
    "temperature": 0.2
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        metadata = json.loads(case_json['metadataJson'])
        metadata['summary'] = response.json()['choices'][0]['message']['content']
        case_json['metadataJson'] = json.dumps(metadata)
        json.dump(case_json, open(case.replace('vectara2', 'vectara3'), "w"))
