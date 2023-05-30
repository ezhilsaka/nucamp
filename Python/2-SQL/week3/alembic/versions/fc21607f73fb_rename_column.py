"""rename column

Revision ID: fc21607f73fb
Revises: 3d1201d0a531
Create Date: 2023-05-29 21:27:11.731505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc21607f73fb'
down_revision = '3d1201d0a531'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN date_of_birth TO dob;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN dob to date_of_birth;
        """
    )