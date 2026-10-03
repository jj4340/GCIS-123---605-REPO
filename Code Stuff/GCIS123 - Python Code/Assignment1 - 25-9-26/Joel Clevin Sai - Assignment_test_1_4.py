from Joel_Clevin_Sai_Assignment_production import getting_device_status

"""
Below are test conditions for the following:
1) Test for getting_device_status() to give normal reading
2) Test for getting_device_status() when reading is at boundary
3) Test for getting_device_status() to give High reading
4) Test for getting_device_status() to give Critical reading
"""

#-----------------------------------------------------------------------------------------#

"""
Test case for normal condition.
Shows that any reading with reading less that maximum is normal.
"""
def test_gds_normal():
    r = getting_device_status(0.5,0.4)
    assert r == "NORMAL"

#-----------------------------------------------------------------------------------------#

"""
Test case for boundary condition.
Reading is the maximum value of normal range for Television.
It should return HIGH since reading is at maximum value. 
"""
def test_gds_boundary():
    r = getting_device_status(0.5,0.5)
    assert r == "HIGH"

#-----------------------------------------------------------------------------------------#

"""
Test case for high reading.
Reading is higher than maximum but less than the limit for a critical reading.
Returns HIGH.
"""
def test_gds_high():
    r = getting_device_status(0.5,0.8)
    assert r == "HIGH"

#-----------------------------------------------------------------------------------------#

"""
Test case for critical reading.
Reading is higher than limit for critical reading (cv*max).
Returns CRITICAL
"""
def test_gds_critical():
    r = getting_device_status(0.5,1.2)
    assert r == "CRITICAL"