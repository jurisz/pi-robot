#!/usr/bin/env python3

from datetime import date, datetime

today = date.today()
now = datetime.now()

fttime = now.strftime("%Y-%m-%d_%H:%M")

name = "sample-%s-%s"

for i in range(5):
    print(name % (fttime, i))
