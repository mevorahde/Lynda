def countdown(x):
    if x == 0:
        print("Done!")
    else:
        print(x, "...")
        countdown(x-1)


countdown(5)
