import pytest
from src.app.main.database import Role

from .presets.role import role_metrics


@pytest.fixture
def cleanup(database):
    yield
    try:
        database.session.query(Role).delete()
        database.session.commit()
    except:
        database.session.rollback()


@pytest.mark.parametrize(
    (
        "name",
        "can_triage_jobs",
        "can_edit_settings",
        "can_create_users",
        "can_create_groups",
        "can_edit_roles",
        "can_manage_infrastructure",
    ),
    role_metrics,
)
def test_create_model_object(
    name,
    can_triage_jobs,
    can_edit_settings,
    can_create_users,
    can_create_groups,
    can_edit_roles,
    can_manage_infrastructure,
    database,
    cleanup,
):

    new_role = Role(
        name=name,
        can_triage_jobs=can_triage_jobs,
        can_edit_settings=can_edit_settings,
        can_create_users=can_create_users,
        can_create_groups=can_create_groups,
        can_edit_roles=can_edit_roles,
        can_manage_infrastructure=can_manage_infrastructure,
    )
    database.session.add(new_role)
    database.session.commit()
