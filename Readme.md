# haip.config

[![License](https://img.shields.io/github/license/haipdev/jira.svg)](LICENSE)
[![Build Status](https://travis-ci.org/haipdev/jira.svg?branch=master)](https://travis-ci.org/haipdev/jira)

haip.jira is a simple module to communicate with JIRA REST API.

## Features

-   **get**: get JIRA issue by key

## Getting Started

### Installing

```sh
pip install haip-jira
```

or from source:

```sh
git clone https://github.com/haipdev/jira.git
```

### Example

#### config-files

/path-to-my-config-dir/jira.yml

```yaml
jira:
    url: https://myjira.domain.com/rest/api/latest
    username: user
    password: pass
    timeout: 10
```

#### python implementation

```python
import haip.config as config
import haip.jira as jira

config.load('/path-to-my-config-dir', 'dev')
issue = jira.get('ISSUE-01')
```

## Running the tests

Tests are written using pytest and located in the "tests" directory.

```sh
pytest tests
```

## Contributing

Feel free to use and enhance this project. Pull requests are welcome.

## Authors

-   **Reinhard Hainz** - _Initial work_ - [haipdev](https://github.com/haipdev)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Dependencies

-   [haip-config](https://github.com/haipdev/config)
