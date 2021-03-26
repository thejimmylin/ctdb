# ctdb
 
This repository includes many reusable Django apps.

## Overview

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/login" width="60%">

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/news" width="60%">

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/diary" width="60%">

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/i18n" width="60%">

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/reminder" width="60%">


## Installation

git clone
```
git clone https://github.com/j3ygithub/ctdb /Users/jimmy_lin/repos/ctdb
```

venv & pip
```
python3 -m venv /Users/jimmy_lin/repos/ctdb/.venv
source /Users/jimmy_lin/repos/ctdb/.venv
pip install -r /Users/jimmy_lin/repos/ctdb/requirements/dev.txt
```

DB migrate
```
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
