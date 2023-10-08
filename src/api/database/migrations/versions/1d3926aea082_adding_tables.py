"""Adding Tables

Revision ID: 1d3926aea082
Revises: ac0e8725fa7e
Create Date: 2023-10-08 13:44:02.727823

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1d3926aea082'
down_revision = 'ac0e8725fa7e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuarios', 'id_nivel')
    op.drop_column('usuarios', 'pendiente')
    op.drop_column('usuarios', 'fechapass')
    op.drop_column('usuarios', 'fechaacceso')
    op.drop_column('usuarios', 'codempresa')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('codempresa', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('usuarios', sa.Column('fechaacceso', mysql.DATETIME(), nullable=True))
    op.add_column('usuarios', sa.Column('fechapass', mysql.DATETIME(), nullable=True))
    op.add_column('usuarios', sa.Column('pendiente', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('usuarios', sa.Column('id_nivel', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
