"""empty message

Revision ID: 31b52c56182c
Revises: c33472886410, dcc0489f7a2f
Create Date: 2025-05-27 12:40:17.220032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31b52c56182c'
down_revision: Union[str, None] = ('c33472886410', 'dcc0489f7a2f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
