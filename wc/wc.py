from typing import Optional
import typer
from typing_extensions import Annotated
import sys

app = typer.Typer()


@app.command()
def count_bytes(
    file: Optional[Annotated[typer.FileBinaryRead, typer.Option()]] = None,
    c: bool = typer.Option(False,"--bytes","-c"),
    l: bool = typer.Option(False,"--lines","-l"),
    w: bool = typer.Option(False,"--words","-w"),
    m: bool = typer.Option(False,"--chars","-m")
):
    line_counter = 0
    byte_counter = 0
    word_counter = 0
    char_counter = 0

    if file is None:
        file = sys.stdin.buffer

    for line in file:
        byte_counter += len(line)
        line_counter += 1
        word_counter += len(line.decode().split())
        decoded_line = line.decode()
        for char in decoded_line:
            char_counter += 1
    
    if not any([c,l,w,m]):
        print(line_counter, word_counter, byte_counter)

    else:
        if c:
            print(byte_counter)
        if l:
            print(line_counter)
        if w:
            print(word_counter)
        if m:
            print(char_counter)
        
    
if __name__ == "__main__":
    app()
