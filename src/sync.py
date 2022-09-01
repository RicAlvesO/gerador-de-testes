import requests,json

def syncer(file):
    r = requests.get('https://ricalveso.github.io/questions-api/'+file).json()
    """syncs local data with the API"""
    with open(file, 'w') as f:
        json.dump(r, f, indent=4)

def main():
    """fetches data from the API updating local data files"""
    print('Downloading Data...', end='')
    r = requests.get('https://ricalveso.github.io/questions-api/data/data.json').json()
    with open('data/data.json', 'w') as f:
        json.dump(r, f, indent=4)
    print('DONE\n\nDownloading Languages:')
    for lang in r['Languages']:
        print(lang['Name']+'...', end='')
        syncer(lang['Path'])
        print('DONE')
    print('\nDownloading Presets:')
    for pres in r['Presets']:
        print(pres['Name']+'...', end='')
        syncer(pres['Path'])
        print('DONE')
    print('\nFinished')

if __name__ == "__main__":
    print('\033c')
    main()
