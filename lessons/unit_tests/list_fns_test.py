from lessons.unit_tests.list_fns import get_first, get_and_remove_first, remove_first


def test_get_first() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


def test_remove_first_return_value() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


def test_remove_first_behavior() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]
