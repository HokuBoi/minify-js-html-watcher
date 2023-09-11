#!/usr/bin/env python3
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from css_html_js_minify import html_minify

OUTPUT_FILE = "minified_output.js"

class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch

    def run(self):
        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        observer.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_modified(event):
        if event.src_path.endswith(OUTPUT_FILE):
            return

        if event.is_directory:
            return

        file_extension = os.path.splitext(event.src_path)[1]
        minified_content = None

        if file_extension == '.js':
            with open(event.src_path, 'r') as f:
                content = f.read()
            minified_content = terser_minify(content)

        elif file_extension == '.html':
            with open(event.src_path, 'r') as f:
                content = f.read()
            minified_content = html_minify(content)

        if minified_content is not None:
            update_minified_file(event.src_path, minified_content)

def terser_minify(js_content):
    result = subprocess.run(['terser'], input=js_content, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        return js_content
    return result.stdout

def update_minified_file(path, content):
    timestamp = datetime.now().strftime("%H:%M:%S")
    file_name = os.path.basename(path)
    character_count = len(content)
    header = f"//{file_name} {timestamp} {character_count}\n"
    cleaned_content = content.rstrip("\n")
    with open(OUTPUT_FILE, 'a') as f:
        f.write(header + cleaned_content + "\n\n")



if __name__ == "__main__":
    directory_to_watch = os.path.abspath('.')
    print("Minify watcher script running...")
    w = Watcher(directory_to_watch)
    w.run()
