from rich.console import Console

console = Console()

def log_info(message):
    console.print(f"[bold blue][*][/bold blue] {message}")

def log_success(message):
    console.print(f"[bold green][+][/bold green] {message}")

def log_error(message):
    console.print(f"[bold red][-][/bold red] {message}")

