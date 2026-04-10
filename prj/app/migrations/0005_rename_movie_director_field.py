from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_review_profile_actor_birth_date_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Director',
            new_name='director',
        ),
    ]
