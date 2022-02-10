"""add content column to post table

Revision ID: 56abb1575549
Revises: 590bbc75c661
Create Date: 2022-02-10 17:27:56.874594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56abb1575549'
down_revision = '590bbc75c661'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass