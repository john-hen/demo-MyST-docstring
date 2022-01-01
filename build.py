from subprocess import run

process = run(['sphinx-build', 'docs', 'HTML'])
