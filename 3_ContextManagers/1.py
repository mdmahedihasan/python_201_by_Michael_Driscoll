from contextlib import redirect_stdout
from io import StringIO


stream = StringIO()
write_to_strem = redirect_stdout(stream)
with write_to_strem:
    print("write something")
    with write_to_strem:
        print("write something else")

print(stream.getvalue())