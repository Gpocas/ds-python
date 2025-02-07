import re
from subprocess import PIPE, Popen

COMMAND_STATS = ['docker', 'stats', '--format', 'json']
ANSI_ESPACE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')


def run_stats():
    return Popen(COMMAND_STATS, stdout=PIPE, universal_newlines=True)


def clean_stdout(line: str):
    return ANSI_ESPACE.sub('', line).strip()
