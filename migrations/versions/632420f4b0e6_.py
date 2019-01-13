"""empty message

Revision ID: 632420f4b0e6
Revises: 
Create Date: 2019-01-13 17:31:12.283958

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '632420f4b0e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('feature_ibfk_1', 'feature', type_='foreignkey')
    op.drop_constraint('feature_ibfk_2', 'feature', type_='foreignkey')
    op.drop_column('feature', 'user_id')
    op.drop_column('feature', 'client_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feature', sa.Column('client_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('feature', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('feature_ibfk_2', 'feature', 'client', ['client_id'], ['id'])
    op.create_foreign_key('feature_ibfk_1', 'feature', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
