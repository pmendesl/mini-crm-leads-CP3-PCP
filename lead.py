from datetime import date

class Lead:
    STAGES = ["novo"]

    def __init__(self, name: str, company: str, email: str, stage: str = "novo", created: str = None):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = created if created else date.today().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            company=data["company"],
            email=data["email"],
            stage=data["stage"],
            created=data["created"],
        )

    def __repr__(self):
        return f"Lead(name='{self.name}', email='{self.email}', stage='{self.stage}')"

    def __str__(self):
        return f"Nome: {self.name}, Empresa: {self.company}, E-mail: {self.email}, Estágio: {self.stage}"
