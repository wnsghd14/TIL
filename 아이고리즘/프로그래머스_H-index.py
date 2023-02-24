def solution(citations):
    citations.sort()
    for i, v in enumerate(citations):
        if v >= len(citations) - i :
            return len(citations) - i
    return 0