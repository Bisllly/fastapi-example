"""add content column to posts table

Revision ID: 46b151e5ec56
Revises: 59c8f57ab777
Create Date: 2024-05-03 20:05:13.155037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b151e5ec56'
down_revision: Union[str, None] = '59c8f57ab777'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
