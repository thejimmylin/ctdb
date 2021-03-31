def get_role(session, user):
    role = session.get('role')
    if role in user.profile.get_available_roles():
        return role
    return {}
