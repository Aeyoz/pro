# ********************
# ORDENANDO POR EDADES
# ********************

# VERSION AYOZE
def run(people: list) -> list:
    speople = []
    for element in people:
        values = []
        for item in element.values():
            values.append(item)
        speople.append(values)
    speople = sorted(speople, key=lambda x: x[1])
    speople = [dict(age=age, name=name) for name, age in speople]
    return speople

# VERSION DIEGO
def run(people: list) -> list:
    person = [tuple(people.items()) for people in people]
    new_people = sorted(person, key=lambda x: x[1])
    speople = [dict(age=age, name=name) for name, age in new_people]
    return speople

# VERSION ABIAN
def run(people: list) -> list:
    speople = sorted(people, key=lambda x: x["age"])
    return speople


if __name__ == '__main__':
    run([{'name': 'DeRozan', 'age': 33}, {'name': 'Lonzo', 'age': 25}, {'name': 'Beverly', 'age': 34}, {'name': 'Dragic', 'age': 36}, {'name': 'Williams', 'age': 21}])
