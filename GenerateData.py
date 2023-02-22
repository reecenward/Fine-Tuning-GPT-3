import openai
import json

openai.api_key = "<YOUR-API-KEY>"

YEAR = ["2024", "2044", "2087", "2093", "2100"]
THING1 = ["Jobs", "Science", "Transportation", "Energy", "Homes"]
THING2 = ["Art", "Food", "Fun", "Human Life", "Love"]

scenarios = []

for year in YEAR:
    for thing1 in THING1:
        for thing2 in THING2:
            scenario = f"Its the year {year} and AI has taken over, tell me about how AI has affected {thing1} and {thing2}."
            response = openai.Completion.create(
              engine="text-davinci-003",
              prompt=scenario,
              temperature=1,
              max_tokens=150,
              n=1,
              stop=None,
              timeout=15
            ).choices[0].text.strip()
            data = {
              "scenario": scenario,
              "response": response
            }
            scenarios.append(data)

with open("scenarios.json", "w") as f:
    json.dump(scenarios, f)
