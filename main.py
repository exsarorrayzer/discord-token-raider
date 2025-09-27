import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from modules.banner import banner
from modules.creds import creds
from modules.dm_spammer import DMSpammer
from modules.guild_spammer import GuildSpammer
from modules.group_spammer import GroupSpammer
from modules.token_manager import TokenManager

console = Console()

def load_config():
    if not os.path.exists("config.json"):
        # Create default config
        default_config = {
            "dm": {"channel_id": "", "message": ""},
            "guild": {"channel_id": "", "message": "", "amount": 5},
            "group": {"channel_id": "", "message": "", "amount": 3}
        }
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
        return default_config
    
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        console.print(f"[red]✗ Config load error: {e}[/red]")
        return None

def show_menu():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=10)
    table.add_column("Description", style="white")
    
    table.add_row("1", "📨 DM Spam")
    table.add_row("2", "🏰 Guild Spam")
    table.add_row("3", "👥 Group Spam")
    table.add_row("4", "🔧 Token Management")
    table.add_row("5", "⚙️ Config Info")
    table.add_row("6", "👤 Developer Info")
    table.add_row("0", "🚪 Exit")
    
    console.print(Panel(table, title="[bold yellow]MAIN MENU[/bold yellow]"))

def token_management_menu(token_manager):
    while True:
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Option", style="cyan", width=10)
        table.add_column("Description", style="white")
        
        table.add_row("1", "📋 Token List")
        table.add_row("2", "➕ Add Token")
        table.add_row("3", "🧹 Clear Placeholders")
        table.add_row("0", "🔙 Back")
        
        console.print(Panel(table, title="[bold green]TOKEN MANAGEMENT[/bold green]"))
        
        choice = input("\n[?] Your choice: ").strip()
        
        if choice == "1":
            token_manager.show_tokens()
        elif choice == "2":
            new_token = input("\n[?] New Token: ").strip()
            token_manager.add_token(new_token)
        elif choice == "3":
            token_manager.clear_placeholder_text()
        elif choice == "0":
            break
        else:
            console.print("[red]❌ Invalid choice![/red]")

def show_config_info(config, token_manager):
    tokens = token_manager.load_tokens()
    
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Token Count", str(len(tokens)))
    table.add_row("DM Channel ID", config["dm"]["channel_id"] or "Not set")
    table.add_row("DM Message", config["dm"]["message"][:30] + "..." if config["dm"]["message"] else "Not set")
    table.add_row("Guild Channel ID", config["guild"]["channel_id"] or "Not set")
    table.add_row("Guild Message", config["guild"]["message"][:30] + "..." if config["guild"]["message"] else "Not set")
    table.add_row("Group Channel ID", config["group"]["channel_id"] or "Not set")
    table.add_row("Group Message", config["group"]["message"][:30] + "..." if config["group"]["message"] else "Not set")
    table.add_row("Message Count", str(config["guild"]["amount"]))
    
    console.print(Panel(table, title="[yellow]Config Information[/yellow]"))

def main():
    # Show banner
    banner()
    
    # Load config
    config = load_config()
    if not config:
        return
    
    # Create token manager
    token_manager = TokenManager()
    
    # Clear placeholders
    token_manager.clear_placeholder_text()
    
    while True:
        show_menu()
        
        try:
            choice = input("\n[?] Your choice: ").strip()
            
            if choice == "1":
                console.print("\n[bold cyan]📨 Starting DM Spam...[/bold cyan]")
                tokens = token_manager.load_tokens()
                if tokens:
                    spammer = DMSpammer(tokens)
                    spammer.spam(
                        config["dm"]["channel_id"],
                        config["dm"]["message"],
                        config["guild"]["amount"]
                    )
                else:
                    console.print("[red]❌ No tokens found![/red]")
                
            elif choice == "2":
                console.print("\n[bold cyan]🏰 Starting Guild Spam...[/bold cyan]")
                tokens = token_manager.load_tokens()
                if tokens:
                    spammer = GuildSpammer(tokens)
                    spammer.spam(
                        config["guild"]["channel_id"],
                        config["guild"]["message"],
                        config["guild"]["amount"]
                    )
                else:
                    console.print("[red]❌ No tokens found![/red]")
            
            elif choice == "3":
                console.print("\n[bold cyan]👥 Starting Group Spam...[/bold cyan]")
                tokens = token_manager.load_tokens()
                if tokens:
                    spammer = GroupSpammer(tokens)
                    spammer.spam(
                        config["group"]["channel_id"],
                        config["group"]["message"],
                        config["group"]["amount"]
                    )
                else:
                    console.print("[red]❌ No tokens found![/red]")
                
            elif choice == "4":
                token_management_menu(token_manager)
                
            elif choice == "5":
                show_config_info(config, token_manager)
                
            elif choice == "6":
                creds()
                
            elif choice == "0":
                console.print(Panel("[bold yellow]👋 Exiting...[/bold yellow]", 
                                  border_style="red"))
                break
                
            else:
                console.print("[red]❌ Invalid choice![/red]")
                
        except KeyboardInterrupt:
            console.print(Panel("[bold yellow]👋 Exiting...[/bold yellow]", 
                              border_style="red"))
            break
        except Exception as e:
            console.print(f"[red]❌ Error: {e}[/red]")

if __name__ == "__main__":
    main()