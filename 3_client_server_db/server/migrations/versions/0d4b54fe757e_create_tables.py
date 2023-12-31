"""create tables

Revision ID: 0d4b54fe757e
Revises: 
Create Date: 2023-11-16 15:31:49.073821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d4b54fe757e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('difficulty', sa.String(), nullable=False),
    sa.Column('range_min', sa.Integer(), nullable=False),
    sa.Column('range_max', sa.Integer(), nullable=False),
    sa.Column('secret_number', sa.Integer(), nullable=True),
    sa.Column('is_over', sa.Boolean(), nullable=True),
    sa.CheckConstraint('range_min <= range_max', name=op.f('ck_games_min_max_range')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games'))
    )
    op.create_table('rounds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('range_min', sa.Integer(), nullable=False),
    sa.Column('range_max', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('guess', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('range_min <= range_max', name=op.f('ck_rounds_min_max_range')),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_rounds_game_id_games')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_rounds'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rounds')
    op.drop_table('games')
    # ### end Alembic commands ###
