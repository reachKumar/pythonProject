import tempfile

tempfile.tempdir = "c:\\temp"
print(tempfile.gettempdir())
