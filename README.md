# Charge Validation Tool

This is a tool to validate charging parameters.

Given a set of values, it checks if they have 'sudden jumps'.
Such jumps indicate a failed / noisy sensor.

## Tasks

1. The 'No Duplications' check is failing. Resolve the duplication.
1. Give a good name to the function `_give_me_a_good_name`.
It is a boolean function, used in `if` statements.
Ensure that the `if` statement reads like a sentence after you rename the function.
1. The `values` parameter, given to the `validate...` function can be `None`.
Currently, the code does not handle that.
Ensure the code ignores a call with `None` and add a test for that.
   

## Solutions

1. Resolved 'No Duplications' check by making a `single validate_sensor_stream` function and taking the param type as an
   argument.
1. Renamed the `_give_me_a_good_name` function to `is_there_a_spike` with corresponding return value changes which
   I feel sounds apt when read as a pseudocode.
1. Added none type checks to the renamed `sensor_stream` parameter (previously `values`) with an additional `param_name`
   check as well. Handled various errors and returns using status codes.
