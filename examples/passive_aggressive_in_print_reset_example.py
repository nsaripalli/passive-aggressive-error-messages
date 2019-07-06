from error_message_handler import regular_error_messages_and_print_passive_aggresive, reset_error_messages

# STANDARD ERROR:
# Traceback (most recent call last):
#   File "passive_aggressive_in_print_reset_example.py", line 8, in <module>
#     float("Adsfas9232")
# ValueError: could not convert string to float: 'Adsfas9232'

# STANDARD OUT: N/A

if __name__ == "__main__":
    regular_error_messages_and_print_passive_aggresive()

    reset_error_messages()

    float("Adsfas9232")
