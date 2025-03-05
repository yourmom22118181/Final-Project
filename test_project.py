import pytest
from project import calculate_sleep_duration, suggest_best_wake_time, analyze_productivity

def test_calculate_sleep_duration():
    assert calculate_sleep_duration("23:00", "07:00") == 8.0
    assert calculate_sleep_duration("22:30", "06:30") == 8.0
    assert calculate_sleep_duration("01:00", "09:00") == 8.0
    assert calculate_sleep_duration("23:30", "04:00") == 4.5
    assert calculate_sleep_duration("23:00", "23:30") == 0.5

def test_suggest_best_wake_time():
    assert suggest_best_wake_time(7.5, [1.5, 3, 4.5, 6, 7.5, 9]) == "Suggested sleep duration: 7.50 hours"
    assert suggest_best_wake_time(6.0, [1.5, 3, 4.5, 6, 7.5, 9]) == "Suggested sleep duration: 6.00 hours"
    assert suggest_best_wake_time(4.5, [1.5, 3, 4.5, 6, 7.5, 9]) == "Suggested sleep duration: 4.50 hours"

def test_analyze_productivity():
    assert "Correlation between sleep and productivity" in analyze_productivity([7, 6.5, 8], [80, 75, 85])
    assert "Insufficient data to analyze." == analyze_productivity([], [])
    assert "Insufficient data to analyze." == analyze_productivity([7, 8], [80])