'''
 Assume the days of current year is numbered 1 to 365.

A Coverage is defined as range of dates with a coverage start and end/term date. 
Eg: Cov(1, 30) means the person is covered for something for Jan of this year.

Problem: Given a series of coverage data for a person, we need to find the longest continuous coverage. 
The coverage may have overlap and/or gaps in coverage.
 
Example data:

class Cov(eff: Int, term: Int
val coverages = List(Cov(1, 20), Cov(21, 30), Cov(15, 25), Cov(28, 40), Cov(50, 60), Cov(61, 200)

Output:

Sorted: [(1, 20), (15, 25), (21, 30), (28, 40), (50, 60), (61, 200)]

(1, 20)
(1, 25)
(1, 30)
(1, 40)
(50, 60)
(50, 200)

Longest continuous coverage for: [(1, 20), (21, 30), (15, 25), (28, 40), (50, 60), (61, 200)] 

Longest continuous coverage: 150


'''


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
