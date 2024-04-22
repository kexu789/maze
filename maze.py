# 定义迷宫地图
maze = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '*', ' ', '*', ' ', '*', '*', ' ', '*'],
    ['*', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
]

# 宝藏位置
treasure_location = (5, 8)

# 玩家初始位置
player_location = (1, 1)

# 游戏循环
while True:
    # 打印迷宫地图
    for row in maze:
        print(''.join(row))

    # 获取玩家输入的移动命令
    command = input("请输入移动命令 (w: 上, s: 下, a: 左, d: 右): ")

    # 根据命令更新玩家位置
    if command == 'w':
        new_location = (player_location[0] - 1, player_location[1])
    elif command == 's':
        new_location = (player_location[0] + 1, player_location[1])
    elif command == 'a':
        new_location = (player_location[0], player_location[1] - 1)
    elif command == 'd':
        new_location = (player_location[0], player_location[1] + 1)
    else:
        print("无效的命令，请重新输入")
        continue

    # 检查新位置是否合法
    if maze[new_location[0]][new_location[1]] == '*':
        print("撞墙了，请重新输入移动命令")
        continue

    # 更新玩家位置
    player_location = new_location

    # 检查是否找到宝藏
    if player_location == treasure_location:
        print("恭喜你找到宝藏！游戏结束。")
        break
