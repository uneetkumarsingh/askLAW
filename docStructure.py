from config import config 
import json
from tqdm import tqdm
section_head_key= config["section_head_key"]
section_keys= config["section_keys"]
document_head_key= config["document_head_key"]
document_title_key= config["document_title_key"]
document_description_key= config["document_description_key"]
metadata_keys=config["metadata_keys"]
metadata_head_key=config["metadata_head_key"]


def convert_law_json_to_vectara_json(law_json):
    vectara_json = {}
    vectara_json[document_head_key] = law_json['id']
    vectara_json[document_title_key] = law_json['t']
    vectara_json[document_description_key] = ''
    vectara_json[section_head_key] = [{
        section_keys['title'] : law_json['id'],
        section_keys['text']: law_json['d']
    }]
    vectara_json[metadata_head_key] = json.dumps({
        metadata_keys['author']:law_json['s'],
        metadata_keys['url']:f'https://indiankanoon.org/doc/{vectara_json[document_head_key]}',
        'references':[f'https://indiankanoon.org/doc/{id}' for id in law_json['c']],
        'n_references':law_json['cl']
    })
    return vectara_json

def convert_law_list_to_vectara_json_list(law_json_list):
    vectara_json_list  = []
    for i, doc_law in enumerate(tqdm(law_json_list[:100])):
        vector_json = convert_law_json_to_vectara_json(doc_law)
        json.dump(vector_json, open(f"../vectara/{i}.json", "w"))
        vectara_json_list.append(vector_json)
    return vectara_json_list
