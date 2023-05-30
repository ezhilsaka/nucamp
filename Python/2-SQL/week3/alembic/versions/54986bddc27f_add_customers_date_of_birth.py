"""add customers date_of_birth

Revision ID: 54986bddc27f
Revises: 38c3c3349086
Create Date: 2023-05-29 20:43:30.239983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54986bddc27f'
down_revision = '38c3c3349086'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
