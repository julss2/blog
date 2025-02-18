"""Initial migration

Revision ID: aa94ff8f572e
Revises: 
Create Date: 2024-06-24 19:58:08.512841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa94ff8f572e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('content', sa.Text(), nullable=True))
    op.drop_index('ix_posts_question_text', table_name='posts')
    op.create_index(op.f('ix_posts_content'), 'posts', ['content'], unique=False)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    op.drop_column('posts', 'question_text')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('question_text', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_index(op.f('ix_posts_content'), table_name='posts')
    op.create_index('ix_posts_question_text', 'posts', ['question_text'], unique=False)
    op.drop_column('posts', 'content')
    op.drop_column('posts', 'title')
    # ### end Alembic commands ###
