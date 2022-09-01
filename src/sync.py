import requests,json

def syncer(file):
    r = requests.get('https://ricalveso.github.io/questions-api/'+file).json()
    """syncs local data with the API"""
    with open(file, 'w') as f:
        json.dump(r, f, indent=4)

def main():
    """fetches data from the API updating local data files"""
    r = requests.get('https://ricalveso.github.io/questions-api/data/data.json').json()
    with open('data/data.json', 'w') as f:
        json.dump(r, f, indent=4)
    for lang in r['Languages']:
        syncer(lang['Path'])
    for lang in r['Presets']:
        syncer(lang['Path'])

if __name__ == "__main__":
    main()
