import csv

def dedupe_headlines(headlines): 
  deduped_headlines = []
  preexisting_headlines = set()

  with open("headlines.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file, delimiter="\n")

    for row in reader:
      headline = row[0]
      preexisting_headlines.add(headline)

  for headline in headlines:
    if headline not in preexisting_headlines:
      deduped_headlines.append(headline)

  return deduped_headlines