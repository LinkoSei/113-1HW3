def can_knight_cover_board(N, startX, startY):
    # 定義騎士的 8 種可能移動方式
    moves = [
        (-2, -1), (-2, 1), (-1, 2), (1, 2),
        (2, 1), (2, -1), (1, -2), (-1, -2)
    ]

    # 初始化棋盤，0 表示未訪問過
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # 初始化堆疊
    stack = [(startX, startY, 1)]  # (x, y, step_count)
    board[startX][startY] = 1  # 標記起始點已訪問
    
    while stack:
        x, y, step = stack.pop()

        # 如果所有格子都已訪問，返回 True
        if step == N * N:
            return True

        # 遍歷 8 種可能的移動方式
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:  # 確保在棋盤內且未訪問過
                board[nx][ny] = step + 1  # 標記下一步
                stack.append((nx, ny, step + 1))

        # 如果此路徑無法完成任務，回溯
        board[x][y] = 0

    return False

# 輸入
N = int(input("請輸入棋盤大小 N (4 <= N <= 10): "))
startX = int(input("請輸入起始點 X 座標 (0<=X<N): "))
startY = int(input("請輸入起始點 Y 座標 (0<=Y<N): "))

# 輸出
if can_knight_cover_board(N, startX, startY):
    print("True")
else:
    print("False")
