from datetime import datetime


class Event:
    def __init__(self, title, location, start_time):
        self.title = title
        self.location = location
        self.start_time = start_time

    def description(self):
        return f"{self.title} | {self.location} | {self.start_time:%Y-%m-%d %H:%M}"


class EventPlanner:
    def __init__(self):
        self.events = []

    def add_event(self, title, location, start_time):
        self.events.append(Event(title, location, start_time))

    def upcoming_events(self):
        return sorted(self.events, key=lambda event: event.start_time)

    def print_schedule(self):
        print("Event Schedule")
        print("==============")

        for event in self.upcoming_events():
            print(event.description())


def main():
    planner = EventPlanner()

    planner.add_event("Project Meeting", "Conference Room", datetime(2026, 8, 10, 9, 30))
    planner.add_event("Client Call", "Online", datetime(2026, 8, 10, 14, 0))
    planner.add_event("Workshop", "Training Center", datetime(2026, 8, 11, 11, 15))

    planner.print_schedule()


if __name__ == "__main__":
    main()
