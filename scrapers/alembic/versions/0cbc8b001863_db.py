"""db

Revision ID: 0cbc8b001863
Revises: b92a48dd69b9
Create Date: 2023-08-29 10:58:30.026855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cbc8b001863'
down_revision = 'b92a48dd69b9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kiwi_l1', sa.Column('description', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kiwi_l1', 'description')
    # ### end Alembic commands ###
