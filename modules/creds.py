from rich.console import Console  # By Rayzer

console = Console()  # By Rayzer

def creds() -> None:  # By Rayzer
    """creds"""  # By Rayzer
    info = """GitHub:    exsarorrayzer
Instagram: exsarorrayzer
Discord:   noinfonocontext
Youtube:   exsarorrayzer"""  # By Rayzer

    # Kirmizi tonları (RGB)  # By Rayzer
    red_shades = [
        (255, 0, 0),
        (255, 0, 25),
        (255, 0, 30),
        (255, 0, 45),
        (255, 0, 55),
        (255, 0, 75),
        (255, 0, 80)
    ]  # By Rayzer

    lines = info.strip("\n").split("\n")  # By Rayzer
    colored_lines = []  # By Rayzer

    for i, line in enumerate(lines):  # By Rayzer
        color = red_shades[i % len(purple_shades)]  # By Rayzer
        hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"  # By Rayzer
        colored_lines.append(f"[{hex_color}]{line}[/{hex_color}]")  # By Rayzer

    console.print("\n".join(colored_lines))  # By Rayzer

if __name__ == "__main__":  # By Rayzer
    creds()  # By Rayzer