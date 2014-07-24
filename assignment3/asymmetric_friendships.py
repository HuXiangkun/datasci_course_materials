import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    key = ()
    if personA > personB:
        key = (personA, personB)
    else:
        key = (personB, personA)
    mr.emit_intermediate(key, personB)

def reducer(key, list_of_values):
    person1 = key[0]
    person2 = key[1]
    if person1 not in list_of_values or person2 not in list_of_values:
        mr.emit((person1, person2))
        mr.emit((person2, person1))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
