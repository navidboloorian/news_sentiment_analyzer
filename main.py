import os
import importlib
from sentiment_analyzer import analyze_sentiment
from subject_determiner import determine_subject
from headline_deduper import dedupe_headlines
from datetime import datetime
from subprocess import Popen, PIPE

def main():
  for file in os.listdir("scrapers/"):
    if file.endswith(".py") and file != "__init__.py":
      module_name = file[:-3]
      module_path = f"scrapers.{module_name}"

      try:
        module = importlib.import_module(module_path)

        if hasattr(module, "get_headlines"):
          get_headlines = getattr(module, "get_headlines")
          headlines = dedupe_headlines(get_headlines())
          subjects = determine_subject(headlines)

          pruned_headlines = []
          pruned_subjects = []

          for i in range(len(headlines)):
            if subjects[i] != "N/A":
              pruned_headlines.append(headlines[i])
              pruned_subjects.append(subjects[i])

          headlines = pruned_headlines
          subjects = pruned_subjects
          sentiments = analyze_sentiment(headlines)

          with open("headlines.csv", "a", encoding="utf-8") as file:
            for headline in headlines:
              line = f"{headline}\n"
              file.write(line)

          with open("data.csv", "a", encoding="utf-8") as file:
            for i in range(len(headlines)):
              line = f"{module_name},{subjects[i]},\"{headlines[i]}\",{sentiments[i]},{datetime.today().strftime('%Y-%m-%d')}\n"
              file.write(line)

      except Exception as e:
        print(f"There was an error: {e}")

      daily_commit = Popen(
        "daily_update.bat", 
        shell=True,
        stdout=PIPE,
        stderr=PIPE
      )

      # _, stderr = daily_commit.communicate()

      with open("log.txt", "a", encoding="utf-8") as file:
        file.write(stderr)

if __name__ == "__main__":
  main() 