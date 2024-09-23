def validate_temperature(temperature):
    """
    Validates if the given temperature is within the valid range.

    Parameters:
    - temperature: float
        The temperature value to be validated.

    Returns:
    - bool:
        True if the temperature is within the valid range, False otherwise.
    """

    if temperature >= -40 and temperature <= 55:
        return True
    else:
        return False


def calculate_average_temperature(temperatures):
    """
    Calculates the average temperature for a given list of temperatures.

    Parameters:
    - temperatures: list of floats
        The list of temperatures for which the average needs to be calculated.

    Returns:
    - int:
        The average temperature as an integer.

    Raises:
    - ValueError:
        If any of the temperatures in the list is not within the valid range.
    """

    # Validating each temperature in the list
    for temperature in temperatures:
        if not validate_temperature(temperature):
            raise ValueError("Invalid temperature value.")

    # Calculating the average temperature
    average = sum(temperatures) / len(temperatures)

    # Returning the average temperature as an integer
    return int(average)


# Example usage:
temperatures = [25, 30, 28, 32, 27, 29, 26]

try:
    average_temperature = calculate_average_temperature(temperatures)
    print(f"The average temperature for the week is: {average_temperature}°C")
except ValueError as e:
    print(f"Error: {e}")
