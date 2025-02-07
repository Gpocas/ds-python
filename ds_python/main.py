import json

from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from utils import clean_stdout, run_stats

console = Console()
stats = run_stats()

first_iter = True
wait_live = None  # Variável para armazenar o objeto Live quando em "wait"

try:
    for line in iter(stats.stdout.readline, ''):
        if line == '\x1b[J\x1b[H\x1b[H\x1b[K\n':
            if wait_live is None:
                console.clear()
                wait_live = Live(
                    Spinner(
                        'dots', text='Wait for containers...', style='green'
                    ),
                    console=console,
                    refresh_per_second=10,
                )
                wait_live.start()
            else:
                wait_live.update(
                    Spinner(
                        'dots', text='Wait for containers...', style='green'
                    )
                )
        else:
            if wait_live is not None:
                wait_live.stop()
                wait_live = None
                console.clear()

            clear_line = clean_stdout(line)
            if clear_line:
                dict_value = json.loads(clear_line)
                nome = dict_value['Name']
                cpu = dict_value['CPUPerc']
                mem = dict_value['MemPerc']

                console.print(dict_value)

except KeyboardInterrupt:
    if wait_live is not None:
        wait_live.stop()
    console.print('\nInterrupt by user...')

finally:
    stats.terminate()
    stats.wait()
