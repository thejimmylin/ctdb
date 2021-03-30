def get_role(session, user):
    default_role = user.profile.get_default_role()
    if not default_role:
        default_role = {'pk': 0, 'name': ''}
    role = session.get('role', default_role)
    if role not in user.get_available_roles():
        return default_role
    return role
