"""add foreign key to posts table

Revision ID: e3a0eaec3c20
Revises: 95ba6dc8eca2
Create Date: 2024-05-03 21:44:47.993058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3a0eaec3c20'
down_revision: Union[str, None] = '95ba6dc8eca2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'],
                          ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint(constraint_name='post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass