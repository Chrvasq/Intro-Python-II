class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def __str__(self):
        return f"{self.name} is currently in the {self.current_room.name}."

    def __repr__(self):
        return f"Player(name={self.name}, current_room={self.current_room})"
