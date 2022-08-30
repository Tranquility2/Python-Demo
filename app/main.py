import json
import httpx
import rich
import typer

app = typer.Typer()
console = rich.console.Console(highlight=False)

GET_MEMES_URL = "https://api.imgflip.com/get_memes"


@app.command()
def get_memes(num_of_results: int = typer.Argument(10, help="Limit number of resutls")) -> None:
    request = httpx.get(GET_MEMES_URL)
    if request.status_code != httpx.codes.OK:
        raise Exception("Failed to process request")
    else:
        data = json.loads(request.text).get("data")
        data_snap = data.get("memes")[:num_of_results]
        
        remove_keys_list = ['width', 'height', 'box_count']
        data_snap = [{key: i[key] for key in i if key not in remove_keys_list} for i in data_snap]

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
