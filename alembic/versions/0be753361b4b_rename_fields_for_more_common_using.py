"""rename fields for more common using

Revision ID: 0be753361b4b
Revises: d39f68313ff7
Create Date: 2024-07-05 16:49:45.840762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0be753361b4b'
down_revision: Union[str, None] = 'd39f68313ff7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author_id', sa.Integer(), nullable=True))
    op.add_column('post', sa.Column('resource_id', sa.Integer(), nullable=True))
    op.drop_constraint('uq_publication', 'post', type_='unique')
    op.create_unique_constraint('uq_publication', 'post', ['author_id', 'resource_id', 'type'])
    op.drop_column('post', 'resource_vk_id')
    op.drop_column('post', 'author_vk_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author_vk_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('resource_vk_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint('uq_publication', 'post', type_='unique')
    op.create_unique_constraint('uq_publication', 'post', ['author_vk_id', 'resource_vk_id', 'type'])
    op.drop_column('post', 'resource_id')
    op.drop_column('post', 'author_id')
    # ### end Alembic commands ###
