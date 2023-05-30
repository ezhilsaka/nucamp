"""drop constrain

Revision ID: 8ca112b9a076
Revises: c07d48ab2313
Create Date: 2023-05-29 21:41:15.322919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca112b9a076'
down_revision = 'c07d48ab2313'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE orders
        DROP CONSTRAINT fk_orders_customers;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE orders
        ADD CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE CASCADE;
        """
    )