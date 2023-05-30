"""create table 123

Revision ID: 2f9f347f02a9
Revises: 8ca112b9a076
Create Date: 2023-05-29 21:43:58.016799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9f347f02a9'
down_revision = '8ca112b9a076'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE table1(
            id SERIAL PRIMARY KEY);
        CREATE TABLE table2(
            id SERIAL PRIMARY KEY);
        CREATE TABLE table3(
            id SERIAL PRIMARY KEY);

        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE table3;
        DROP TABLE table2;
        DROP TABLE table1;
        """
    )