import pandas as pd

# CSV and JSON
data = {
    "Name": ["Prajwal", "Charan"],
    "Age": [20, 22]
}

temp = pd.DataFrame(data)

temp.to_csv("Stud.csv", index=False)
temp.to_json("Stud.json", orient="records")

print(pd.read_csv("Stud.csv"))
print(pd.read_json("Stud.json"))


# Student Class
class Student:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print(self.name)


s1 = Student("Prajwal")
s1.hi()