import zipfile

zip_file = zipfile.ZipFile('data/tweets.zip')

keywords = ['weddie', 'weddies', 'voetbalmatch', 'voetbalpartij', 'potje voetbal',
            'voetbal duel', 'voetbal game', 'voetbal wedstrijden', 'voetbalspel']

days_count = {'mon': 0, 'tue': 0, 'wed': 0,
              'thu': 0, 'fri': 0, 'sat': 0, 'sun': 0}

for filename in zip_file.namelist():
    with zip_file.open(filename, 'r') as file:
        for line in file:
            line = line.decode("utf-8").strip().lower().replace(" ", "")
            day = line[-3:]
            if any(keyword.replace(" ", "") in line for keyword in keywords):
                days_count[day] += 1

print("Days count:", days_count)
