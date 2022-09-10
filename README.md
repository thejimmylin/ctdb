# ctdb
 
A Python web application containing many reusable modules.

## Overview

#### The login page.

<img src="https://github.com/thejimmylin/ctdb/blob/main/docs/img/ctdb-login-4704x2522-raw.png" width="80%">

#### Reminder, one of the applications.

<img src="https://github.com/thejimmylin/ctdb/blob/main/docs/img/ctdb-reminder-4704x2522-raw.png" width="80%">

#### Every application works with i18n.

<img src="https://github.com/thejimmylin/ctdb/blob/main/docs/img/ctdb-diary-i18n-4704x2522-raw.png" width="80%">

#### Every data change will be logged.

<img src="https://github.com/thejimmylin/ctdb/blob/main/docs/img/ctdb-log-4704x2522-raw.png" width="80%">

## Some snippets

#### Auth backend `AuthWithUsernameOrEmailBackend`.

```python
class AuthWithUsernameOrEmailBackend(ModelBackend):
    """
    Override method authenticate, make it possible to login with Email.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            try:
                user = User._default_manager.get_by_natural_key(username)
            except User.DoesNotExist:
                user = User._default_manager.get(email=username)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
```

#### Overrided `permission_required` decorator.
```python
def permission_required(perm, login_url=None, raise_exception=False, exception=PermissionDenied):
    """
    Override Django's built-in permission_required decorator.
    Act like permission_required but let you set a optional `exception` argument.
    You can set it to Http404 instead of the default PermissionDenied.
    """
    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm,)
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise exception
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url=login_url)
```

There are other reusable source code like `flushmigrations`, `dumpdatautf8` Django management commands.

## Installation

git clone this repo
```bash
git clone https://github.com/thejimmylin/ctdb /Users/jimmy_lin/repos/ctdb
```

build venv & install packages with pip
```bash
python3 -m venv /Users/jimmy_lin/repos/ctdb/.venv
source /Users/jimmy_lin/repos/ctdb/.venv
pip install -r /Users/jimmy_lin/repos/ctdb/requirements/dev.txt
```

Make DB migrations
```bash 
python3 /Users/jimmy_lin/repos/ctdb/manage.py makemigrations
python3 /Users/jimmy_lin/repos/ctdb/manage.py migrate
```

## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/thejimmylin/](https://github.com/thejimmylin/)

## Contributing

1. Fork it (<https://github.com/thejimmylin/ctdb/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
