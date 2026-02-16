try:
    from pydantic import BaseModel, ValidationError, model_validator, Field
except ImportError:
    print("pydantic mmodule not found !")
    exit(1)

from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    """Enum for different types of alien contact. """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Model for logging alien contact reports with complex
    validation rules.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def custom_validator(self) -> "AlienContact":
        """
        Custom validation rules for AlienContact.
        - contact_id must start with 'AC'
        - Physical contacts must be verified
        - Telepathic contacts require at least 3 witnesses
        - Strong signals (> 7.0) require a received message
        """

        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) require a received message")

        return self


def main() -> None:
    """
    Main function to test the AlienContact model with
    valid and invalid data.
    """
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp='2025-01-01',
            contact_type="radio",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
    else:
        print("Valid contact report:")
        print("ID:", alien_contact.contact_id)
        print("Type:", alien_contact.contact_type)
        print("Location:", alien_contact.location)
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print("Witnesses:", alien_contact.witness_count)
        print(f"Message:'{alien_contact.message_received}'")
    print()
    print("======================================")
    print("Expected validation error:")
    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            contact_type="telepathic",
            timestamp='2025-01-01',
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
    else:
        print("Valid contact report:")
        print("ID:", alien_contact.contact_id)
        print("Type:", alien_contact.contact_type)
        print("Location:", alien_contact.location)
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print("Witnesses:", alien_contact.witness_count)
        print(f"Message:'{alien_contact.message_received}'")


if __name__ == "__main__":
    main()
