from time import sleep

from dashing import HGauge, VSplit

lt_vs = [
    VSplit(  # ui.items[0]
        HGauge(title='RAM'),  # ui.items[0].items[0]
        HGauge(title='CPU'),  # ui.items[0].items[1]
        title='Postgres',
        border_color=3,
    ),
    VSplit(  # ui.items[1]
        HGauge(title='RAM'),  # ui.items[1].items[0]
        HGauge(title='CPU'),  # ui.items[1].items[1]
        title='Nginx',
        border_color=3,
    ),
]


ui = VSplit(*lt_vs)

while True:
    try:
        ui.display()
        ui.items[0].items[1].value = 50
        sleep(0.5)
    except KeyboardInterrupt():
        break
