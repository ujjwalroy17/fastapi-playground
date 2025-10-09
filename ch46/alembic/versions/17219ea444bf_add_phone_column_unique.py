"""add phone column unique

Revision ID: 17219ea444bf
Revises: 23e1adf2dcff
Create Date: 2025-10-09 13:39:39.949714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17219ea444bf'
down_revision: Union[str, Sequence[str], None] = '23e1adf2dcff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.create_unique_constraint("uq_users_phone",["phone"])


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint("uq_users_phone","users",type_='unique')
