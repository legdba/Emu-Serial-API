#!/usr/bin/env python3
from emu import *
from datetime import datetime, timezone
import sys
import traceback

emu_instance = emu('/dev/ttyACM0')
emu_instance.start_serial()

if __name__ == '__main__':
  try:
      while True:

        emu_instance.get_instantaneous_demand('5s')
        time.sleep(5)
        now = datetime.now(timezone.utc).astimezone().isoformat()
        instantaneous_demand = int(emu_instance.InstantaneousDemand.Demand, 16)

        emu_instance.get_current_summation_delivered()
        time.sleep(5)
        current_summation_delivered = int(emu_instance.CurrentSummationDelivered.SummationDelivered, 16)

        l = "{ts} {instantaneous_demand} {current_summation_delivered}".format(ts=now, instantaneous_demand=instantaneous_demand, current_summation_delivered=current_summation_delivered)
        print(l, file=sys.stdout)
  except:
    traceback.print_exc()

  emu_instance.stop_serial()

