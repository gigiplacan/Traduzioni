import requests
import sys
import os
import json

# Carica l'API key da config.json
with open("config.json", "r") as token_file:
    token_data = json.load(token_file)

AUTH_KEY = token_data.get("deepL_api_key", "")

translate_url = "https://api-free.deepl.com/v2/document"
translate_status_url = "https://api-free.deepl.com/v2/document/{0}"
translate_download_url = "https://api-free.deepl.com/v2/document/{0}/result"

def translatedoc(path):
    translated_file_path = None  # Inizializza con None
    up_file = open(path, "rb")
    output_folder = os.path.dirname(path) 
    _params = {
        "source_lang": "EN",
        "auth_key": AUTH_KEY,
        "target_lang": "IT"
    }
    response = requests.post(translate_url, params=_params, files={"file": up_file})
    jdata = response.json()

    print("\n*****************************************************\n")
    print("[status] => python3 deepl.py status {0} {1}".format(jdata["document_id"],jdata["document_key"]))
    print("[download] => python3 deepl.py download {0} {1}".format(jdata["document_id"],jdata["document_key"]))
    print("\n*****************************************************\n")

    if 'document_id' in jdata and 'document_key' in jdata:
        translated_file_name, _ = os.path.splitext(os.path.basename(path))
        translated_file_path = os.path.join(output_folder, f"{translated_file_name}")
        
        with open(translated_file_path, "wb") as translated_file:
            downloadtranslation(jdata["document_id"], jdata["document_key"], translated_file_path)
    
    return translated_file_path  # Ora restituisce anche se le chiavi non sono presenti nella risposta


def docstatus(docid,dockey):
    _params = {
        "auth_key" : AUTH_KEY,
        "document_key" : dockey
    }
    response = requests.get(translate_status_url.format(docid),params=_params)
    print(response.text)

def downloadtranslation(docid, dockey, file_name):
    output_folder = os.path.dirname(os.path.abspath(__file__)) 
    file_name_without_extension, extension = os.path.splitext(os.path.basename(file_name))
    output_file_path = os.path.join(output_folder, f"{file_name_without_extension}.ini")
    
    _params = {
        "auth_key": AUTH_KEY,
        "document_key": dockey
    }
    
    response = requests.get(translate_download_url.format(docid), params=_params, allow_redirects=True)
    
    with open(output_file_path, "wb") as translated_file:
        translated_file.write(response.content)
    
    print(f"File tradotto salvato in: {output_file_path} \n")

action = sys.argv[1]
if action == "translate":
    translatedoc(sys.argv[2])
elif action == "status":
    docstatus(sys.argv[2],sys.argv[3])
elif action == "download":
    downloadtranslation(sys.argv[2],sys.argv[3])