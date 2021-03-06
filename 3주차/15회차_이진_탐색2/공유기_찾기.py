def install_router(lst, C):
    # 1. 이분탐색을 위한 정렬
    lst.sort()

    # 2. 이분탐색 대상은 '최대거리'.
    # 최솟값은 1, 최댓값은 양 끝값의 차이.
    lo = 1 # 현재 역활: 최솟값
    hi = lst[-1] - lst[0] # 현재 역활: 양 끝값 차이
    min_gap = 0 # 0

    # [1, 2, 4, 8, 9]
    # [1,2,3,4,5,6,7,8]
    # 3. 최대 거리를 찾을 때까지 이분탐색

    while lo <= hi: # 최소값이 양 끝값 차이보다 적냐
        # 중간 거리를 시험해본다.
        mid = (lo + hi) // 2 # 두 요소 중간값

        # 0번째 요소에 항상 설치하므로 1개를 깔고 간다.
        cnt = 1 # 보기에는 그냥 카운트 같아 보인다, 근데 1부터시작
        # 0번째 요소부터 시작.
        cur = lst[0] # 리스트에 첫번째꺼, 이름이 커서인거 보니 바뀔꺼 같다.
        # [1**, 2, 4, 8, 9]

        # 1번째 ~ 마지막 요소를 연결시켜본다.
        for i in range(1, len(lst)): # 1부터 리스트만큼 반복한다
            # 연결만 된다면 더 멀리 있는 것도 괜찮다
            # 이해가 안된다면 문제의 예시인
            # [1, 2, 4, 8, 9] 를 최대거리 3으로 연결하는 경우를 찬찬히 생각해보자.
            # (1, 4, 8)에 설치한 경우, 1~4 거리는 3, 4~8 거리는 4다.
            # 가장 인접한 두 점의 최대 거리가 3이므로 4가 괜찮은 것이다.
            9> 8+4
            if lst[i] >= cur + mid: # 리스트에 특정 요소가 cur(1)에 중간값 더한것 보다 크냐,
                # cur이 비교 대상인데 cur이 작으면 cur은 리스트에 특정 요소로 바뀜
                # -> lst[i] 비교 값 즉 걸리는 기준은 계속 높아진다.
                # -> 근데, lst 정렬된거, 즉 올라도 같이 올라감
                # [1,2,3,4,5,6,7,8] 오르는 갭은 큰 차이가 없다.
                # 커서도 리스트에서 온거니, 그 갭은 큰 변화가 없지만, 갭에 영향을 주는 외부요소가 있다.
                # mid에 따라서 list에서 cur을 선택할 간격이 달라진다.
                # 클 경우
                cur = lst[i] #리스트에 특정 요소가 cur로 변화한다.
                # 이건뭐..그냥 +1
                cnt += 1

        # 카운트가 C라는 애보다 크거나 같으면
        # C는 뭐냐 공유기의 개수
        # 즉 우리가 공유기 개수 만큼 연산을 잘 했느냐
        if cnt >= C:
            # min_gap이란 애한테 mid를 넣는데,
            # min_gap은 리턴값
            # 책에서 리턴값은 뭐냐? -> 최대 거리를 출력하라
            # 즉 min_gap은 최대 거리인데, 여기에 mid를 넣어주니, mid = 최대 거리
            # 즉 mid는 갭이다. 단계, 갭
            min_gap = mid
            # 최소값에 최대거리 + 1 을 넣어준다.
            lo = mid + 1
        else: # 공유기 개수 만큼 연산을 못함
            # 양 끝값 차이에 최대거리 -1을 넣어준다.
            hi = mid - 1
        # 최대 거리 = mid = (lo+hi)//2
        # 즉 어떤 연산을 하든, 위치값 조정은 계속된다.
        # 그 판별은 위에서 하고
        # 최대 거리를 찾기 위해서 위치값을 계속 조정해 연산을 하는 과정
        # 10, 8, 6, 1, 2, 3, 4
        # 그 연산은 위치값이 더이상 연산이 불가능한 경우까지


    return min_gap


assert install_router([1, 2, 8, 4, 9], 3) == 3
