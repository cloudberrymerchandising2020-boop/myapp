from myapp.main import build_greeting


def test_greeting_with_name():
    assert build_greeting("Kenneth") == "Hello, Kenneth!"


def test_greeting_strips_whitespace():
    assert build_greeting("  Kenneth  ") == "Hello, Kenneth!"


def test_greeting_with_empty_name():
    assert build_greeting("") == "Hello, stranger!"


def test_greeting_with_only_whitespace():
    assert build_greeting("   ") == "Hello, stranger!"
