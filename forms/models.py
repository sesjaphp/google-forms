from dataclasses import dataclass, field

@dataclass
class Question:
    title: str
    qtype: str
    options: list[str] = field(default_factory=list)
