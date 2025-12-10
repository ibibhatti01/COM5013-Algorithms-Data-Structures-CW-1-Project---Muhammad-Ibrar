# contact.py

from dataclasses import dataclass

@dataclass
class Contact:
    """Represents a single contact."""
    name: str
    email: str
    phone: str = ""
    address: str = ""

    def __str__(self) -> str:
        return f"{self.name} <{self.email}> ({self.phone}) ({self.address})"
