from fabric.api import local, cd
from settings import HYDE_EXECUTABLE, DEVELOPMENT_DIR

def compile():
	"""
	Compiles the website using hyde into static files.
	"""
	local("{hyde} -g -s {here}".format(
		hyde=HYDE_EXECUTABLE,
		here=DEVELOPMENT_DIR,
	))

def serve():
	"""
	Serves the website locally using a cherrypy server provided by hyde.
	"""
	local("{hyde} -w -k -s {here}".format(
		hyde=HYDE_EXECUTABLE,
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