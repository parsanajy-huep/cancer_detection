"""Functions for preparing delicious lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2  # ثابت جدید برای حذف عدد جادویی


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time."""
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time