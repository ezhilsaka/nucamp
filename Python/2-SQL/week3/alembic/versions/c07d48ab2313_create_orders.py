"""create orders

Revision ID: c07d48ab2313
Revises: fc21607f73fb
Create Date: 2023-05-29 21:33:35.605460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c07d48ab2313'
down_revision = 'fc21607f73fb'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE orders(
            id SERIAL PRIMARY KEY,
            dollar_amount_spent NUMERIC,
            customer_id INT NOT NULL, 
            CONSTRAINT fk_orders_customers
            FOREIGN KEY(customer_id)
            REFERENCES customers(id)
            ON DELETE CASCADE
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE orders;
        """
    )