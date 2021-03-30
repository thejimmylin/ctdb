def get_role(session, user):
    role = session.get('role')
    if role in user.get_available_roles():
        return role
    return {}
