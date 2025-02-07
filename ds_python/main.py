import json
import time

from rich.console import Console
from ui import create_ui
from utils import run_stats

console = Console()

while True:
    try:
        stats = run_stats()
        lines = stats.stdout.split('\n')
        with console.status('Waiting for Containers...'):
            while len(lines) <= 1 and '' in lines:
                console.clear()
                time.sleep(1)
                stats = run_stats()
                lines = stats.stdout.split('\n')

        lines = [json.loads(line) for line in lines if line]
        ui = create_ui(lines)
        ui.display()
        time.sleep(0.5)

    except KeyboardInterrupt:
        break
