"""Adding Tables

Revision ID: e4f8b73521d3
Revises: cea25b263f06
Create Date: 2023-10-18 17:00:10.368789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4f8b73521d3'
down_revision = 'cea25b263f06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proyectos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_proyecto', sa.String(length=100), nullable=True),
    sa.Column('descripcion_proyecto', sa.Text(), nullable=True),
    sa.Column('desarrollador_back', sa.String(length=250), nullable=True),
    sa.Column('desaarrollador_front', sa.String(length=250), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.Column('version', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proyectos_id'), 'proyectos', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proyectos_id'), table_name='proyectos')
    op.drop_table('proyectos')
    # ### end Alembic commands ###
