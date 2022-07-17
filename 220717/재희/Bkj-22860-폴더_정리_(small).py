import sys
from collections import defaultdict

input = sys.stdin.readline

# 해당 폴더부터 상위 폴더까지 파일 갱신
def update_file(folder: str, file: str) -> None:
    current_folder = folder

    while True:
        if file_count[current_folder].get(file):
            file_count[current_folder][file] += 1
        else:
            file_count[current_folder][file] = 1

        if current_folder == 'main':
            break
        current_folder = folder_link[current_folder]

# 파일의 종류, 총 개수 출력
def query(folder: str) -> None:
    files = file_count[folder].values()
    print(len(files), sum(files))


N, M = map(int, input().split())
folder_link = dict()  # 상위 폴더 입력
file_count = defaultdict(dict)  # 2중 딕셔너리로 폴더의 파일 카운트

# 폴더부터 설정한 후 파일 입력 (1 -> 0)
init_data = [list(input().strip().split()) for _ in range(N + M)]
init_data.sort(key=lambda x : int(x[2]), reverse=True)

for P, F, C in init_data:
    if C == '1':
        folder_link[F] = P
    else:
        update_file(P, F)

Q = int(input())

for _ in range(Q):
    q = input().strip().split('/')
    query(q[-1])