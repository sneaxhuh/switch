"""Allow subagent steps in session activity.

Revision ID: ab802e19c401
Revises: f68b679599ab
"""

from alembic import op

revision = "ab802e19c401"
down_revision = "f68b679599ab"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint("ck_session_activity_items_kind", "session_activity_items")
    op.create_check_constraint(
        "ck_session_activity_items_kind",
        "session_activity_items",
        "kind IN ('turn', 'user-message', 'assistant-message', 'tool-activity', 'subagent', 'notice')",
    )


def downgrade() -> None:
    op.execute(
        "UPDATE session_activity_items SET kind = 'tool-activity' WHERE kind = 'subagent'"
    )
    op.drop_constraint("ck_session_activity_items_kind", "session_activity_items")
    op.create_check_constraint(
        "ck_session_activity_items_kind",
        "session_activity_items",
        "kind IN ('turn', 'user-message', 'assistant-message', 'tool-activity', 'notice')",
    )
