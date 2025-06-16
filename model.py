# model.py

class Contact:
    def __init__(self, contact_id: int, name: str, phone: str, comment: str = ""):
        self.id = contact_id
        self.name = name.strip()
        self.phone = phone.strip()
        self.comment = comment.strip()

    def __str__(self):
        return f"ID: {self.id} | Имя: {self.name} | Телефон: {self.phone} | Комментарий: {self.comment}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "comment": self.comment
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            contact_id=data["id"],
            name=data["name"],
            phone=data["phone"],
            comment=data.get("comment", "")
        )