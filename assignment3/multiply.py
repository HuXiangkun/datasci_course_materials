import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrixName = record[0]
    key = ()
    if matrixName == "a":
        for k in range(0,5):
            key = (record[1], k)
            mr.emit_intermediate(key, record)
    else:
        for i in range(0, 5):
            key = (i, record[2])
            mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    row = key[0]
    col = key[1]
    total = 0
    for v in list_of_values:
        if v[0] == "a":
            for bv in list_of_values:
                if bv[0] == "b" and bv[1] == v[2]:
                    total += bv[3] * v[3]
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
