def find_all(source, target):
    result = []
    index = 0
    while True:
        index = source.find(target, index)
        if index == -1:
            return
        else:
            yield index
            index +=1




