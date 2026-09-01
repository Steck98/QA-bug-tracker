import pytest

from src.models.bug import Bug

# ==================================================
# KONSTRUKTOR
# ==================================================


@pytest.mark.parametrize(
    "title, bug_id, status, priority, description, assigned_to, reported_by",
    [
        (
            "QBT-11 Bug",
            "2031",
            "To Do",
            "High",
            "Testing bug for automation tests",
            "Rafał",
            "Rafał",
        )
    ],
)
def test_bug_class(
    title, bug_id, status, priority, description, assigned_to, reported_by
):
    bug = Bug(
        title=title,
        bug_id=bug_id,
        status=status,
        priority=priority,
        description=description,
        assigned_to=assigned_to,
        reported_by=reported_by,
    )
    assert bug.title == title
    assert bug.bug_id == bug_id
    assert bug.status == status
    assert bug.priority == priority
    assert bug.description == description
    assert bug.assigned_to == assigned_to
    assert bug.reported_by == reported_by


# ==================================================
# GETTERY
# ==================================================


@pytest.fixture
def bug_fixture():
    return Bug(
        title="QBT-11 Bug",
        bug_id="2031",
        status="To Do",
        priority="High",
        description="Testing bug for automation tests",
        assigned_to="Rafał",
        reported_by="Rafał",
    )


def test_get_bug_title(bug_fixture):
    assert bug_fixture.title == "QBT-11 Bug"


def test_get_bug_id(bug_fixture):
    assert bug_fixture.bug_id == "2031"


def test_get_bug_status(bug_fixture):
    assert bug_fixture.status == "To Do"


def test_get_bug_priority(bug_fixture):
    assert bug_fixture.priority == "High"


def test_get_bug_description(bug_fixture):
    assert bug_fixture.description == "Testing bug for automation tests"


def test_get_bug_assigned_to(bug_fixture):
    assert bug_fixture.assigned_to == "Rafał"


def test_get_bug_reported_by(bug_fixture):
    assert bug_fixture.reported_by == "Rafał"


# ==================================================
# SETTERY
# ==================================================


@pytest.mark.parametrize("status", ["TODO", "INPROGRESS", "DONE"])
def test_set_bug_status(bug_fixture, status):
    bug_fixture.status = status
    assert status == bug_fixture.status


@pytest.mark.parametrize("new_priority", ["HIGH", "MEDIUM", "LOW"])
def test_set_bug_priority(bug_fixture, new_priority):
    bug_fixture.priority = new_priority
    assert bug_fixture.priority == new_priority


@pytest.mark.parametrize(
    "new_description",
    ["First testing description", "Second testing description!@!  ", "        "],
)
def test_set_bug_description(bug_fixture, new_description):
    bug_fixture.description = new_description
    assert bug_fixture.description == new_description


@pytest.mark.parametrize("assigned_to", ["Rafał", "Tom", "Angelika", "Robert Jr."])
def test_set_bug_assigned_to(bug_fixture, assigned_to):
    bug_fixture.assigned_to = assigned_to
    assert bug_fixture.assigned_to == assigned_to


# ==================================================
# TO DICT
# ==================================================


def test_bug_to_dict(bug_fixture):
    bug_dict = bug_fixture.to_dict()
    assert bug_dict == {
        "title": "QBT-11 Bug",
        "bug_id": "2031",
        "status": "To Do",
        "priority": "High",
        "description": "Testing bug for automation tests",
        "assigned_to": "Rafał",
        "reported_by": "Rafał",
    }


# ==================================================
# REPR
# ==================================================


def test_bug_repr(bug_fixture):
    assert repr(bug_fixture) == (
        f"Title: {bug_fixture.title}\n"
        f"Bug ID: {bug_fixture.bug_id}\n"
        f"Status: {bug_fixture.status}\n"
        f"Priority: {bug_fixture.priority}\n"
        f"Description: {bug_fixture.description}\n"
        f"Assigned to: {bug_fixture.assigned_to}\n"
        f"Reported by: {bug_fixture.reported_by}"
    )
