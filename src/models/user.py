class User:
    allowed_positions = ["QA", "WORKER", "GALAXY DESTROYER"]  # noqa: RUF012

    def __init__(
        self,
        name="name",
        last_name="last_name",
        employee_id="0",
        employed=True,
        position="Worker",
    ):
        self.__name = name
        self.__last_name = last_name
        self.__id = employee_id
        self.__employed = employed
        self.__position = position

    @property
    def employee_id(self):
        return self.__id

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if new_position in self.allowed_positions:
            self.__position = new_position
        else:
            print("Picked position is not available")

    @property
    def employed(self):
        return self.__employed

    @employed.setter
    def employed(self, employed_status):
        if employed_status == "yes":
            self.__employed = True
        else:
            self.__employed = False

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    def to_dict(self):
        return {
            "name": self.__name,
            "last_name": self.__last_name,
            "employee_id": self.__id,
            "employed": self.__employed,
            "position": self.__position,
        }

    def __repr__(self):
        return f"Name: {self.__name}\nLast name: {self.__last_name}\nid: {self.__id}\nemployed: {self.__employed}\nposition: {self.__position}"
