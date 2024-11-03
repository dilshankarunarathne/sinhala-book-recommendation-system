from bson import ObjectId

class User:
    def __init__(self, _id=None, username=None, password=None, email=None, gender=None, age=None,
                 interested_categories=None):
        self._id = ObjectId(_id) if _id else None
        self.username = username
        self.password = password
        self.email = email
        self.gender = gender
        self.age = age
        self.interested_categories = interested_categories

    def to_dict(self):
        return {
            "_id": str(self._id) if self._id else None,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "gender": self.gender,
            "age": self.age,
            "interested_categories": self.interested_categories
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data.get("_id"),
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            gender=data.get("gender"),
            age=data.get("age"),
            interested_categories=data.get("interested_categories")
        )
