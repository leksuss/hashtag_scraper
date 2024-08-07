"""set updated_at with onupdate param

Revision ID: d39f68313ff7
Revises: 9e84a35c581c
Create Date: 2024-07-02 13:09:15.753686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd39f68313ff7'
down_revision: Union[str, None] = '9e84a35c581c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'updated_at',
               existing_type=sa.DATE(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'updated_at',
               existing_type=sa.DateTime(timezone=True),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
