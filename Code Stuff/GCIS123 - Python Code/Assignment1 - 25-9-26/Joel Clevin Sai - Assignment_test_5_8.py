from Joel_Clevin_Sai_Assignment_production import getting_energy_cost
from Joel_Clevin_Sai_Assignment_production import requires_alert
from Joel_Clevin_Sai_Assignment_production import getting_device_status

"""
Below are test conditions for the following:
1) Test for getting_energy_cost() function
2) Test for requires_alert() function
3) Test for reading = 0
4) Test for reading < 0
"""

#-----------------------------------------------------------------------------------------#

"""
Test case for energy cost.
If the function logic is right, then cost would equal to reading*cost_of_consumption.
"""
c = 0.23
def test_energy_cost():
    cost = getting_energy_cost(0.4,c)
    assert cost == 0.4*c

#-----------------------------------------------------------------------------------------#

"""
Test case for requires attention.
The logic of function is that it returns True if the status of device is "HIGH" or "CRITICAL"
If logic works, then for the given test; assertion would equal to True.
This means the device requires attention and function works correctly.
"""
def test_requires_attention():
    assertion = requires_alert("HIGH")
    assert assertion == True

#-----------------------------------------------------------------------------------------#

"""
Test case for invalid Input - 0 input.
We check what happens if the reading is 0.
If the function logic works correctly, r would be equal to "INVALID READING".
The check_zero_or_negative() function checks if the value is 0 or negative. If 0, it returns "NIL".
If NIL, then getting_device_status will return "INVALID READING"
"""
def test_gds_invalid():
    r = getting_device_status(0.5,0)
    assert r == "INVALID READING"

#-----------------------------------------------------------------------------------------#

"""
Test case for invalid Input - negative input.
We check what happens if the reading is negative.
If the function logic works correctly, r would be equal to "INVALID READING".
The check_zero_or_negative() function checks if the value is 0 or negative. If 0, it returns "NIL".
If NIL, then getting_device_status will return "INVALID READING"
"""
def test_gds_invalid_negative():
    r = getting_device_status(0.5,-8)
    assert r == "INVALID READING"
