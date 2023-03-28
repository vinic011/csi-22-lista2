def new_list(strings):
    return list(filter(lambda x: x.isalnum(),strings))

print(new_list(["up","rfi15","%","*cdijo","cdspo"]))