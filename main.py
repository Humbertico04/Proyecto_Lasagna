EXPECTED_BAKE_TIME = 40
#EXPECTED_BAKE_TIME constant returns how many minutes the lasagna should bake in the oven. According to the cookbook, the Lasagna should be in the oven for 40 minutes

PREPARATION_TIME = 2
#PREPARATION_TIME constant returns how many minutes it takes to prepare a single layer. We assume each layer takes 2 minutes to prepare.


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
   
    Function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME'.
   
    function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them based on `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time you´ve been cooking.

    :param number_of_layers: int - number of layers of the lasagna made.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes)
   
    function that returns the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)