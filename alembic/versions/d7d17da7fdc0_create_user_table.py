"""create user table

Revision ID: d7d17da7fdc0
Revises: 
Create Date: 2023-02-13 23:03:40.888577

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd7d17da7fdc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=50), nullable=False),
                    sa.Column('password', sa.String(length=200), nullable=False),
                    sa.Column('city', sa.String(length=40), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('user')
