import os
import sys

if sys.version_info < (3, 9):
    sys.stderr.write("re-execing " + repr(sys.argv) + " with newer python\n")
    python = os.path.join(os.environ["HOME"], "opt", "python39", "bin", "python3")
    os.execl(python, python, *sys.argv)

import datetime

print(datetime.datetime.now())
print("starting wsgi app")
print("python is", sys.version)

venv_site_packages = os.path.join(
    os.path.dirname(__file__), ".venv", "lib", "python3.9", "site-packages"
)
sys.path.insert(0, venv_site_packages)
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))


from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "website.settings"

application = get_wsgi_application()
