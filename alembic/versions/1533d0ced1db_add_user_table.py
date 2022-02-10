"""Add user table

Revision ID: 1533d0ced1db
Revises: dd10b7684bbb
Create Date: 2022-02-10 12:05:42.313311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1533d0ced1db'
down_revision = 'dd10b7684bbb'
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