#!/usr/bin/env python
import sys
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

def get_errors(args):
  errors = list()
  if not len(args) == 3:
    errors.append('args length missmatch.')
    return errors
  elif not os.path.exists(os.path.abspath(args[1])) or not os.path.exists(os.path.abspath(args[2])):
    errors.append('file is not found.')
  return errors

import shutil

class HugoHandler(FileSystemEventHandler):

  def __init__(self, file_path, target):
    super(HugoHandler, self).__init__()
    self.file_path = file_path
    self.ignore_dir = '{}{}{}'.format(self.file_path, os.path.sep, 'public')
    self.target = target

  def on_created(self, event):
    print('{} has been created.'.format(event.src_path))
#    if not event.src_path.startswith(self.ignore_dir):
#      os.system('cd {} & hugo'.format(self.file_path))

  def on_modified(self, event):
    if event.is_directory:
      return
    if not event.src_path.startswith(self.ignore_dir):
      print('{} has been modified.'.format(event.src_path))
      os.system('cd {} & hugo'.format(self.file_path))
      if os.path.exists(self.target):
        shutil.rmtree(self.target)
      shutil.copytree(self.ignore_dir, self.target)

  def on_deleted(self, event):
    if event.is_directory:
      return
    if not event.src_path.startswith(self.ignore_dir):
      print('{} has been deleted.'.format(event.src_path))
      os.system('cd {} & hugo'.format(self.file_path))
      if os.path.exists(self.target):
        shutil.rmtree(self.target)
      shutil.copytree(self.ignore_dir, self.target)

def main(file_path, target_path):
  while True:
    event_handler = HugoHandler(file_path, target_path)
    observer = Observer()
    observer.schedule(event_handler, file_path, recursive=True)
    observer.start()
    try:
      while True:
        time.sleep(1)
    except KeyboardInterrupt:
      observer.stop()
    observer.join()

if __name__ == '__main__':
  args = sys.argv
  errors = get_errors(args)
  if len(errors):
    print('\n'.join(errors))
    sys.exit(1)
  file_path = os.path.abspath(args[1])
  target_path = os.path.abspath(abs[2])
  main(file_path, target_path)