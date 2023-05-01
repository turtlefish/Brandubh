import unittest

from game import check_capture, Turn


class TestCheckCapture(unittest.TestCase):
    print("===== TEST CAPTURES =====")
    def test_wbw(self):
        print("[wbw] capture")
        pieces_dict = {(3, 1): "b", (2, 1): "w", (4, 1): "w"}
        dest = (4, 1)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 1): "w", (4, 1): "w"})


    def test_xbw(self):
        print("[xbw] capture")
        pieces_dict = {(1, 0): "b", (2, 0): "w"}
        dest = (2, 0)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(2, 0): "w"})


    def test_xbb(self):
        print("[xbb] no capture")
        pieces_dict = {(1, 0): "b", (2, 0): "b"}
        dest = (2, 0)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(1, 0): "b", (2, 0): "b"})


    def test_xww_enemy_turn(self):
        print("[xww] no capture enemy turn")
        pieces_dict = {(0, 1): "w", (0, 2): "w", (3, 1): "b"}
        dest = (3, 1)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(0, 1): "w", (0, 2): "w", (3, 1): "b"})

    
    def test_tbw_capture(self):
        print("[tbw] capture")
        pieces_dict = {(4, 3): "b", (5, 3): "w"}
        dest = (5, 3)
        turn = Turn.WHITE

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(5, 3): "w"})

    def test_twb_capture(self):
        print("[twb] capture")
        pieces_dict = {(4, 3): "w", (5, 3): "b"}
        dest = (5, 3)
        turn = Turn.BLACK

        check_capture(pieces_dict, dest, turn)
        self.assertEqual(pieces_dict, {(5, 3): "b"})

if __name__ == "__main__":
    unittest.main()
