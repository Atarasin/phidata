from enum import Enum
import json
import re
from phi.utils.log import logger


class JSONRectifierError(Enum):
    """
    This class defines the error messages that can occur while rectifying the JSON data.
    """
    INVALID_CONTROL_CHARACTERS = "Invalid control character"
    EXPECTING_COMMA_DELIMITER = "Expecting ',' delimiter"
    EXPECTING_COLON_DELIMITER = "Expecting ':' delimiter"


class JSONRectifier:
    """
    This class is used to rectify the JSON data.
    If the JSON data is not in the correct format, this class can be used to rectify it, according to the error message.
    """
    def __init__(self, remove_whitespaces=True):
        """
        This constructor initializes the JSONRectifier object.
        :param remove_whitespaces: A boolean value indicating whether to remove whitespaces from the JSON data.
        """
        self.remove_whitespaces = remove_whitespaces

    def rectify(self, json_data: str) -> str:
        """
        This method rectifies the JSON data.
        :return: The rectified JSON data.
        """
        # remove leading and trailing whitespaces
        if self.remove_whitespaces:
            json_data = json_data.strip()

        # remove ```json and ``` from the response if present
        if json_data.startswith("```json\n") and json_data.endswith("\n```"):
            json_data = json_data.replace("```json\n", "").replace("\n```", "")

        # replace single quotes with double quotes
        json_data = json_data.replace("'", '"')

        try:
            json_object = json.loads(json_data)
            return json.dumps(json_object)
        except json.JSONDecodeError as e:
            error_message = str(e)
            logger.warning(f"JSON data is not in the correct format. Error message: {error_message}, \nJSON data: {json_data}")
            if JSONRectifierError.INVALID_CONTROL_CHARACTERS.value in error_message:
                # If the JSON data contains invalid control characters, we need to remove them within the range of 0x00-0x1F
                json_data_after = re.sub(r"[\x00-\x1F]+", "", json_data)
                return self.rectify(json_data_after)
            elif JSONRectifierError.EXPECTING_COLON_DELIMITER.value in error_message:
                # If the JSON data is not in the correct format, the error message will contain the word "Expecting ':' delimiter".
                # In this case, we need to find the suitable position to insert a colon, and insert it. 
                index = e.pos
                json_data_after = json_data[:index] + ":" + json_data[index:]
                return self.rectify(json_data_after)
            elif JSONRectifierError.EXPECTING_COMMA_DELIMITER.value in error_message:
                # If the JSON data is not in the correct format, the error message will contain the word "Expecting ',' delimiter".
                # In this case, we need to find the suitable position to insert a comma, and insert it. 
                index = e.pos
                json_data_after = json_data[:index] + "," + json_data[index:]
                return self.rectify(json_data_after)
            else:
                # If the error message is not related to the JSON data format, we cannot rectify it.
                raise e


if __name__ == '__main__':
    rectifier = JSONRectifier()

    # Test case 1: Valid JSON data
    json_data = '  {"name": "John", "age": 30, "city": "New York"}   '
    rectified_json_data = rectifier.rectify(json_data)
    print(rectified_json_data)

    # Test case 2: JSON data with invalid control characters
    json_data = '{"name": "John\u0000", "age": 30, "city": "New York"}'
    rectified_json_data = rectifier.rectify(json_data)
    print(rectified_json_data)

    # Test case 3: JSON data with missing colon
    json_data = '{"name": "John", "age" 30, "city": "New York"}'
    rectified_json_data = rectifier.rectify(json_data)
    print(rectified_json_data)

    # Test case 4: JSON data with missing comma
    json_data = '{"name": "John", "age": 30 "city": "New York"}'
    rectified_json_data = rectifier.rectify(json_data)
    print(rectified_json_data)

    # Test case 5: JSON data with single quotes
    json_data = "{'name': 'John', 'age': 30, 'city': 'New York'}"
    rectified_json_data = rectifier.rectify(json_data)
    print(rectified_json_data)

    # Test case 6: JSON data with ```json and ```
    json_data = "```json\n{'name': 'John', 'age': 30, 'city': 'New York'}\n```"
    rectified_json_data = rectifier.rectify(json_data)
    print(rectified_json_data)
