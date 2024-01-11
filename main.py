from time import sleep
import sys

def animationPrinting(word:str, delay:int):
    length = len(word)
    
    for x in range(length):
        print(f"{word[x]}", end="", flush=True)
        sleep(delay)

variable = "Testing_variable"

animationPrinting(f"Test input \nyou can put here literally every string or result\nformatted also \"{variable}\"", float(sys.argv[1]))
