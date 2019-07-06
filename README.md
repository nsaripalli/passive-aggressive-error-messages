Ever needed some passive aggressive motivation while coding?

Now there's a dedicated passive aggressive error messaging system built on top of python's error messaging system
to help question your purpose as a developer. 

There are two options on how you want your passive aggressive error messages delivered.

In error_messages_handler.py there are three functions:
1. regular_error_messages_and_print_passive_aggresive
    * Standard error will stay as the python default and the passive aggressive
    error messages will be delivered via standard out

2. regular_error_messages_includes_passive_aggresive
    * The passive aggressive messages will be added on to the normal error messages in standard out

3. reset_error_messages
    * This resets the error messaging system back to the python default error messages. This will reset
    any modifications that are caused by this program.
