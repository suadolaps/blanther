import blanther


while True:
    # read and write from terminal
    text = input('blanther > ')
    result, error = blanther.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)