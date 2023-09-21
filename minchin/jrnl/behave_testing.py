def _mock_getpass(inputs):
    def prompt_return(prompt=""):
        if type(inputs) == str:
            return inputs
        try:
            return next(inputs)
        except StopIteration:
            raise KeyboardInterrupt

    return prompt_return


def _mock_input(inputs):
    def prompt_return(prompt=""):
        try:
            val = next(inputs)
            print(prompt, val)
            return val
        except StopIteration:
            raise KeyboardInterrupt

    return prompt_return


def _mock_time_parse(context):
    original_parse = jrnl.time.parse
    if "now" not in context:
        return original_parse

    def wrapper(input, *args, **kwargs):
        input = context.now if input == "now" else input
        return original_parse(input, *args, **kwargs)

    return wrapper
