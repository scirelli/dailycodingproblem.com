#!/usr/bin/env python3
"""
This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat,
and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number
of boats required will be three.
"""
ERASED = 0


def findSmallestNumberOfBoats(fatPeopleList, weightLimit):
    numberOfPassengersToSave = len(fatPeopleList)
    numberOfBoatsNeeded = 0
    fatPeopleList = fatPeopleList.copy()
    fatPeopleList.sort(reverse=True)

    for j in range(numberOfPassengersToSave):  # pylint: disable=consider-using-enumerate
        if fatPeopleList[j] == ERASED:
            continue

        currentWeightLimit = weightLimit
        for i in range(j, numberOfPassengersToSave):  # pylint: disable=consider-using-enumerate
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


def findSmallestNumberOfBoats_with_size_limit(fatPeopleList, weightLimit, passengerLimit=2):
    numberOfPassengersToSave = len(fatPeopleList)
    numberOfBoatsNeeded = 0
    fatPeopleList = fatPeopleList.copy()
    fatPeopleList.sort(reverse=True)

    for j in range(numberOfPassengersToSave):  # pylint: disable=consider-using-enumerate
        if fatPeopleList[j] == ERASED:
            continue

        currentWeightLimit = weightLimit
        openSeats = passengerLimit
        for i in range(j, numberOfPassengersToSave):  # pylint: disable=consider-using-enumerate
            personsWeight = fatPeopleList[i]
            fatPeopleList[i] = ERASED

            if personsWeight > weightLimit:
                raise ValueError('Person is to fat for a boat.')

            currentWeightLimit = currentWeightLimit - personsWeight
            openSeats = openSeats - 1
            if openSeats < 0:
                fatPeopleList[i] = personsWeight
                break
            elif currentWeightLimit == 0:
                break
            elif currentWeightLimit < 0:
                currentWeightLimit = currentWeightLimit + personsWeight
                fatPeopleList[i] = personsWeight
                openSeats = openSeats + 1

        numberOfBoatsNeeded = numberOfBoatsNeeded + 1

    return numberOfBoatsNeeded


def main():
    import random

    MAX_WEIGHT = 201
    MIN_NUMBER_OF_PEOPLE = 10
    MAX_NUMBER_OF_PEOPLE = 1001
    fatPeopleList = [random.randrange(1, MAX_WEIGHT) for x in range(random.randrange(MIN_NUMBER_OF_PEOPLE, MAX_NUMBER_OF_PEOPLE))]
    print('Smallest number of boats for [{}] is {}'.format(', '.join(str(x) for x in fatPeopleList), findSmallestNumberOfBoats(fatPeopleList, 200)))


if __name__ == '__main__':
    main()
