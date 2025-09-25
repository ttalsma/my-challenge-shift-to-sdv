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

import sys, time, logging
import json

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher

logger = logging.getLogger("acc_publisher")
stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

def create_adas_dict(counter):
    distance_reset_value = 100
#    velocity_result_value = ...
    result = {"distance": distance_reset_value-counter,
              "velocity": 120}
    return result

if __name__ == "__main__":
    logger.info("Starting ecal example publisher app...")

    # Initialize eCAL
    ecal_core.initialize(sys.argv, "eCAL Example Publisher App")

    # Create a publisher that sends dummy data to the "hello_topic" topic
    pub = StringPublisher("acc_topic")
    
    # Send the dummy data every 0.5 seconds
    counter = 0
    while ecal_core.ok():
        acc_data = create_adas_dict(counter)
        acc_data_2_send =json.dumps(acc_data)
        pub.send(acc_data_2_send)
        counter += 1
        time.sleep(1)
    
    # finalize eCAL API
    ecal_core.finalize()
    