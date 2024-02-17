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
    check()

def on_modified(event):
    check()

def on_moved(event):
    check()

def sort():
    for imgDownload in os.listdir(downloads):
        if imgDownload.endswith('.jpg') or imgDownload.endswith('.png') or imgDownload.endswith('.gif') or imgDownload.endswith('.webp') or imgDownload.endswith('.jpeg') or imgDownload.endswith('.raw'):
            shutil.move(downloads + '/' + imgDownload, 'D:\DownloadedImages/' + imgDownload)
            return 1

    for zipDownload in os.listdir(downloads):
        if zipDownload.endswith('.zip'):
            shutil.move(downloads + '/' + zipDownload, 'D:\DownloadedZIPS/' + zipDownload)
            return 1

    for pdfDownload in os.listdir(downloads):
        if pdfDownload.endswith('.pdf') or pdfDownload.endswith('.docx'):
            shutil.move(downloads + '/' + pdfDownload, 'D:\DownloadedPDF/' + pdfDownload)
            return 1
        
    for mediaDownload in os.listdir(downloads):
        if mediaDownload.endswith('.mp4') or mediaDownload.endswith('.mp3') or mediaDownload.endswith('.mov') or mediaDownload.endswith('.avi'):
            shutil.move(downloads + '/' + mediaDownload, 'D:\DownloadedMedia/' + mediaDownload)
            return 1
        
    for exeDownload in os.listdir(downloads):
        if exeDownload.endswith('.exe'):
            shutil.move(downloads + '/' + exeDownload, 'D:\DownloadedEXE/' + exeDownload)
            return 1
        
def misc():
    for miscDownload in os.listdir(downloads):
        shutil.move(downloads + '/' + miscDownload, 'D:\DownloadedMisc/' + miscDownload)

def check():
    if not sort():
        misc()

my_event_handler.on_created = on_created
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, downloads, recursive=go_recursively)

my_observer.start()
try:
    while True:
        check()
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()