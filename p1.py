def remove_empty(tup_list):
    no_empty_list = list(filter(lambda x: len(x)>0,tup_list))
    return no_empty_list

print(remove_empty([(),(1,2,3),(12,45),()]))
