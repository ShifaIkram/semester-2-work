# Task#3
# UDF for two Tuple Intersection

# User Defined Function
def tuple_intersection(t1, t2):
    result = tuple(x for x in t1 if x in t2)   # tuple comprehension
    return result


tuple1 = (1, 2, 3, 4, 7)
tuple2 = (3, 4, 3, 7, 6)

print("Intersection:",tuple_intersection(tuple1, tuple2))

