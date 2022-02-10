"""Add foreign key to post table

Revision ID: 5542785c995e
Revises: 1533d0ced1db
Create Date: 2022-02-10 12:13:11.425057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5542785c995e'
down_revision = '1533d0ced1db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass