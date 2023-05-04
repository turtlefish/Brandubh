import unittest

from game import Turn, check_capture, get_piece_moves


class TestCheckCapture(unittest.TestCase):
    print("===== TEST CAPTURES =====")

    def test_bkb(self):
        print("[bKb] capture")
        pieces_dict = {(2, 1): "b", (3, 1): "K", (4, 1): "b"}
        dest = (4, 1)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "b", (4, 1): "b"})

    def test_xkb(self):
        print("[xKb] capture")
        pieces_dict = {(1, 0): "K", (2, 0): "b"}
        dest = (2, 0)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 0): "b"})

    def test_wbw(self):
        print("[wbw] capture")
        pieces_dict = {(3, 1): "b", (2, 1): "w", (4, 1): "w"}
        dest = (4, 1)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "w", (4, 1): "w"})

    def test_wbk(self):
        print("[wbK] capture")
        pieces_dict = {(3, 1): "b", (2, 1): "w", (4, 1): "K"}
        dest = (4, 1)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "w", (4, 1): "K"})

    def test_xbw(self):
        print("[xbw] capture")
        pieces_dict = {(1, 0): "b", (2, 0): "w"}
        dest = (2, 0)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 0): "w"})

    def test_tbw(self):
        print("[tbw] capture")
        pieces_dict = {(4, 3): "b", (5, 3): "w"}
        dest = (5, 3)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(5, 3): "w"})

    def test_twb(self):
        print("[twb] capture")
        pieces_dict = {(4, 3): "w", (5, 3): "b"}
        dest = (5, 3)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(5, 3): "b"})

    def test_bwbwb_horizontal(self):
        print("[bwbwb] double capture horizontal")
        pieces_dict = {(2, 1): "b", (4, 1): "b", (6, 1): "b", (3, 1): "w", (5, 1): "w"}
        dest = (4, 1)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "b", (4, 1): "b", (6, 1): "b"})

    def test_bwbwb_right_angle_capture(self):
        print("[bwbwb] double capture right angle")
        pieces_dict = {(1, 1): "b", (3, 1): "b", (1, 3): "b", (1, 2): "w", (2, 1): "w"}
        dest = (1, 1)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(1, 1): "b", (3, 1): "b", (1, 3): "b"})

    def test_xbb(self):
        print("[xbb] no capture")
        pieces_dict = {(1, 0): "b", (2, 0): "b"}
        dest = (2, 0)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(1, 0): "b", (2, 0): "b"})

    def test_wkw(self):
        print("[wKw] no capture")
        pieces_dict = {(2, 1): "w", (3, 1): "K", (4, 1): "w"}
        dest = (4, 1)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "w", (3, 1): "K", (4, 1): "w"})

    def test_xkw(self):
        print("[xKw] no capture")
        pieces_dict = {(1, 0): "K", (2, 0): "w"}
        dest = (2, 0)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(1, 0): "K", (2, 0): "w"})

    def test_xww_black_turn(self):
        print("[xww] no capture black turn")
        pieces_dict = {(0, 1): "w", (0, 2): "w", (3, 1): "b"}
        dest = (3, 1)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(0, 1): "w", (0, 2): "w", (3, 1): "b"})

    def test_bwk_white_turn(self):
        print("[bwK] no capture white turn")
        pieces_dict = {(2, 1): "b", (3, 1): "w", (4, 1): "K"}
        dest = (4, 1)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "b", (3, 1): "w", (4, 1): "K"})

    def test_bwk_black_turn(self):
        print("[bwK] no capture black turn")
        pieces_dict = {(2, 1): "b", (3, 1): "w", (4, 1): "K"}
        dest = (2, 1)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "b", (3, 1): "w", (4, 1): "K"})


class TestMovement(unittest.TestCase):
    pieces_dict = {
        (1, 0): "w",
        (3, 0): "w",
        (5, 3): "b",
        (5, 6): "b",
        (1, 5): "b",
        (3, 5): "K",
    }

    pieces_dict_king_throne = {(3, 3): "K", (3, 0): "w", (5, 3): "w"}

    def test_white_moves(self):
        print("White moves")

        moves = get_piece_moves(TestMovement.pieces_dict, (1, 0))
        self.assertEqual(moves, [(2, 0), (1, 1), (1, 2), (1, 3), (1, 4)])

        moves = get_piece_moves(TestMovement.pieces_dict, (3, 0))
        self.assertEqual(moves, [(4, 0), (5, 0), (2, 0), (3, 1), (3, 2), (3, 4)])

        moves = get_piece_moves(TestMovement.pieces_dict_king_throne, (3, 0))
        self.assertEqual(moves, [(4, 0), (5, 0), (2, 0), (1, 0), (3, 1), (3, 2)])

    def test_black_moves(self):
        print("Black moves")

        moves = get_piece_moves(TestMovement.pieces_dict, (5, 3))
        self.assertEqual(
            moves,
            [
                (6, 3),
                (4, 3),
                (2, 3),
                (1, 3),
                (0, 3),
                (5, 4),
                (5, 5),
                (5, 2),
                (5, 1),
                (5, 0),
            ],
        )

        moves = get_piece_moves(TestMovement.pieces_dict, (1, 5))
        self.assertEqual(
            moves, [(2, 5), (0, 5), (1, 6), (1, 4), (1, 3), (1, 2), (1, 1)]
        )

        moves = get_piece_moves(TestMovement.pieces_dict, (5, 6))
        self.assertEqual(moves, [(4, 6), (3, 6), (2, 6), (1, 6), (5, 5), (5, 4)])

        moves = get_piece_moves(TestMovement.pieces_dict_king_throne, (5, 3))
        self.assertEqual(
            moves, [(6, 3), (4, 3), (5, 4), (5, 5), (5, 6), (5, 2), (5, 1), (5, 0)]
        )

    def test_king_moves(self):
        print("King moves")
        moves = get_piece_moves(TestMovement.pieces_dict, (3, 5))
        self.assertEqual(
            moves,
            [(4, 5), (5, 5), (6, 5), (2, 5), (3, 6), (3, 4), (3, 3), (3, 2), (3, 1)],
        )

        moves = get_piece_moves(TestMovement.pieces_dict_king_throne, (3, 3))
        self.assertEqual(
            moves,
            [(4, 3), (2, 3), (1, 3), (0, 3), (3, 4), (3, 5), (3, 6), (3, 2), (3, 1)],
        )


if __name__ == "__main__":
    unittest.main()
