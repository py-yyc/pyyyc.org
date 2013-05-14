from fabric.api import local, cd
from settings import DEVELOPMENT_DIR

def compile():
	"""
	Compiles the website using hyde into static files.
	"""
	local("hyde -g -s {here}".format(
		here=DEVELOPMENT_DIR,
	))

def serve():
	"""
	Serves the website locally using a cherrypy server provided by hyde.
	"""
	local("hyde -w -s {here}".format(
		here=DEVELOPMENT_DIR,
	))

def deploy():
	"""
	Pushes the latest version of the website to Github.
	"""
	compile()
	with cd('..'):
		local('git add -A')
		local('git commit')
		local('git push')		