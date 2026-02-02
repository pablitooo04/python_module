from abc import ABC, abstractmethod
from typing import Any, Optional


class DataProcessor(ABC):
    def __init__(self) -> None:
        print(f"Initialising {self.__class__.__name__}...")

    @abstractmethod
    def process(self, data: Any) -> Optional[str]:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> Optional[str]:
        if self.validate(data):
            print("Validation: Numeric data verified.")
            processed_len = f"Processed {len(data)} numeric values "
            try:
                statistics = f"sum={sum(data)}, avg={sum(data)/len(data)}"
            except ZeroDivisionError as e:
                raise ValueError(e)
            return processed_len + statistics
        else:
            raise ValueError("Validation: Numeric data failed.")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        if not all(isinstance(x, (int, float)) for x in data):
            return False
        if len(data) == 0:
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> Optional[str]:
        if self.validate(data):
            print("Validation: Text data verified.")
            number_of_word = len(data.split(sep=' '))
            statistics = f"{len(data)} characters, {number_of_word} words."
            return "Processed text: " + statistics
        else:
            raise ValueError("Validation: Text data failed.")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> Optional[str]:
        if self.validate(data):
            try:
                keyword = data.split(sep=' ')[0]
            except IndexError:
                raise ValueError("Log must not contain only spaces")
            keyword_t = f"[{''.join(c for c in keyword if c.isalpha())}] "
            print("Validation: Log entry verified.")
            return keyword_t + data
        else:
            raise ValueError("Validation: Log data failed!")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if data == "":
            return False
        if not data.split(sep=' ')[0].isupper():
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    try:
        numeric_processor_1 = NumericProcessor()
        print("Processing data:", [1, 2, 3, 4, 5])
        result = numeric_processor_1.process([1, 2, 3, 4, 5])
        print(numeric_processor_1.format_output(result))
    except ValueError as e:
        print(e)

    print()

    try:
        text_processor_1 = TextProcessor()
        print("Processing data:", "\"Hello Nexus World\"")
        result = text_processor_1.process("Hello Nexus World")
        print(text_processor_1.format_output(result))
    except ValueError as e:
        print(e)

    print()

    try:
        log_processor_1 = LogProcessor()
        print("Processing data:", "\"ERROR: Connection timeout\"")
        result = log_processor_1.process("ERROR: Connection timeout")
        print(log_processor_1.format_output(result))
    except ValueError as e:
        print(e)

    print()

    print("=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...\n")
    data_to_process = [[1, 2, 3, 4, 5],
                       "This is a test",
                       "INFO level level detected: System ready"
                       ]

    processors: list[DataProcessor] = [
        numeric_processor_1,
        log_processor_1,
        text_processor_1
    ]

    try:
        for i, data in enumerate(data_to_process):
            for cl in processors:
                if cl.validate(data):
                    process = cl.process(data)
                    print(f"Result {i + 1}: {cl.format_output(process)}\n")
                    break
            else:
                print(f"No processor could handle: {data}\n")

    except ValueError as e:
        print(e)
