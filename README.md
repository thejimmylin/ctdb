# ctdb
 
This repository includes many reusable Django apps.

## Overview

#### Clean & simple style

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/login.png" width="60%">

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/news.png" width="60%">

#### with i18 & user-role system

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/i18n.png" width="60%">

#### Diary app

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/diary.png" width="60%">

#### Reminder app

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/reminder.png" width="60%">

#### Log app

<img src="https://github.com/j3ygithub/ctdb/blob/main/docs/img/log.png" width="60%">

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
