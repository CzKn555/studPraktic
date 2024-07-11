x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
is_within_board = all(1 <= coordinate <= 8 for coordinate in (x1, y1, x2, y2))
can_move_rook = is_within_board and (x1 == x2 or y1 == y2)
output_rook = "YES" if can_move_rook else "NO"
print(output_rook)