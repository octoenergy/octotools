# octotools - Utilities for the UK energy market from Octopus Energy

_This repo is deprecated. Its functionality has been merged into
[xocto](https://github.com/octoenergy/xocto)_

This repo groups together a bunch of useful utilities for the UK energy market, made with love by the Octopus Energy team.

CI status:

[![CircleCI](https://circleci.com/gh/octoenergy/octotools/tree/master.svg?style=svg)](https://circleci.com/gh/octoenergy/octotools/tree/master)


## Contributing

Create and activate a virtualenv then:

    $ make

Test package with:

    $ make test

and:

    $ make lint  

Release to PyPI by:

1. Bumping the version in `setup.py`

2. Running: 

        $ make publish
