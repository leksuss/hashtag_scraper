"""add

Revision ID: f81271075de1
Revises: 655b4eadcbd1
Create Date: 2024-06-26 16:37:34.391551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f81271075de1'
down_revision: Union[str, None] = '655b4eadcbd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'type',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'type',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###
