"""db

Revision ID: b92a48dd69b9
Revises: 8b238867e568
Create Date: 2023-08-29 09:32:08.331938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b92a48dd69b9'
down_revision = '8b238867e568'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mms_lite', sa.Column('style', sa.String(length=512), nullable=True))
    op.add_column('mms_lite', sa.Column('setting', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mms_lite', 'setting')
    op.drop_column('mms_lite', 'style')
    # ### end Alembic commands ###