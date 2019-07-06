import sys, traceback, random

def __passive_aggressive_to_error_messages_handler(type, value, tb):
    """Adds a passive aggressive message to an error message in standard error"""
    traceback.print_exception(type, value, tb)

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

    sys.stderr.write(random.choice(errors))

def __print_passive_aggressive_messages_handler(type, value, tb):
    """Prints a passive aggressive message along with the normal error message"""
    traceback.print_exception(type, value, tb)

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

    print(random.choice(errors))


def regular_error_messages_and_print_passive_aggresive():
    """Passive aggressive messages in stdout along with the regular error messages in std error"""
    sys.excepthook = __print_passive_aggressive_messages_handler

def regular_error_messages_includes_passive_aggresive():
    """Inlcudes passive aggressive messages in the standard error messages"""
    sys.excepthook = __passive_aggressive_to_error_messages_handler

def reset_error_messages():
    """Resets the error messages handler to the python default"""
    sys.excepthook = sys.__excepthook__
