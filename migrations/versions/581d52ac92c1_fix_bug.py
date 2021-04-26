"""fix bug

Revision ID: 581d52ac92c1
Revises: ab24ef482647
Create Date: 2021-04-19 18:23:09.415724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '581d52ac92c1'
down_revision = 'ab24ef482647'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flasky_group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_group_and_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_group_and_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_menu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_operation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=True),
    sa.Column('prefix_url', sa.String(length=300), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_operation_log',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.Column('operation_content', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('operation_time', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('permission_type', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_permission_menu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_permission_operation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('operation_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_permission_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flasky_user_and_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flasky_user_and_role')
    op.drop_table('flasky_user')
    op.drop_table('flasky_role')
    op.drop_table('flasky_permission_role')
    op.drop_table('flasky_permission_operation')
    op.drop_table('flasky_permission_menu')
    op.drop_table('flasky_permission')
    op.drop_table('flasky_operation_log')
    op.drop_table('flasky_operation')
    op.drop_table('flasky_menu')
    op.drop_table('flasky_group_and_user')
    op.drop_table('flasky_group_and_role')
    op.drop_table('flasky_group')
    # ### end Alembic commands ###
