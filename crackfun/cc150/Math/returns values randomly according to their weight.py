class solution():
    import random
    def weightedChoice(self, choices):
        """Like random.choice, but each element can have a different chance of
        being selected.

        choices can be any iterable containing iterables with two items each.
        Technically, they can have more than two items, the rest will just be
        ignored.  The first item is the thing being chosen, the second item is
        its weight.  The weights can be any numeric values, what matters is the
        relative differences between them.
        """

        space = {}
        current = 0
        for choice, weight in choices:
            if weight > 0:
                space[current+weight] = choice
                current += weight
        rand = random.uniform(0, current)
        print(rand)

        for key in sorted(space.keys()):
            choice = space[key]
            if rand < key:
                #return choice
                print(choice)
                break

        return None