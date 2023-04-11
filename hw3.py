from hw2 import logger

@logger('flat_generator.log')
def flat_generator(list_of_lists):

    for item in list_of_lists:
        if isinstance(item, (list, tuple)):
            for i in flat_generator(item):
                yield i
        else:
            yield item

list1 = [
    1,
    [2, [3, 4, 5], 6],
    7,
    [[8, 9, [10, 11]], 12],
    13,
    [14, ],
    15,
    [],
    16
]

if __name__ == '__main__':
    
    flat_generator(list1)
