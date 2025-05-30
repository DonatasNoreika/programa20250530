import sqlalchemy
import django
import pandas
import pickle

from modelis import Klase

for x in range(5):
    print("Labas")

klase1 = Klase()
print(klase1)

with open("failas.pkl", 'wb') as file:
    pickle.dump(klase1, file)
