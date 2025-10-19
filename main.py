import json


# Variables to make it easy
MACHINE = "machine"
INPUTS = "inputs"
MAMYFLUX = "mamyflux"
TIME = "time"
OUTPUTS = "outputs"

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

read = open("Recipes.json", "r")
itemRaw = read.read()
read.close()
# store = open("NEW.json", "w")
itemData = json.loads(itemRaw)

test = list(str(itemData[19][OUTPUTS]).partition(";"))
test.remove(";")
test2 = []

for tmpData in test:
    tmpData = tmpData.replace(" x ", "!")
    test2.append(list(tmpData.split("!")))
for tmp in test2:
    for i in range(len(tmp)):
        if is_integer(tmp[i]):
            tmp[i] = int(tmp[i])
        if is_float(tmp[i]):
            tmp[i] = float(tmp[i])
print(test)
print(test2)

temp = input("What do you want to make? ")

for data in itemData:
    
    if temp in [data[OUTPUTS]]:
        for tmpData in test:

            tmpData = tmpData.replace(" x ", "!")
            test2.append(list(tmpData.split("!")))

            for tmp in test2:
                for i in range(len(tmp)):
                    if is_integer(tmp[i]):
                        tmp[i] = int(tmp[i])

                    if is_float(tmp[i]):
                        tmp[i] = float(tmp[i])