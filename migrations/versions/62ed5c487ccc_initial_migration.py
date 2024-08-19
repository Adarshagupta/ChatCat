"""Initial migration

Revision ID: 62ed5c487ccc
Revises: 
Create Date: 2024-08-19 11:31:02.078788

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '62ed5c487ccc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api')
    op.drop_table('admin_user')
    op.drop_table('file')
    op.drop_table('chat_log')
    op.drop_table('subscription')
    op.drop_table('context')
    op.drop_table('interaction')
    op.drop_table('chatbot_appearance')
    op.drop_table('chatbot')
    op.drop_table('apis')
    op.drop_table('users')
    with op.batch_alter_table('analytics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('api_key', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('endpoint', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('response_time', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('status_code', sa.Integer(), nullable=False))
        batch_op.drop_column('last_interaction')
        batch_op.drop_column('interaction_count')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('api_keys')
        batch_op.drop_column('is_verified')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('api_keys', sa.TEXT(), autoincrement=False, nullable=True))

    with op.batch_alter_table('analytics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('interaction_count', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('last_interaction', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.drop_column('status_code')
        batch_op.drop_column('response_time')
        batch_op.drop_column('timestamp')
        batch_op.drop_column('endpoint')
        batch_op.drop_column('api_key')

    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    op.create_table('apis',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('key', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='apis_pkey'),
    sa.UniqueConstraint('name', name='apis_name_key')
    )
    op.create_table('chatbot',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('chatbot_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('api_key', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='chatbot_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='chatbot_pkey'),
    sa.UniqueConstraint('api_key', name='chatbot_api_key_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('chatbot_appearance',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('chatbot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('background_color', sa.VARCHAR(length=7), autoincrement=False, nullable=True),
    sa.Column('text_color', sa.VARCHAR(length=7), autoincrement=False, nullable=True),
    sa.Column('font_family', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chatbot_id'], ['chatbot.id'], name='chatbot_appearance_chatbot_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='chatbot_appearance_pkey')
    )
    op.create_table('interaction',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('chatbot_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_input', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('ai_response', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chatbot_id'], ['chatbot.id'], name='interaction_chatbot_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='interaction_pkey')
    )
    op.create_table('context',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='context_pkey')
    )
    op.create_table('subscription',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('plan', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='subscription_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='subscription_pkey')
    )
    op.create_table('chat_log',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('api_key', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('input', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('response', sa.TEXT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='chat_log_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='chat_log_pkey')
    )
    op.create_table('file',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('filename', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('path', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('upload_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='file_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='file_pkey')
    )
    op.create_table('admin_user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='admin_user_pkey'),
    sa.UniqueConstraint('email', name='admin_user_email_key')
    )
    op.create_table('api',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('key', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='api_pkey'),
    sa.UniqueConstraint('name', name='api_name_key')
    )
    # ### end Alembic commands ###
