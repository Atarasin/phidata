import json
from phi.utils.log import logger


class JSONRectifier:
    """
    This class is used to rectify the JSON data.
    If the JSON data is not in the correct format, this class can be used to rectify it, according to the error message.
    """
    def __init__(self, json_data: str):
        self.json_data = json_data

    def rectify(self) -> str:
        """
        This method rectifies the JSON data.
        :return: The rectified JSON data.
        """
        try:
            json_data = json.loads(self.json_data)
            return json.dumps(json_data)
        except json.JSONDecodeError as e:
            error_message = str(e)
            logger.warning(f"JSON data is not in the correct format. Error message: {error_message}")
            if "Expecting ',' delimiter" in error_message:
                # error_message = "Expecting ',' delimiter: line 1 column 10 (char 9)"
                # If the JSON data is not in the correct format, the error message will contain the word "Expecting ',' delimiter".
                # In this case, we need to find the suitable position to insert a comma, and insert it. 
                match_text = "(char "
                position = error_message.find(match_text)
                index = int(error_message[position+len(match_text):-1])
                self.json_data = self.json_data[:index] + "," + self.json_data[index:]
                return self.rectify()
                
            else:
                # If the error message is not related to the JSON data format, we cannot rectify it.
                raise e


if __name__ == '__main__':
    json_data = "{ \"name\": \"John\", \"age\": 30, \"city\": \"New York\" }"

    rectifier = JSONRectifier(json_data)
    rectified_json_data = rectifier.rectify()

    print(rectified_json_data)

    json_data = "{ \"name\": \"John\" \"age\": 30, \"city\": \"New York\" }"

    rectifier = JSONRectifier(json_data)
    rectified_json_data = rectifier.rectify()

    print(rectified_json_data)