from typing import Protocol, Any, Optional


class ProcessingStage(Protocol): #blueprint
    def process(self, data: Any) -> Any:
        pass

class JSONInputStage(ProcessingStage): #input <- '{key:value,key2:value2}'
    def process(self, data: Any) -> Any:
        data_cropped = data[1:-1]
        couples = data_cropped.split(",")
        output = {key.strip(): value.strip()
                  for couple in couples
                  for key, value in [couple.split(":")]}
        return output

class JSONTransformStage(ProcessingStage):
    def process(self, data: Any) -> Any:
        output = {}
        for key, value in data.items():
            if JSONTransformStage.string_to_int(value):
                output[key] = int(value)
            elif JSONTransformStage.string_to_float(value):
                output[key] = float(value)
            else:
                output[key] = value()
        return output

    @staticmethod
    def string_to_int(string: str) -> bool:
        try:
            int(string)
        except ValueError:
            return False
        else:
            return True
        
    @staticmethod
    def string_to_float(string: str) -> bool:
        try:
            float(string)
        except ValueError:
            return False
        else:
            return True
    
class JSONOutputStage(ProcessingStage):
    def process(self, data: Any) -> Any:
        #exemple
        output = f"Processed temperature reading"
        temp = data.get("temp", None)

if __name__ == "__main__":
    input = "{test:2}"
    input2 = "{test:2.0}"
    
    json = JSONInputStage()
    
    first = json.process(input)
    first2 = json.process(input2)
    
    print(first)
    print(first2)

    second = JSONTransformStage().process(first)
    second2 = JSONTransformStage().process(first2)

    print(second)
    print(second2)