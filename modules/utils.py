import requests
from rich.console import Console

console = Console()

def send_message(token, channel_id, message, message_type="DM"):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    payload = {"content": message}
    
    try:
        response = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            console.print(f"[green]✓ {token[:15]}... => {message_type} sent[/green]")
            return True
        else:
            console.print(f"[red]✗ {token[:15]}... => Error: {response.status_code}[/red]")
            return False
            
    except Exception as e:
        console.print(f"[red]✗ {token[:15]}... => Exception: {str(e)}[/red]")
        return False