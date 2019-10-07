from distutils.core import setup

majv = 1
minv = 0

setup(
	name = 'demon',
	version = "%d.%d" %(majv,minv),
	description = "Overlaying module to the daemonize module with a few more controlling features to make it easier to use",
	author = "Colin ML Burnett",
	author_email = "cmlburnett@gmail.com",
	url = "",
	packages = ['demon'],
	package_data = {'demon': ['demon/__init__.py']},
	classifiers = [
		'Programming Language :: Python :: 3.7'
	]
)
