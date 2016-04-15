import Queue

class DogCatNode(object):
    ANIMAL_TYPES = ['dog', 'cat']
    def __init__(self, index, animal_type='dog'):
        self.validate_type(animal_type)
        self.index = index
        self.type = animal_type
    def validate_type(self, animal_type):
        if not animal_type in self.ANIMAL_TYPES:
            raise Exception('invalid type')

class DogCatQueue(object):
    def __init__(self):
        self.index = 0
        self.dog_queue = Queue.Queue()
        self.cat_queue = Queue.Queue()

    def get_index(self):
        self.index += 1
        return self.index

    def enqueue(self, animal_type):
        node = DogCatNode(self.get_index(), animal_type)
        if animal_type == 'dog':
            self.dog_queue.put(node)
        elif animal_type == 'cat':
            self.cat_queue.put(node)


    def dequeueAny(self):
        if self.dog_queue.queue[0] < self.cat_queue.queue[0]:
            return self.dog_queue.get()
        else:
            return self.cat_queue.get()

    def dequeueDog(self):
        return self.dog_queue.get()

    def dequeueCat(self):
        return self.cat_queue.get()

    def __str__(self):
        dog_list = []
        for d in list(self.dog_queue.queue):
            dog_list.append(d.index)
        cat_list = []
        for c in list(self.cat_queue.queue):
            cat_list.append(c.index)
        res = "dog queue: " + str(dog_list) + "\n"
        res += "cat queue: " + str(cat_list)
        return res


def test():
    dcq = DogCatQueue()
    dcq.enqueue('dog')
    dcq.enqueue('cat')
    dcq.enqueue('dog')
    dcq.enqueue('dog')
    dcq.enqueue('cat')
    print dcq
    dcq.dequeueAny()
    print dcq
    dcq.dequeueAny()
    print dcq
    dcq.dequeueAny()
    print dcq
    dcq.dequeueDog()
    dcq.dequeueCat()
    print dcq

if __name__ == "__main__":
    test()
