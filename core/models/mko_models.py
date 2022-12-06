# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    number = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
    name = models.CharField(max_length=200)
    filial = models.CharField(max_length=10)
    card = models.ForeignKey('Cards', on_delete=models.CASCADE, blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'

    def __str__(self):
        return str(self.name)


class ApiUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    created_by = models.IntegerField()
    token_valid_period = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brands(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'

    def __str__(self):
        return str(self.name)


class Cards(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=16)
    expire = models.CharField(max_length=4)
    type = models.IntegerField()
    owner = models.CharField(max_length=100)
    balance = models.BigIntegerField()
    hold_amount = models.BigIntegerField()
    phone = models.CharField(max_length=13)
    token = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'

    def __str__(self):
        return str(self.number)


class Clients(models.Model):
    id = models.BigAutoField(primary_key=True)
    application_id = models.CharField(max_length=100)
    client_code = models.CharField(max_length=100)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)
    limit = models.BigIntegerField()
    limit_status = models.IntegerField()
    used_limit = models.BigIntegerField()
    date_expiry = models.DateField()
    pnfl = models.CharField(max_length=14)
    passport = models.CharField(max_length=9, blank=True, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'

    def __str__(self):
        return f"{str(self.first_name)}-{str(self.last_name)}"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class LimitHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    limit = models.BigIntegerField()
    date_expiry = models.DateField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_histories'


class MerchantPeriodHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant = models.ForeignKey('Merchants', on_delete=models.CASCADE)
    period = models.IntegerField()
    percentage = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_period_histories'


class MerchantPeriods(models.Model):
    id = models.BigAutoField(primary_key=True)
    merchant_id = models.IntegerField()
    period = models.IntegerField()
    percentage = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_periods'


class Merchants(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchants'

    def __str__(self):
        return str(self.name)


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', on_delete=models.CASCADE, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', on_delete=models.CASCADE, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchants, on_delete=models.CASCADE)
    period = models.IntegerField()
    percentage = models.IntegerField()
    sender_card = models.CharField(max_length=100)
    cost = models.BigIntegerField()
    amount = models.BigIntegerField()
    date = models.DateField()
    is_transaction = models.IntegerField()
    status = models.IntegerField()
    tr_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, on_delete=models.CASCADE, primary_key=True)
    role = models.ForeignKey('Roles', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Tokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    api_user_id = models.IntegerField()
    token = models.CharField(unique=True, max_length=255)
    token_expires_at = models.DateTimeField()
    is_active = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'


class TransactionAccounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='receiver')
    amount = models.BigIntegerField()
    transactionid = models.IntegerField(db_column='transactionId')  # Field name made lowercase.
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_accounts'


class Transactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender_card = models.CharField(max_length=100)
    receiver_card = models.CharField(max_length=100)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    cost_amount = models.BigIntegerField()
    percentage = models.IntegerField()
    status = models.IntegerField()
    is_sent = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    token = models.CharField(max_length=100, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    theme = models.CharField(max_length=30)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
