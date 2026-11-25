from simulation.result import Result


def test_result_members_and_values() -> None:
    assert Result.PREY_ESCAPED.value == "Prey ran into infinity"
    assert Result.FIGHT_HAPPENED.value == "Some R-rated things have happened"
    assert set(Result) == {Result.PREY_ESCAPED, Result.FIGHT_HAPPENED}