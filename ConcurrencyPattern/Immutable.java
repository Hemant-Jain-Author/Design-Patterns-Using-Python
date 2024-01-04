from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int
    gender: str


person = ImmutablePerson("John Doe", 30, "Male")
new_person = ImmutablePerson(person.name, person.age + 1, person.gender)
print(person)
print(new_person)

# person.age = 32
# dataclasses.FrozenInstanceError: cannot assign to field 'age'

