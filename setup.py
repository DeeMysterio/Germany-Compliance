from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in germany_compliance/__init__.py
from germany_compliance import __version__ as version

setup(
	name="germany_compliance",
	version=version,
	description="App to include regional compliance settings for Germany",
	author="Frappe Technologies Private Limited[C",
	author_email="diksha@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
