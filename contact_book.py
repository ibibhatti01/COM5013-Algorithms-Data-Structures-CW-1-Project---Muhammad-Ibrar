# contact_book.py

from typing import Dict, List, Optional
from contact import Contact
from algorithms import linear_search


class ContactBook:
    """
    Stores contacts by email using a hash table (dict).
    Provides methods to search and list contacts.
    """

    def __init__(self) -> None:
        self._contacts_by_email: Dict[str, Contact] = {}

    # --- Core operations ---

    def add_contact(self, contact: Contact) -> bool:
        """
        Add a new contact.
        Returns False if email already exists (no overwrite), True otherwise.
        """
        if contact.email in self._contacts_by_email:
            return False
        self._contacts_by_email[contact.email] = contact
        return True

    def update_contact(self, email: str, **fields) -> bool:
        """
        Update an existing contact's fields by email.
        Example: update_contact("a@b.com", phone="123")
        """
        contact = self._contacts_by_email.get(email)
        if contact is None:
            return False

        for key, value in fields.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
        return True

    def remove_contact(self, email: str) -> bool:
        """Remove a contact by email. Returns True if removed, False if not found."""
        if email in self._contacts_by_email:
            del self._contacts_by_email[email]
            return True
        return False

    # --- Search operations ---

    def find_by_email(self, email: str) -> Optional[Contact]:
        """O(1) average case using dict lookup."""
        return self._contacts_by_email.get(email)

    def find_by_name(self, name: str) -> List[Contact]:
        """
        Linear search by name over dictionary values.
        Case-insensitive and returns all matching contacts.
        O(n) time.
        """
        lowered = name.lower()
        return linear_search(
            list(self._contacts_by_email.values()),
            lambda c: c.name.lower() == lowered
        )

    # --- Listing / sorting ---

    def list_all(self) -> List[Contact]:
        """Return all contacts in arbitrary order."""
        return list(self._contacts_by_email.values())

    def list_sorted_by_name(self) -> List[Contact]:
        """
        Return contacts sorted by name using Python's built-in
        Timsort (O(n log n) worst case).
        """
        return sorted(self._contacts_by_email.values(), key=lambda c: c.name.lower())
