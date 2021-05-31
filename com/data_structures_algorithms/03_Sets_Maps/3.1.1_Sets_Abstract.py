"""
A set is a container that stores a collection of unique values over a given comparable
domain in which the stored values have no particular ordering
"""

"""
 intersect(setB): Creates and returns a new set that is the intersection of this set and setB.
  The intersection of sets A and B contains only those elements that are in both A and B. 
  Neither set A nor set B is modified by this operation.
  
􏰀 difference( setB ): Creates and returns a new set that is the difference of this set and setB.
 The set difference, A−B, contains only those elements that are in A but not in B.
  Neither set A nor set B is modified by this operation.
"""

abir = set()
abir.add("Math-112")
abir.add("HIST-121")
abir.add("ECON-101")
abir.add("CSCI-121")

roberts = set()
roberts.add("ECON-101")
roberts.add("ANTH-230")
roberts.add("CSCI-121")
roberts.add("POL-101")

"""
Next, we determine if the two students are taking the exact same courses. 
If not, then we want to know if they are taking any of the same courses. 
We can do this by computing the intersection between the two sets.
"""
if abir == roberts:
    print("Taking same courses")
else:
    sameCourses = abir.intersection(roberts)
    if sameCourses == 0:
        print("Abir and Roberts are taking any of "
              + "the same cour  se.")
    else:
        print("They are taking some of the "
              + "same courses")
        for course in sameCourses:
            print("They are taking same courses: ", course)

uniqueCourse = abir.difference(roberts)
for course in uniqueCourse:
    print("They are taking difference courses: ", course)

