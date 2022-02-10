"""Create Post Table

Revision ID: ea20664014be
Revises:
Create Date: 2022-02-10 11:51:42.247535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea20664014be'
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