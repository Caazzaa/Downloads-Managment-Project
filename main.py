import os, shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

downloads = os.path.expanduser("~")+"/Downloads/"

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    sort()

def on_modified(event):
    sort()

def on_moved(event):
    sort()

def sort():
    for download in os.listdir(downloads):
        if download.endswith('.jpg') or download.endswith('.png') or download.endswith('.gif') or download.endswith('.webp') or download.endswith('.jpeg') or download.endswith('.raw') or download.endswith('.ase'):
            shutil.move(downloads + '/' + download, 'D:\DownloadedImages/' + download)

        elif download.endswith('.zip'):
            shutil.move(downloads + '/' + download, 'D:\DownloadedZIPS/' + download)

        elif download.endswith('.pdf') or download.endswith('.docx'):
            shutil.move(downloads + '/' + download, 'D:\DownloadedPDF/' + download)

        elif download.endswith('.mp4') or download.endswith('.mp3') or download.endswith('.mov') or download.endswith('.avi'):
            shutil.move(downloads + '/' + download, 'D:\DownloadedMedia/' + download)

        elif download.endswith('.exe'):
            shutil.move(downloads + '/' + download, 'D:\DownloadedEXE/' + download)

        else:
            shutil.move(downloads + '/' + download, 'D:\DownloadedMisc/' + download)

my_event_handler.on_created = on_created
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, downloads, recursive=go_recursively)

my_observer.start()
try:
    while True:
        sort()
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()