from typing import Any, List, Union, Dict, Optional
from abc import ABC, abstractmethod

def str_is_int(value :str) -> bool:
    try:
        int(value)
    except ValueError:
        return False
    else:
        return True
    
def str_is_float(value :str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    else:
        return True


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}

class SensorStream(DataStream):
    sensors = {"temp", "humidity", "pressure"}

    def __init__(self, stream_id: str) -> None:
        print("Initializing Sensor Stream...")
        if not isinstance(stream_id, str):
            raise ValueError("Error: stream_id must be a str!")
        if stream_id == "":
            raise ValueError("Error: stream_id must not be empty!")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")
        self.stream_id = stream_id
        self.read_count = 0
        self.temperatures = []
        self.avg_temperature = None

    @staticmethod
    def data_is_valid(data_batch: List[Any]) -> None:
        if not isinstance(data_batch, list):
            raise ValueError("Error: data_batch must be a list!")
        if not all(isinstance(data, str) for data in data_batch):
            raise ValueError("Error: data_batch must contain only str!")
        if not all(":" in data for data in data_batch):
            raise ValueError("Error: data batch must contain str -> <data:value>")
        if not all(data.index(":") == data.rindex(":") for data in data_batch):
            raise ValueError("Error: data batch must contain only one ':'")
        if not all(data[:data.index(":")] in SensorStream.sensors for data in data_batch):
            raise ValueError(f"Error: data must be in {SensorStream.sensors}")
        for data in data_batch:
            value = data[data.index(":") + 1:]
            if not (str_is_float(value) or str_is_int(value)):
                raise ValueError("Error: values must be convertible to int")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            SensorStream.data_is_valid(data_batch)
        except ValueError as e:
            raise ValueError(e)
        else:
            for data in data_batch:
                key, value = data[:data.index(":")], data[data.index(":") + 1:]
                if key == "temp" and str_is_float(value):
                        if self.avg_temperature == None:
                            self.temperatures.append(float(value))
                        else:
                            self.temperatures.append(int(value))
                else:
                    self.temperatures.append(int(value))
            self.read_count += len(data_batch)
        
        return "Processing sensor batch: " + str(data_batch)

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        ...

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        if len(self.temperatures) == 0:
            return {"avg_temp": "N/A",
                "read": self.read_count
                }

        return {"avg_temp": round(sum(self.temperatures)/len(self.temperatures), 2),
                "read": self.read_count
                }

class TransactionStream(DataStream):
    ops = {"buy", "sell"}

    def __init__(self, stream_id: str) -> None:
        print("Initializing Transaction Stream...")
        if not isinstance(stream_id, str):
            raise ValueError("Error: stream_id must be a str!")
        if stream_id == "":
            raise ValueError("Error: stream_id must not be empty!")

        print(f"Stream ID: {stream_id}, Type: Financial Data")
        self.stream_id = stream_id
        self.operation_count = 0
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            TransactionStream.data_is_valid(data_batch)
        except ValueError as e:
            print(e)
        else:
            for data in data_batch:
                key, value = data[:data.index(":")], data[data.index(":") + 1:]
                self.operation_count += 1
                if key == "buy":
                    self.net_flow += int(value)
                else:
                    self.net_flow -= int(value)
        return "Processing transaction batch: " + str(data_batch)

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        ...
    
    @staticmethod
    def data_is_valid(data_batch: List[Any]):
        if not isinstance(data_batch, list):
            raise ValueError("Error: data_batch must be a list!")
        if not all(isinstance(data, str) for data in data_batch):
            raise ValueError("Error: data_batch must contain only str!")
        if not all(":" in data for data in data_batch):
            raise ValueError("Error: data batch must contain str -> <data:value>")
        if not all(data.index(":") == data.rindex(":") for data in data_batch):
            raise ValueError("Error: data batch must contain only one separator")
        if not all(data[:data.index(":")] in TransactionStream.ops for data in data_batch):
            raise ValueError(f"Error: data must be in {TransactionStream.ops}")
        for data in data_batch:
            value = data[data.index(":") + 1:]
            if not str_is_int(value):
                raise ValueError("Error: values must be convertible to int")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"net_flow": self.net_flow,
                "ops": self.operation_count
                }

class EventStream(DataStream):
    events = {"login", "error", "logout"}
    def __init__(self, stream_id: str) -> None:
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")
        self.stream_id = stream_id
        self.event_count = 0
        self.errors_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        if EventStream.data_is_valid(data_batch):
            for data in data_batch:
                if data == "error":
                    self.errors_count += 1
                self.event_count += 1

        return "Processing event batch: " + str(data_batch)
        
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        ...

    @staticmethod
    def data_is_valid(data_batch: List[Any]):
        if not isinstance(data_batch, list):
            raise ValueError("Error: data_batch must be a list!")
        if not all(isinstance(data, str) for data in data_batch):
            raise ValueError("Error: data_batch must contain only str!")
        if not all(data in EventStream.events for data in data_batch):
            raise ValueError(f"Error: data must be in {EventStream.events}")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"total_events": self.event_count,
                "errors": self.errors_count
                }

class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)
        else:
            raise ValueError("Error: stream must be a DataStream stream!")

    def process_all(self, data_batches: List[List[Any]]) -> List[str]:
        ...

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    try:
        sensor_001 = SensorStream("SENSOR_001")
        result = sensor_001.process_batch([])
        stats = sensor_001.get_stats()
        print(result)
        print(f"Sensor analysis: {stats.get('read', None)}", end="")
        print(f"readings processed, avg temp: {stats.get('avg_temp')}°C")
    except ValueError as e:
        print(e)

    print()

    try:
        trans_001 = TransactionStream("TRANS_001")
        result = trans_001.process_batch(["buy:100", "sell:150", "buy:75"])
        stats = trans_001.get_stats()
        print(result)
        print(f"Transaction analysis: {stats.get('ops', None)},", end="")
        print(f"operations, net flow: {stats.get('net_flow', None)} units")
    except ValueError as e:
        print(e)
    
    print()

    try:
        event_001 = EventStream("EVENT_001")
        result = event_001.process_batch(["login", "error", "logout"])
        print(result)
        print(f"Event analysis: {stats.get('total_events', None)} events, ", end="")
        print(f"{stats.get('errors', None)} errors recorded")
    except ValueError as e:
        print(e)

