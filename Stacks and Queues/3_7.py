class Animal(object):
    def __init__(self):
        self._ticket = 0

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        self._ticket = value


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()


class AnimalQueue(object):
    def __init__(self):
        self._storage = []

    def push(self, animal):
        self._storage.append(animal)

    def pop(self):
        return self._storage.pop()

    def peep(self):
        return self._storage[-1]


class AnimalShelter(object):
    def __init__(self):
        self._dogShelter = AnimalQueue()
        self._catShelter = AnimalQueue()
        self._ticketGenerator = 0

    def _getNewTicket(self):
        self._ticketGenerator += 1
        return self._ticketGenerator

    def enqueue(self, animal):
        animal.ticket = self._getNewTicket()
        if isinstance(animal, Dog):
            self._dogShelter.push(animal)
        elif isinstance(animal, Cat):
            self._catShelter.push(animal)
        else:
            raise ValueError()

    def dequeueDog(self):
        return self._dogShelter.pop()

    def dequeueCat(self):
        return self._catShelter.pop()

    def dequeueAny(self):
        if self._dogShelter.peep().ticket > self._catShelter.peep().ticket:
            return self.dequeueCat()
        else:
            return self.dequeueDog()