from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 4


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
def test_days_left_negative_when_overdue():
    
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    result = days_left(due, today)
    assert result == -2


def test_is_urgent_true_when_due_tomorrow():
    
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    result = is_urgent(due, today)
    assert result is True


def test_is_urgent_true_at_exact_limit():
   
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)  # exactly 2 days away
    result = is_urgent(due, today)
    assert result is False 


def test_is_urgent_false_when_overdue():
    
    today = date(2026, 10, 19)
    due = date(2026, 10, 15)
    result = is_urgent(due, today)
    assert result is False


def test_sort_by_due_puts_soonest_first():
    
    tasks = [
        {"title": "later", "due": date(2026, 10, 30)},
        {"title": "soonest", "due": date(2026, 10, 20)},
        {"title": "middle", "due": date(2026, 10, 25)},
    ]
    result = sort_by_due(tasks)
    assert result[0]["title"] == "soonest"


def test_completion_rate_zero_when_no_tasks():
    
    done, total = 0, 0
    result = completion_rate(done, total)
    assert result == 0.0


def test_completion_rate_one_of_three():
   
    done, total = 1, 3
    result = completion_rate(done, total)
    assert result == 33.3
