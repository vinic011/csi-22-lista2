def mean_tuple(tuple_of_tuples):
    new_tup = tuple([sum(tup)/len(tup) for tup in tuple_of_tuples])
    return new_tup


print(mean_tuple(((1,2),(3,4))))
        
        
        