# Advanced Features and Security

## Permissions and Groups Setup

This Django application uses custom permissions and groups to control access
to different parts of the system.

### Custom Permissions
Permissions are defined in the `Article` model:

- can_view
- can_create
- can_edit
- can_delete

These permissions are created automatically when migrations are run.

### Groups Configuration

Groups are managed through the Django admin panel:

#### Viewers
- can_view

#### Editors
- can_view
- can_create
- can_edit

#### Admins
- can_view
- can_create
- can_edit
- can_delete

### Permission Enforcement
Permissions are enforced in views using Django’s `@permission_required`
decorator. Users attempting to access unauthorized views will receive a
403 Forbidden response.

### Testing
Create test users and assign them to different groups via the admin panel.
Log in as each user to verify that permissions are enforced correctly.

