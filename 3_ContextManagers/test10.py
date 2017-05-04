from contextlib import redirect_stdout
from io import StringIO


stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
    print("write somethin to the stream")
    with write_to_stream:
        print("write something else to the stream")

print(stream.getvalue())