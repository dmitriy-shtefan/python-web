from .models import Profile


def is_teacher(user):
    return (
        user.is_authenticated
        and hasattr(user, 'profile')
        and user.profile.role == Profile.ROLE_TEACHER
    )


def is_student(user):
    if user.is_authenticated and hasattr(user, 'profile'):
        print(user.profile)
        if hasattr(user.profile, 'role'):
            return user.profile.role == Profile.ROLE_STUDENT
    return False
