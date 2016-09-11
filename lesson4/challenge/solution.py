import pandas as pd

url = 'http://www.softschools.com/social_studies/state_abbreviations/'
df = pd.read_html(url)
list_of_states = df[0][1][4:].tolist()
print(list_of_states)

