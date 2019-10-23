def calculateFine(actually: list, expected: list) -> int:
	if expected[2] < actually[2]:
        return 10000
    elif expected[2]==actually[2]:
        if expected[1] < actually[1]:
            return (actually[1]-expected[1]) * 500
        if expected[0] < actually[0]:
            return (actually[0]-expected[0]) * 15
    return 0

a1=list(map(int, input().split()))
a2=list(map(int, input().split()))
print(calculateFine(a1, a2))