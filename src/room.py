class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = "\n"
        output += f"{self.name}\n"
        output += f"{self.description}\n"
        output += "Exits to the: "
        output += " [North] N" if hasattr(self, "n_to") else ""
        output += " [South] S" if hasattr(self, "s_to") else ""
        output += " [East] E" if hasattr(self, "e_to") else ""
        output += " [West] W" if hasattr(self, "w_to") else ""
        output += "\n"

        return output

    def __repr__(self):
        return f"Room(name={self.name}, description={self.description})"
