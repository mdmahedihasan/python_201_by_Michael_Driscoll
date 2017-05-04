from contextlib import redirect_stdout


path = "text1.txt"
with open(path, "w") as f_obj:
    with redirect_stdout(f_obj):
        help(redirect_stdout)