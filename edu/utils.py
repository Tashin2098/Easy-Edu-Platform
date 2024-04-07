def is_teacher(user):
    # Assuming teachers are identified by belonging to a specific group
    return user.groups.filter(name='TEACHER').exists()
