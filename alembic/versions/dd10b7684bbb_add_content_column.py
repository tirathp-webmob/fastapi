"""Add Content column

Revision ID: dd10b7684bbb
Revises: ea20664014be
Create Date: 2022-02-10 12:00:18.517253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd10b7684bbb'
down_revision = 'ea20664014be'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
            'content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
