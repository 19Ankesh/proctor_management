import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proctor_management.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    # Create the superuser and assign role='admin'
    admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'AdminPassword123')
    admin_user.role = 'admin'
    admin_user.is_email_verified = True
    admin_user.save()
    print("Superuser 'admin' created successfully with password 'AdminPassword123'")
else:
    print("Superuser 'admin' already exists.")
