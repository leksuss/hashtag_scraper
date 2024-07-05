"""add updated_at in hashtag model

Revision ID: 9e84a35c581c
Revises: d58f956d9630
Create Date: 2024-07-01 17:44:04.232298

"""
from datetime import date
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e84a35c581c'
down_revision: Union[str, None] = 'd58f956d9630'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('updated_at', sa.Date(), nullable=False, server_default=sa.func.current_date()))
    op.alter_column('post', 'updated_at', server_default=None)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'updated_at')
    # ### end Alembic commands ###
