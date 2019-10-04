#!/usr/bin/env python3
"""
This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

del fpl[i:i+1]
"""
ERASED = 0


def findSmallestNumberOfBoats(fatPeopleList, weightLimit):
    numberOfPeople = len(fatPeopleList)
    numberOfBoatsNeeded = 0
    fatPeopleList = fatPeopleList.copy()
    fatPeopleList.sort(reverse=True)

    for j in range(numberOfPeople):  # pylint: disable=consider-using-enumerate
        if fatPeopleList[j] == ERASED:
            continue

        currentWeightLimit = weightLimit
        for i in range(j, numberOfPeople):  # pylint: disable=consider-using-enumerate
            personsWeight = fatPeopleList[i]
            fatPeopleList[i] = ERASED

            if personsWeight > weightLimit:
                raise ValueError('Person is to fat for a boat.')

            currentWeightLimit = currentWeightLimit - personsWeight

            if currentWeightLimit == 0:
                break
            elif currentWeightLimit < 0:
                currentWeightLimit = currentWeightLimit + personsWeight
                fatPeopleList[i] = personsWeight

        numberOfBoatsNeeded = numberOfBoatsNeeded + 1

    return numberOfBoatsNeeded


def main():
    import random

    MAX_WEIGHT = 201
    MIN_SIZE = 10
    MAX_SIZE = 1001
    fatPeopleList = [random.randrange(1, MAX_WEIGHT) for x in range(random.randrange(MIN_SIZE, MAX_SIZE))]
    print('Smallest number of boats for [{}] is {}'.format(', '.join(str(x) for x in fatPeopleList), findSmallestNumberOfBoats(fatPeopleList, 200)))


if __name__ == '__main__':
    main()
