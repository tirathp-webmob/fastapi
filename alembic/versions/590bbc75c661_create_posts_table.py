"""create posts table

Revision ID: 590bbc75c661
Revises: 
Create Date: 2022-02-10 17:25:19.489802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '590bbc75c661'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass