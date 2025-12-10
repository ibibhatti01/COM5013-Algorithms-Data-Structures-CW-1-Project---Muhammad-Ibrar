# tests.py

from contact_book import ContactBook
from contact import Contact


def run_basic_tests() -> None:
    book = ContactBook()

    # Empty structure tests
    assert book.find_by_email("none@example.com") is None
    assert book.list_sorted_by_name() == []

    # Add and find
    alice = Contact(name="Alice", email="alice@example.com", phone="123")
    assert book.add_contact(alice) is True
    assert book.add_contact(alice) is False  # duplicate email
    assert book.find_by_email("alice@example.com") == alice

    # Update
    assert book.update_contact("alice@example.com", phone="999") is True
    assert book.find_by_email("alice@example.com").phone == "999"

    # Search by name
    bob = Contact(name="Bob", email="bob@example.com")
    book.add_contact(bob)
    matches = book.find_by_name("Alice")
    assert len(matches) == 1 and matches[0].name == "Alice"

    # Remove
    assert book.remove_contact("alice@example.com") is True
    assert book.remove_contact("alice@example.com") is False

    print("All basic tests passed.")


if __name__ == "__main__":
    run_basic_tests()
