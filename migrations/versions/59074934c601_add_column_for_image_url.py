"""Add Column for image URL

Revision ID: 59074934c601
Revises: 05aefab0c7ef
Create Date: 2023-03-10 15:37:07.649394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59074934c601'
down_revision = '05aefab0c7ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=400), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
