class CommandHelper:
    @staticmethod
    def get_valid_parameter(data_resources, messages):
        parameter = None

        while parameter is None:
            data_resources_str = [str(item) for item in data_resources]
            print(messages['title'] + "[" + ", ".join(data_resources_str) + "]: ")
            user_input = input(messages['select'])

            parameter = CommandHelper.parse_input(user_input, data_resources)

            if parameter is None:
                print(messages['invalid'])
                parameter = None

        return parameter

    @staticmethod
    def parse_input(value, data_resources):
        try:
            int_value = int(value)
            if int_value in data_resources:
                return int_value
        except ValueError:
            pass

        try:
            float_value = float(value)
            if float_value in data_resources:
                return float_value
        except ValueError:
            pass

        if value in data_resources:
            return value

        return None
