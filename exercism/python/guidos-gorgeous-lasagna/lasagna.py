"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(real_time):
    return EXPECTED_BAKE_TIME - real_time
    


def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2




#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    prep_time = number_of_layers * 2
    return prep_time + elapsed_bake_time
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
# def 