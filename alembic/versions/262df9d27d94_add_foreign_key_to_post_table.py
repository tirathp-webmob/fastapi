"""add foreign key to post table

Revision ID: 262df9d27d94
Revises: 135bdd30f4c8
Create Date: 2022-02-10 17:30:09.689667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '262df9d27d94'
down_revision = '135bdd30f4c8'
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