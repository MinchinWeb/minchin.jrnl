from minchin.jrnl.time import parse as jrnl_time_pase


def _mock_getpass(inputs):
    def prompt_return(prompt=""):
        # if type(inputs) == str:
        if isinstance(inputs, str):
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
    original_parse = jrnl_time_pase
    if "now" not in context:
        return original_parse

    def wrapper(my_input, *args, **kwargs):
        my_input = context.now if my_input == "now" else my_input
        return original_parse(my_input, *args, **kwargs)

    return wrapper
