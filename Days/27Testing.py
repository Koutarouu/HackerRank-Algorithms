def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function
        return [i for i in range(2)]

    @staticmethod
    def get_expected_result():
        # complete this function
        return 0

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        return [0 for i in range(2)] + [1] #[0,0,1]

    @staticmethod
    def get_expected_result():
        # complete this function
        return 0 #the first minimum


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

"""
Since the problem is all about designing data for unit tests according to the given requirements, the solution is pretty straightforward:
TestDataEmptyArray.get_array() returns an empty array, so for example [] in Python (in fact, it's called a list,
not an array in python), or empty vector<int> in C++
TestDataUniqueValues.get_array() returns an array of at least two elements with all unique values, so for example [1,2] is sufficient,
and then, TestDataUniqueValues.get_expected_result() returns 0 as the index of minimum value in this array
TestDataExactlyTwoDifferentMinimums.get_array() returns an array with at exactly two different elements with minimum value,
so for example [2,1,1] is fine, and then TestDataExactlyTwoDifferentMinimums.get_expected_result()
returns 1 as the index of first of these minimums because it is the expected result according to the statement.
"""