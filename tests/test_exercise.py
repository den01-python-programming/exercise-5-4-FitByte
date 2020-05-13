import pytest
import os

def test_exercise():
    os.chdir('src')

    from fitbyte import FitByte
    age = 25
    resting_heart_rate = 56
    maximum_heart_rate = 206.3 - (0.711 * age)
    target_heart_rate = (maximum_heart_rate - resting heart rate) * (target heart rate percentage) + resting heart rate

    heart = FitByte(age,resting_heart_rate)

    assert heart.target_heart_rate(100) == target_heart_rate
