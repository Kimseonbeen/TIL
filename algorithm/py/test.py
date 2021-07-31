import time

def solution(numbers):
    answer = list()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer


start_time = time.time()
print(solution([2,1,3,4,1]))
end_time = time.time()
print("time : ", end_time - start_time)