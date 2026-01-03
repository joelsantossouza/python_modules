from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    """Enumeration of all types of contacts"""
    radio: str = "radio"
    visual: str = "visual"
    physical: str = "physical"
    telepathic: str = "telepathic"


class AlienContact(BaseModel):
    """
    AlientContact type definition, rejecting
    invalid inputs to its creation
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate(self):
        if self.contact_id[:2] != "AC":
            raise ValueError(
                f"Contact_id '{self.contact_id}' must start with 'AC'"
            )
        if self.contact_type == ContactType.physical \
                and not self.is_verified:
            raise ValueError(
                "For physical contacts, reports must be verified"
            )
        if self.contact_type == ContactType.telepathic \
                and self.witness_count < 3:
            raise ValueError(
                "For telepathic contacts require at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) must include received messages"
            )
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    inputs: list[dict] = [
        # ✅ Valid geral contact
        {
            "ID": "AC_2024_001",
            "Timestamp": "2025-12-30",
            "Location": "Area 51, Nevada",
            "Type": "radio",
            "Signal": 8.5,
            "Duration": 45,
            "Witnesses": 5,
            "Message": "Greetings from Zeta Reticuli",
            "Is verified": None
        },
        # ✅ Valid radio contact
        {
            "ID": "AC_2024_001",
            "Timestamp": "2025-12-30T12:00:00",
            "Location": "Area 51, Nevada",
            "Type": "radio",
            "Signal": 6.5,
            "Duration": 45,
            "Witnesses": 5,
            "Message": None,
            "Is verified": False
        },
        # ✅ Valid physical contact (must be verified)
        {
            "ID": "AC_2024_002",
            "Timestamp": "2025-12-30T13:00:00",
            "Location": "Roswell, New Mexico",
            "Type": "physical",
            "Signal": 5.0,
            "Duration": 30,
            "Witnesses": 2,
            "Message": None,
            "Is verified": True
        },
        # ❌ Invalid contact_id (does not start with AC)
        {
            "ID": "XX_2024_003",
            "Timestamp": "2025-12-30T14:00:00",
            "Location": "Area 52",
            "Type": "visual",
            "Signal": 3.0,
            "Duration": 20,
            "Witnesses": 1,
            "Message": None,
            "Is verified": False
        },
        # ❌ Invalid physical contact (not verified)
        {
            "ID": "AC_2024_004",
            "Timestamp": "2025-12-30T15:00:00",
            "Location": "Nevada Desert",
            "Type": "physical",
            "Signal": 4.0,
            "Duration": 25,
            "Witnesses": 3,
            "Message": None,
            "Is verified": False
        },
        # ❌ Telepathic contact with less than 3 witnesses
        {
            "ID": "AC_2024_005",
            "Timestamp": "2025-12-30T16:00:00",
            "Location": "Deep Space",
            "Type": "telepathic",
            "Signal": 6.0,
            "Duration": 50,
            "Witnesses": 2,
            "Message": "Hello from Zeta",
            "Is verified": False
        },
        # ❌ Strong signal but no message received (None)
        {
            "ID": "AC_2024_006",
            "Timestamp": "2025-12-30T17:00:00",
            "Location": "Mars Base",
            "Type": "radio",
            "Signal": 8.5,
            "Duration": 40,
            "Witnesses": 4,
            "Message": None,
            "Is verified": False
        },
        # ❌ Strong signal but no message received (Empty)
        {
            "ID": "AC_2024_006",
            "Timestamp": "2025-12-30T17:00:00",
            "Location": "Mars Base",
            "Type": "radio",
            "Signal": 8.5,
            "Duration": 40,
            "Witnesses": 4,
            "Message": "",
            "Is verified": False
        },
        # ✅ Valid telepathic contact
        {
            "ID": "AC_2024_007",
            "Timestamp": "2025-12-30T18:00:00",
            "Location": "Alpha Centauri",
            "Type": "telepathic",
            "Signal": 5.5,
            "Duration": 60,
            "Witnesses": 3,
            "Message": "Greetings",
            "Is verified": True
        },
    ]
    for i, input in enumerate(inputs):
        print("======================================")
        print(f"Test {i + 1}:")
        try:
            result: AlienContact = AlienContact(
                contact_id=input["ID"],
                timestamp=input["Timestamp"],
                location=input["Location"],
                contact_type=input["Type"],
                signal_strength=input["Signal"],
                duration_minutes=input["Duration"],
                witness_count=input["Witnesses"],
                message_received=input["Message"],
                is_verified=input["Is verified"],

            )
            for key, value in result.model_dump().items():
                print(f"{key}: {value}")
        except Exception as e:
            print("ERRORS: ", end="")
            for error in e.errors():
                print(error['msg'], end=", ")
            print()
