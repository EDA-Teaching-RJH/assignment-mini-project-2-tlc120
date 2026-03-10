class Student:
    def __init__(self, name, degree, foundation):
        if not name:
            raise ValueError("Missing name")
        if degree not in ["ECE", "BIO", "MECH", "EEE"]:
            raise ValueError("Invalid degree")
        self.name = name
        self.degree = degree
        self.foundation = foundation

    def __str__(self):
        return f"{self.name} from {self.degree}"
