import time
import win32evtlog
import re
import shutil

from tools.data_folder import DataFolder

FLSPEW_MATCH = r"\?.*FLSpew\.txt"


class CrashManager:

    def __init__(self):
        self.current_time = int(time.time())

    def register_crash(self):
        data_folder = DataFolder()
        if event := self.get_event():
            folder = data_folder.get_crashes_root() / str(self.current_time)
            folder.mkdir()

            event_data_file = folder / 'win_event.txt'
            event_data_file.write_text(event, encoding='utf-8')

            match = re.search(FLSPEW_MATCH, event)
            if match:
                log_file = match.group().replace('?\\', '')
                flspew_file = folder / 'flspew.txt'
                shutil.copyfile(log_file, flspew_file)

            current_autosave = data_folder.get_autosave()
            if current_autosave.exists():
                keeped_autosave = folder / 'AutoSave.fl'
                shutil.copyfile(current_autosave, keeped_autosave)



    def get_event(self):
        hand = win32evtlog.OpenEventLog('localhost', 'application')
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = 1
        while events:
            print('iter')
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            for event in events:
                print(event.StringInserts)
                try:
                    combined_string = '\n\n'.join(list(event.StringInserts))
                    if 'freelancer' in combined_string.lower():
                        return combined_string
                except TypeError:
                    continue
