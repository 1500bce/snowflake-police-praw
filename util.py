# filename: my_input.py

def get_time_of_day(hour):
    if 0 <= hour < 6:
        time_of_day = "nightly"
    elif 6 <= hour < 12:
        time_of_day = "daily"
    elif 12 <= hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    return time_of_day


def get_snowflake_words():
    return [
        "AM I THE ONLY ONE",
        "AKO LANG BA",
        "DOES ANYBODY ELSE",
        "DOES ANYONE ELSE"
    ]

def get_response():
    return (
        "#SNOWFLAKE ALERT"
        "\n"
        # "Unless you eat and drink through your nose, then, yeah, you're probably the only one."
        "\n"
        "---"
        "\n"
        "^^*Bleep* ^^*bloop* ^^*I'm* ^^*a* ^^*bot* ^^*and* ^^*I* ^^*'detect'* ^^*snowflakes* ^^*like* ^^*you.*"
        )