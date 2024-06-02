from itertools import combinations

def count_valid_combinations(N, M, K, tests):
    all_keys = set(range(1, N + 1))
    possible_sets = set()
    impossible_sets = set()
    # テスト結果に基づいてフィルタリング
    for test_keys, result in tests:
        test_keys = test_keys[1:]
        test_keys_set = set(test_keys)
        if result == 'o':
            # ドアが開いた => K本以上の正しい鍵が含まれている必要がある
            print(test_keys_set)
            for comb in combinations(test_keys_set, K):
                if comb not in possible_sets:
                    possible_sets.add(comb)
            print(possible_sets)
        elif result == 'x':
            # ドアが開かなかった => K本以上の正しい鍵が含まれていない
            for comb in combinations(test_keys_set, K):
                impossible_sets.add(comb)
    
    # 開く可能性のある組み合わせから、開かない組み合わせを引く
    print(len(possible_sets), len(impossible_sets))
    valid_combinations = possible_sets - impossible_sets
    
    return len(valid_combinations)

# 入力を読み取る
N, M, K = map(int, input().split())
tests = []

for _ in range(M):
    data = input().split()
    test_keys = list(map(int, data[:-1]))
    result = data[-1]
    tests.append((test_keys, result))

# 結果を表示
print(count_valid_combinations(N, M, K, tests))
