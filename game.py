from enum import Enum
import random


class Turn(Enum):
    WHITE = "Kw"
    BLACK = "b"


BOARD_SIZE = 7
ESCAPE_SQUARES = [(0, 0), (0, 6), (6, 0), (6, 6)]
THRONE_SQUARE = (3, 3)
SPECIAL_SQUARES = ESCAPE_SQUARES + [THRONE_SQUARE]
KING_CHAR, WHITE_CHAR, BLACK_CHAR = "K", "w", "b"
ADJACENCY_MASKS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


white_pieces = [(4, 3), (2, 3), (3, 4), (3, 2)]
king = (3, 3)
black_pieces = [(0, 3), (1, 3), (5, 3), (6, 3), (3, 0), (3, 1), (3, 5), (3, 6)]

# white_pieces = [(3, 0)]
# king = (3, 3)
# black_pieces = [(5, 3)]

pieces = [white_pieces, king, black_pieces]

pieces_dict = {}
for piece in white_pieces:
    pieces_dict[piece] = "w"

for piece in black_pieces:
    pieces_dict[piece] = "b"

pieces_dict[king] = "K"

turn = Turn.BLACK


def print_board(pieces_dict: dict, print_turn=False):
    board_str = "+---------------+\n"

    for y in range(BOARD_SIZE):
        board_str += "| "
        for x in range(BOARD_SIZE):
            empty_char = (
                "#"
                if (x, y) in ESCAPE_SQUARES
                else "@"
                if (x, y) == THRONE_SQUARE
                else "."
            )

            end_char = f" |{y}" if x == BOARD_SIZE - 1 else " "

            if val := pieces_dict.get((x, y)):
                board_str += val + end_char

            else:
                board_str += empty_char + end_char

        board_str += "\n"

    board_str += "+---------------+\n"
    board_str += "  0 1 2 3 4 5 6\n"
    if print_turn:
        board_str += str(turn) + "\n"

    print(board_str)
    return board_str


def change_turn():
    global turn
    if turn == Turn.BLACK:
        turn = Turn.WHITE

    else:
        turn = Turn.BLACK


def get_pieces(pieces_dict: dict, turn: Turn):
    return [loc for (loc, col) in pieces_dict.items() if col in turn.value]


def move_piece(origin: tuple[int], dest: tuple[int]):
    pieces_dict[dest] = pieces_dict[origin]
    pieces_dict.pop(origin)
    check_capture(pieces_dict, dest, turn)
    change_turn()


def get_piece_moves(pieces_dict: dict, piece: tuple[int]):
    if piece not in pieces_dict:
        raise ValueError(f"Piece {piece} is not in the dictionary.")

    moves = []
    for dx in range(piece[0] + 1, BOARD_SIZE):
        if (dx, piece[1]) in pieces_dict or (
            (dx, piece[1]) in SPECIAL_SQUARES and pieces_dict[piece] != "K"
        ):
            if (dx, piece[1]) == THRONE_SQUARE and THRONE_SQUARE not in pieces_dict:
                continue

            else:
                break

        moves.append((dx, piece[1]))

    for dx in range(piece[0] - 1, -1, -1):
        if (dx, piece[1]) in pieces_dict or (
            (dx, piece[1]) in SPECIAL_SQUARES and pieces_dict[piece] != "K"
        ):
            if (dx, piece[1]) == THRONE_SQUARE and THRONE_SQUARE not in pieces_dict:
                continue

            else:
                break

        moves.append((dx, piece[1]))

    for dy in range(piece[1] + 1, BOARD_SIZE):
        if (piece[0], dy) in pieces_dict or (
            (piece[0], dy) in SPECIAL_SQUARES and pieces_dict[piece] != "K"
        ):
            if (piece[0], dy) == THRONE_SQUARE and THRONE_SQUARE not in pieces_dict:
                continue

            else:
                break

        moves.append((piece[0], dy))

    for dy in range(piece[1] - 1, -1, -1):
        if (piece[0], dy) in pieces_dict or (
            (piece[0], dy) in SPECIAL_SQUARES and pieces_dict[piece] != "K"
        ):
            if (piece[0], dy) == THRONE_SQUARE and THRONE_SQUARE not in pieces_dict:
                continue

            else:
                break

        moves.append((piece[0], dy))

    return moves


def make_random_move(pieces_dict: dict, turn: Turn):
    pieces = get_pieces(pieces_dict, turn)
    piece = random.choice(pieces)

    while not len(get_piece_moves(pieces_dict, piece)):
        piece = random.choice(pieces)

    move_piece(piece, random.choice(get_piece_moves(pieces_dict, piece)))


def check_capture(pieces_dict: dict, dest: tuple[int], turn: Turn):
    for MASK in ADJACENCY_MASKS:
        adj_piece = (dest[0] + MASK[0], dest[1] + MASK[1])
        sandwich_piece = (dest[0] + MASK[0] * 2, dest[1] + MASK[1] * 2)

        if (ac := pieces_dict.get(adj_piece)) and (ac not in turn.value):
            if ((sc := pieces_dict.get(sandwich_piece)) and (sc in turn.value)) or (
                sandwich_piece in SPECIAL_SQUARES
            ):
                pieces_dict.pop(adj_piece)


# while True:
#     print_board(pieces_dict, print_turn=True)
#     print(f"{pieces_dict=}")

#     origin = tuple(int(_) for _ in input("origin: ").split(","))
#     while origin not in pieces_dict:
#         origin = tuple(int(_) for _ in input("origin: ").split(","))

#     dest = tuple(int(_) for _ in input("dest: ").split(","))
#     while dest not in get_piece_moves(pieces_dict, origin):
#         dest = tuple(int(_) for _ in input("dest: ").split(","))

#     # moves = get_piece_moves(pieces_dict, origin)
#     # moves_board = {move: "O" for move in moves}
#     # print(f"{moves=}")
#     # print_board(moves_board)

#     # make_random_move(pieces_dict, turn)
#     move_piece(origin, dest)
