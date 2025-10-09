"""add phone column

Revision ID: 23e1adf2dcff
Revises: 16e41f259738
Create Date: 2025-10-09 13:16:20.129289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23e1adf2dcff'
down_revision: Union[str, Sequence[str], None] = '16e41f259738'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone",sa.Integer()))


def downgrade() -> None:
    op.drop_column("users","phone")
