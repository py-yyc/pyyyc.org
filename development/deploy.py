#!/usr/bin/env python

""" 
PyYYC website deployment application.

The PyYYC website is hosted as a Github repository using Github pages. The
website is made using the hyde compiler, which this script invokes to generate,
serve and deploy the website.

Usage:
	deploy.py <command> [<args>...]

Options:
	-h --help    Show this screen.
	--version    Show version.

The various commands are:
	compile    Generate the static pages for this website using the Hyde compiler
	serve      Serve this website using a local CherryPy server
	deploy     Deploy this website to Github pages
"""
from docopt import docopt
from plumbum.cmd import hyde, git
from plumbum import local, FG
from settings import DEVELOPMENT_DIR

hyde_with_site = hyde['-s', DEVELOPMENT_DIR]

def deploy():
	with local.cwd('..'):
		git['add', '-A'] & FG
		git['commit'] & FG
		git['push'] & FG

COMMAND_MAP = {
	'compile': lambda: hyde_with_site['-g'] & FG,
	'serve': lambda: hyde_with_site['-w'] & FG,
	'deploy': deploy,
}

if __name__ == '__main__':
	arguments = docopt(__doc__, version='0.1')
	command = arguments['<command>']

	if command not in COMMAND_MAP.keys():
		exit('{command} is not a valid command. See "deploy.py help"'.format(command=command))
	else:
		COMMAND_MAP[command]()
