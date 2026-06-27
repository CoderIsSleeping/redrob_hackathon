"""
Feature Engineering Module

Converts raw candidate JSON
into structured features for
the AI ranking pipeline.
"""


def calculate_notice_score(days):
    """
    Convert notice period into a normalized score.

    0 days  -> 1.0
    150 days -> 0.0
    """

    MAX_NOTICE = 150

    days = max(0, min(days, MAX_NOTICE))

    return round(1 - (days / MAX_NOTICE), 3)


def get_experience_bucket(years):
    """
    Categorize experience level.
    """

    if years < 3:
        return "Junior"

    elif years < 8:
        return "Mid"

    else:
        return "Senior"


def has_github_profile(score):
    """
    GitHub score of -1 means
    profile unavailable.
    """

    return score != -1

def normalize_github_score(score):
    """
    Normalize GitHub activity score
    between 0 and 1.
    """

    if score == -1:
        return 0.0

    return round(score / 100, 3)


def calculate_availability_score(open_to_work, notice_score):
    """
    Combine availability signals.
    """

    score = notice_score

    if open_to_work:
        score += 0.3

    return min(round(score, 3), 1.0)

if __name__ == "__main__":

    print(calculate_notice_score(0))
    print(calculate_notice_score(90))
    print(calculate_notice_score(150))

    print(get_experience_bucket(2))
    print(get_experience_bucket(6))
    print(get_experience_bucket(12))

    print(has_github_profile(-1))
    print(has_github_profile(45))

    print(normalize_github_score(-1))
    print(normalize_github_score(80))

    print(calculate_availability_score(True, 0.6))