


def continuosCoverage(coverages):
    # store continuous coverage range
    daysCoverage = []

    # need to sort so consecutive days are ordered
    cvr = sorted(coverages)
    print("Sorted:", cvr)
    daybegin = cvr[0][0]
    dayend = cvr[0][1]

    # need to add this in beginning as this is starting coverage outside the loop
    daysCoverage.append(dayend - daybegin)
    print((daybegin, dayend))

    for i in range(1, len(cvr)):
        # compare starter tuple to current loop tuple
        # compare previous dayend to loop day begin, if difference between is less than or equal to 1,
        # need to take care of continuous day, e.g. if ends on 2nd and start on 3rd, its treated as continuous
        if (cvr[i][0] - dayend <= 1):
            dayend = cvr[i][1]
        else:
            daybegin = cvr[i][0]
            dayend = cvr[i][1]
        # add days coverage difference
        print((daybegin, dayend))
        daysCoverage.append(dayend - daybegin)
    return max(daysCoverage)



coverages = [(1, 20), (21, 30), (15, 25), (28, 40), (50, 60), (61, 200)]
print("Longest continuous coverage for:",coverages,continuosCoverage(coverages))


# coverages = [(1, 20), (21, 30), (15, 25), (28, 40), (50, 60), (29, 200)]
# print("Longest continuous coverage for:",coverages,continuosCoverage(coverages))
#
# coverages = [(1, 20), (31, 50)]
# print("Longest continuous coverage for:",coverages,continuosCoverage(coverages))
#
# coverages = [(1, 20), (31, 49)]
# print("Longest continuous coverage for:",coverages,continuosCoverage(coverages))
