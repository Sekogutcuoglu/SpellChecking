import requests
import time
def grammar_check(text):
    url = 'https://languagetool.org/api/v2/check'

    payload = {
        'text': text,
        'language': 'en-US',  
        'enabledOnly': 'false',
        'enabledCategories': 'TYPOS,GrammarErrors',
    }
    start_time = time.time()  
    response = requests.post(url, data=payload)
    end_time = time.time()  
    json_response = response.json()
    errors = []
    for match in json_response['matches']:
        error = {
            'message': match['message'],
            'replacements': match['replacements'],
            'offset': match['offset'],
            'length': match['length'],
            'context': match['context']['text'],
        }
        errors.append(error)
    elapsed_time = end_time - start_time  
    return errors, elapsed_time
text = "he run."
errors, elapsed_time = grammar_check(text)
if errors:
    print("Dilbilgisi hataları:")
    for error in errors:
        print(f"- {error['message']}")
else:
    print("Dilbilgisi hatası bulunamadı.")
print("Elapsed Time:", elapsed_time, "seconds")
