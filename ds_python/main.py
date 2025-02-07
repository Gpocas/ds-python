from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from utils import clean_stdout, run_stats

console = Console()
stats = run_stats()
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
            console.print(clear_line)

except KeyboardInterrupt:
    if wait_live is not None:
        wait_live.stop()
    console.print('\nInterrupt by user...')

finally:
    stats.terminate()
    stats.wait()
