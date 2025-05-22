import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class DataChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if "iris.csv" in event.src_path:
            print("Data changed, re-running pipeline...")
            os.system("dvc repro")

observer = Observer()
observer.schedule(DataChangeHandler(), path="data/raw", recursive=False)
observer.start()
print("Watching for new data... (Ctrl+C to stop)")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
