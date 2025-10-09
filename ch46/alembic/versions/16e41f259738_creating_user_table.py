"""creating user table

Revision ID: 16e41f259738
Revises: 
Create Date: 2025-10-08 16:59:40.495685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16e41f259738'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id",sa.Integer,primary_key=True),
        sa.Column("name",sa.String(50),nullable=False),
        sa.Column("email",sa.String ,nullable=False,unique=True),

    )


def downgrade() -> None:
    op.drop_table('users')
