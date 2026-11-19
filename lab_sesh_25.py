import pandas as pd

data = {
    "Name": ["Prajwal", "Charan"],
    "Age": [20, 22]
}

temp = pd.DataFrame(data)

temp.to_csv("Stud.csv", index=False)

temp = pd.read_csv("Stud.csv")
print(temp)

temp.to_json("Stud.json", orient="records")

temp = pd.read_json("Stud.json")
print(temp)