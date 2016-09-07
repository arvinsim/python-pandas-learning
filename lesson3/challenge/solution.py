import pandas as pd

with open('poorly_delimited.txt', 'r') as f:
    contents = f.read()

splitted_lines = contents.split('\n')


data = []
for line in splitted_lines:
    result = line.partition(',')
    classification = result[0]
    example_text = result[2]
    data.append({
        'Classification': classification,
        'Text': example_text
    })

df = pd.DataFrame(data)
print(df)

