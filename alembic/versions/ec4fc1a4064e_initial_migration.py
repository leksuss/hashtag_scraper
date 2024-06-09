"""Initial migration

Revision ID: ec4fc1a4064e
Revises: 
Create Date: 2024-06-10 01:38:47.742707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec4fc1a4064e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtag',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_hashtag_id'), 'hashtag', ['id'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('social_network', sa.Enum('VK', 'IG', name='socialnetworksenum'), nullable=False),
    sa.Column('link', sa.String(length=200), nullable=False),
    sa.Column('date_published', sa.Date(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=False),
    sa.Column('hashtag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hashtag_id'], ['hashtag.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link')
    )
    op.create_index(op.f('ix_post_id'), 'post', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_id'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_hashtag_id'), table_name='hashtag')
    op.drop_table('hashtag')
    # ### end Alembic commands ###