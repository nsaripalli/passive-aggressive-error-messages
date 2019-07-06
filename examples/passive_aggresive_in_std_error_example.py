from error_message_handler import regular_error_messages_includes_passive_aggresive

# STANDARD ERROR:
# Traceback (most recent call last):
#   File "passive_aggresive_in_std_error_example.py", line 7, in <module>
#     float("Adsfas9232")
# ValueError: could not convert string to float: 'Adsfas9232'
# What did you think this was? Python?

# STANDARD OUT:
# This will not be in the error message

if __name__ == "__main__":
    regular_error_messages_includes_passive_aggresive()
    print("This will not be in the error message")

    float("Adsfas9232")