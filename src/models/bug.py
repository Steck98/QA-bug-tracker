class Bug:
    allowed_status = ["TODO", "INPROGRESS", "DONE"]  # noqa: RUF012
    allowed_priorities = ["HIGH", "MEDIUM", "LOW"]  # noqa: RUF012

    def __init__(
        self,
        title="title",
        bug_id="0",
        status="status",
        priority="priority",
        description="description",
        assigned_to="assigned",
        reported_by="reported",
    ):
        self.__title = title
        self.__bug_id = bug_id
        self.__status = status
        self.__priority = priority
        self.__description = description
        self.__assigned_to = assigned_to
        self.__reported_by = reported_by

    @property
    def title(self):
        return self.__title

    @property
    def bug_id(self):
        return self.__bug_id

    @property
    def reported_by(self):
        return self.__reported_by

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, new_priority):
        self.__priority = new_priority

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def assigned_to(self):
        return self.__assigned_to

    @assigned_to.setter
    def assigned_to(self, new_assigned_to):
        self.__assigned_to = new_assigned_to

    def __repr__(self):
        return (
            f"Title: {self.__title}\n"
            f"Bug ID: {self.__bug_id}\n"
            f"Status: {self.__status}\n"
            f"Priority: {self.__priority}\n"
            f"Description: {self.__description}\n"
            f"Assigned to: {self.__assigned_to}\n"
            f"Reported by: {self.__reported_by}"
        )
