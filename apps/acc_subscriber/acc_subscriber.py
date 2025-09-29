# Copyright (c) 2024 Elektrobit Automotive GmbH and others

# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# SPDX-License-Identifier: Apache-2.0

import sys, time, logging, json

import ecal.core.core as ecal_core
from ecal.core.subscriber import StringSubscriber

logger = logging.getLogger("acc_subscriber") #ank-logs <file> as a command
stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO) #debug, info, warning, error/fatal, in this case we only print INFO or higher
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

class Car:
    def __init__(self, name:str):
        self.name = name
        self.velocity = 140 
        self.dangerous_distance = 70
        temp_name = self.name + "/acc_topic"
        print("registering for topic" + temp_name)
        self.sub = StringSubscriber(temp_name)
        self.sub.set_callback(callback)
    def get_name(self):
        return self.name
    def set_velocity(self,ego_speed):
        self.velocity = ego_speed
        logger.info(f"The ego speed is {self.velocity}") #previously print()
    def is_too_close(self,distance):
        if distance >= self.dangerous_distance:
            return False
        else:
            return True
    def acc_function(self,distance,other_speed):
        if self.is_too_close(distance) == True:
            logger.info(f"Too close to car ahead")
            self.set_velocity(other_speed)
        else:
            logger.info("Distance OK")

class CarFleet:
    def __init__(self):
        self.fleet = []
    def add_car(self,car:Car):
        self.fleet.append(car)
    def add_multiple_cars(self, cars:list):
        for name in cars:
            car_fleet.add_car(Car(name))
    def show_fleet(self, car:Car):
        for car in self.fleet:
            print(car.get_name())
    # def add_cars_from_database(self, path:str):
    #     with open(path) as file:
    #         for line in file:
                # print(line.rstrip()[2])
                # tmpname = 

# Callback for receiving messages
def callback(topic_name, msg, time):
    try:
        acc_data_2_rec = json.loads(msg)
        # logger.info(f"Received: {msg}")
        logger.info(acc_data_2_rec) #entire dict, items with brackets
        car_1.acc_function(acc_data_2_rec["distance"],acc_data_2_rec["velocity"])
    except Exception as e:
        logger.error(f"Error: {e}") #with higher severity

if __name__ == "__main__":
    logger.info("Starting ecal example subscriber app...")
    # car_1 = Car("car_tessa")
    car_fleet = CarFleet()
    car_fleet.add_car(Car("car_tessa"))
    car_fleet.add_car(Car("car_max"))
    car_fleet.add_car(Car("blue_car"))

    car_name_list = ["Fritz",
                     "Diana",
                     "Dianas-lover"]
    car_fleet.add_cars_from_database("/workspaces/shift2sdv/apps/acc_subscriber/cardatabase.txt")


    # Initialize eCAL
    ecal_core.initialize(sys.argv, "eCAL Example Subscriber app")

    # Create a subscriber that listens to the "hello_topic" eCAL topic
    # sub = StringSubscriber("acc_topic")

    # Set the Callback
    # sub.set_callback(callback)
    
    # Just don't exit
    while ecal_core.ok():
        time.sleep(0.5)
    
    # finalize eCAL API
    ecal_core.finalize()