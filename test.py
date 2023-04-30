import unittest

from game import check_capture, Turn


class TestCheckCapture(unittest.TestCase):
    def test_capture(self):
        print("Test standard capture [wbw]")
        pieces_dict = {(3, 1): "b", (2, 1): "w", (4, 1): "w"}
        dest = (4, 1)
        turn = Turn.WHITE
        check_capture(pieces_dict, dest, turn)
        print(pieces_dict)
        self.assertEqual(pieces_dict, {(2, 1): "w", (4, 1): "w"})


if __name__ == "__main__":
    unittest.main()
