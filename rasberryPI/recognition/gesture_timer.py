import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.duration = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            self.duration = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = None
        self.duration = 0
        self.running = False

    def get_duration(self):
        if self.running:
            return time.time() - self.start_time
        return self.duration

    def is_running(self):
        return self.running
