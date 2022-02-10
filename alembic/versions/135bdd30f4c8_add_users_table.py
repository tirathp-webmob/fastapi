"""add users table

Revision ID: 135bdd30f4c8
Revises: 56abb1575549
Create Date: 2022-02-10 17:28:57.447725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '135bdd30f4c8'
down_revision = '56abb1575549'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass