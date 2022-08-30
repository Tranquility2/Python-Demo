import rich
import typer

from app.demo.fetcher import fetch_data

app = typer.Typer()
console = rich.console.Console(highlight=False)


@app.command()
def get_memes(num_of_results: int = typer.Argument(10, help="Limit number of results")) -> None:
    data_snap = fetch_data(num_of_results=num_of_results)

    table = rich.table.Table(title="Top Memes")
    columns = data_snap[0].keys()

    for c in columns:
        table.add_column(c)

    for d in data_snap:
        values = [str(v) for v in d.values()]
        table.add_row(*values)

    console.print(table)


if __name__ == "__main__":
    app()
