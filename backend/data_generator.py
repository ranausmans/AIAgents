import random
import time

class TrafficDataGenerator:
    def __init__(self):
        self.intersections = [
            'Times Square',
            'Columbus Circle',
            'Union Square',
            'Herald Square',
            'Washington Square Park'
        ]
        self.traffic_levels = ['Low', 'Medium', 'High']

    def generate_traffic_data(self):
        data = {}
        for intersection in self.intersections:
            vehicles = random.randint(0, 100)
            average_speed = random.randint(10, 60)
            traffic_level = self.calculate_traffic_level(vehicles, average_speed)
            
            data[intersection] = {
                'traffic_level': traffic_level,
                'vehicles': vehicles,
                'average_speed': average_speed
            }
        return data

    def calculate_traffic_level(self, vehicles, average_speed):
        if vehicles <= 20 and average_speed >= 40:
            return 'Low'
        elif vehicles >= 60 or average_speed <= 20:
            return 'High'
        else:
            return 'Medium'

    def generate_continuous_data(self):
        while True:
            yield self.generate_traffic_data()
            time.sleep(5)  # Generate new data every 5 seconds
