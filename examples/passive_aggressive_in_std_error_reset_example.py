from error_message_handler import regular_error_messages_includes_passive_aggresive, reset_error_messages

# STANDARD ERROR:
# Traceback (most recent call last):
#   File "passive_aggressive_in_std_error_reset_example.py", line 9, in <module>
#     float("Adsfas9232")
# ValueError: could not convert string to float: 'Adsfas9232'

# STANDARD OUT:
# This will not be in the error message

if __name__ == "__main__":
    regular_error_messages_includes_passive_aggresive()
    print("This will not be in the error message")

    reset_error_messages()

    float("Adsfas9232")