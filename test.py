import subprocess
import unittest


class PassiveAggressiveErrorsTest(unittest.TestCase):
    errors = ["How's that CS degree working out for you?",
              "Did you actually think that was going to work?",
              "I admire how much confidence you have",
              "Boy, you sure have lived up to your potential haven't you?",
              "Bless your heart",
              "I'm sure you're doing the best you can",
              "I feel like I've asked too much of you.",
              "A, for Effort ",
              "Wow the amount of effort you put into today really shows",
              "I can explain it to you again, but I can't make you understand.",
              "What did you think this was? Python?"]

    def test_passive_aggressive_in_std_error(self):
        proc = subprocess.run(['python', 'examples/passive_aggresive_in_std_error_example.py'], capture_output=True)
        self.assertIn(proc.stderr.decode().split("\n")[-1], self.errors)
        self.assertEqual("This will not be in the error message\n", proc.stdout.decode())

    def test_passive_aggressive_in_print_reset(self):
        proc = subprocess.run(['python', 'examples/passive_aggressive_in_print_reset_example.py'], capture_output=True)
        self.assertFalse(any(error_message in proc.stderr.decode() for error_message in self.errors))
        self.assertEqual(proc.stdout.decode(), '')

    def test_passive_aggressive_in_standard_out(self):
        proc = subprocess.run(['python', 'examples/passive_aggressive_in_standard_out_example.py'], capture_output=True)
        self.assertFalse(any(error_message in proc.stderr.decode() for error_message in self.errors))
        self.assertTrue(any(error_message in proc.stdout.decode() for error_message in self.errors))

    def test_passive_aggressive_in_std_error_reset(self):
        proc = subprocess.run(['python', 'examples/passive_aggressive_in_std_error_reset_example.py'], capture_output=True)
        self.assertFalse(any(error_message in proc.stderr.decode() for error_message in self.errors))
        self.assertEqual(proc.stdout.decode(), 'This will not be in the error message\n')


if __name__ == '__main__':
    unittest.main()
