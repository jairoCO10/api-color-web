"""Adding Tables

Revision ID: 4038eab1cfe9
Revises: e4f8b73521d3
Create Date: 2023-10-18 17:15:47.784972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4038eab1cfe9'
down_revision = 'e4f8b73521d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('colores', sa.Column('id_proyecto', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('colores', 'id_proyecto')
    # ### end Alembic commands ###
