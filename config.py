config = {"document_head_key" : 'documentId',
"document_title_key" : 'title' ,
"document_description_key" : 'description',
"metadata_head_key" : 'metadataJson',
"section_head_key" : 'section', #List
"section_keys" : {'title':'title',
                'text': 'text', 
                 'metadataJson': 'metadataJson'},
"metadata_keys" : {'date': 'date', 
                 'url': 'url', 
                 'ts_create': 'ts_create', #a creation date in epoch seconds
                 'author': 'author' #string or an array of strings
                 },
# 't', 's', 'id', 'd', 'c', 'cl', 'b'
"kanoon_to_vectara" : {
    "t":'title',
    "id":'documentId',
    's':'court',
    'd':'text',
    'c':'ref_id',
    'cl':'n_ref_ids'
}}