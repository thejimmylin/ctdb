# ctdb
 
This repository includes many reusable Django apps.

## Overview

#### Clean & simple style

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/login.png" width="80%">

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/news.png" width="80%">

#### with i18 & user-role system

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/i18n.png" width="80%">

#### Diary app

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/diary.png" width="80%">

#### Reminder app

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/reminder.png" width="80%">

#### Log app

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/log.png" width="80%">

## Source code overview

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
git clone https://github.com/j3ygithub/ctdb /Users/jimmy_lin/repos/ctdb
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

[https://github.com/j3ygithub/](https://github.com/j3ygithub/)

## Contributing

1. Fork it (<https://github.com/j3ygithub/ctdb/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
