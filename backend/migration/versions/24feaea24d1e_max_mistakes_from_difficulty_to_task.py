"""max_mistakes from difficulty to task

Revision ID: 24feaea24d1e
Revises: 4530f38b59e2
Create Date: 2024-11-29 11:42:27.566773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '24feaea24d1e'
down_revision: Union[str, None] = '4530f38b59e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('difficulty', 'max_mistakes')
    op.add_column('task', sa.Column('max_mistakes', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'max_mistakes')
    op.add_column('difficulty', sa.Column('max_mistakes', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###