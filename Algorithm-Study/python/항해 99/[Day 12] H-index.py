def solution(citations):
    result = []
    citations.sort(reverse=True)

    if citations[0] == 0:
        return 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            result.append(i + 1)

    return max(result)