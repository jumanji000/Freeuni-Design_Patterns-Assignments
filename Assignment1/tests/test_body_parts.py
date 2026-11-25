from simulation.body_parts import PowerModifier, Claws, Teeth

def test_claws_modifier() -> None:
    small_modifier: PowerModifier = Claws.SMALL
    medium_modifier: PowerModifier = Claws.MEDIUM
    large_modifier: PowerModifier = Claws.LARGE

    assert small_modifier.modify_power(10) == 20
    assert medium_modifier.modify_power(10) == 30
    assert large_modifier.modify_power(10) == 40
    assert large_modifier.modify_power(0) == 0


def test_teeth_modifier() -> None:
    low_modifier: PowerModifier = Teeth.LOW
    medium_modifier: PowerModifier = Teeth.MEDIUM
    high_modifier: PowerModifier = Teeth.HIGH

    assert low_modifier.modify_power(10) == 13
    assert medium_modifier.modify_power(10) == 16
    assert high_modifier.modify_power(10) == 19
    assert high_modifier.modify_power(0) == 9


def test_body_parts_descriptions() -> None:
    assert Claws.SMALL.description == "Small Claws"
    assert Claws.MEDIUM.description == "Medium Claws"
    assert Claws.LARGE.description == "Large Claws"
    assert Teeth.LOW.description == "Low Teeth Sharpness"
    assert Teeth.MEDIUM.description == "Medium Teeth Sharpness"
    assert Teeth.HIGH.description == "High Teeth Sharpness"