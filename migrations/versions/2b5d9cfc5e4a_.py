"""empty message

Revision ID: 2b5d9cfc5e4a
Revises: 23e786b7c1d8
Create Date: 2021-03-03 15:55:19.482284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b5d9cfc5e4a'
down_revision = '23e786b7c1d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audiobook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('narrator', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('podcast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=True),
    sa.Column('host', sa.String(length=100), nullable=True),
    sa.Column('participants', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    op.drop_table('podcast')
    op.drop_table('audiobook')
    # ### end Alembic commands ###
