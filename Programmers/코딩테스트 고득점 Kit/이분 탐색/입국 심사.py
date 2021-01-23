def solution(n, times):
    start = 1
    end = max(times)*n
    #시간이라는 답을 먼저 잡아놓고, 이 시간동안 할 수 있어? 를 판단해서 최적의 값을 내놓기
    def binary_search(start, end, n):
        result = 0
        while start <= end:
            mid = (start + end) // 2
            cnt = 0
            for time in times:#mid의 시간동안 몇명 할 수 있어?
                cnt += mid//time
            if cnt >= n: #mid의 시간동안 N명보다 많이 할 수 있으면
                # 시간을 덜 줘도 됨> 시간을 줄여야함
                end = mid - 1
                result = mid
            else:#mid의 시간동안 N명을 못 채우면 시간을 더 줘야해
                start = mid + 1

        return result
    answer = binary_search(start,end,n)
    return answer