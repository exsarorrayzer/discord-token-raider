import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class TokenManager:
    def __init__(self, token_file="tokens.txt"):
        self.token_file = token_file
    
    def load_tokens(self):
        """Load tokens from tokens.txt"""
        if not os.path.exists(self.token_file):
            console.print("[red]✗ tokens.txt not found![/red]")
            return []
        
        try:
            with open(self.token_file, "r", encoding="utf-8") as f:
                tokens = [line.strip() for line in f.readlines() if line.strip()]
            
            # Filter out placeholder text
            filtered_tokens = []
            for token in tokens:
                if (token and 
                    not token.lower().startswith("put your") and 
                    not token.lower().startswith("token") and
                    len(token) > 10):
                    filtered_tokens.append(token)
            
            console.print(f"[green]✓ {len(filtered_tokens)} tokens loaded[/green]")
            return filtered_tokens
            
        except Exception as e:
            console.print(f"[red]✗ Error loading tokens: {e}[/red]")
            return []
    
    def add_token(self, new_token):
        """Add new token"""
        if not new_token or len(new_token) < 10:
            console.print("[red]✗ Invalid token![/red]")
            return False
        
        try:
            # Load current tokens
            current_tokens = self.load_tokens()
            
            # Check if token already exists
            if new_token in current_tokens:
                console.print("[yellow]⚠ Token already exists![/yellow]")
                return True
            
            # Add token to list
            current_tokens.append(new_token)
            
            # Rewrite file
            with open(self.token_file, "w", encoding="utf-8") as f:
                for token in current_tokens:
                    f.write(token + "\n")
            
            console.print("[green]✓ Token added successfully![/green]")
            return True
            
        except Exception as e:
            console.print(f"[red]✗ Error adding token: {e}[/red]")
            return False
    
    def show_tokens(self):
        """Show current tokens (shortened)"""
        tokens = self.load_tokens()
        
        if not tokens:
            console.print("[yellow]⚠ No tokens found![/yellow]")
            return
        
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("#", style="white", width=5)
        table.add_column("Token", style="green")
        table.add_column("Status", style="yellow")
        
        for i, token in enumerate(tokens, 1):
            displayed_token = f"{token[:15]}..." if len(token) > 15 else token
            table.add_row(str(i), displayed_token, "✅ Active")
        
        console.print(Panel(table, title="[bold magenta]Token List[/bold magenta]"))
    
    def clear_placeholder_text(self):
        """Clear placeholder text"""
        try:
            if os.path.exists(self.token_file):
                with open(self.token_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                # Filter placeholders
                cleaned_lines = []
                for line in lines:
                    line_stripped = line.strip().lower()
                    if (line_stripped and 
                        not line_stripped.startswith("put your") and 
                        not line_stripped.startswith("token") and
                        not line_stripped.startswith("here") and
                        len(line.strip()) > 10):
                        cleaned_lines.append(line.strip())
                
                # Rewrite file
                with open(self.token_file, "w", encoding="utf-8") as f:
                    for line in cleaned_lines:
                        f.write(line + "\n")
                
                if len(lines) != len(cleaned_lines):
                    console.print("[green]✓ Placeholder text cleared![/green]")
                    
        except Exception as e:
            console.print(f"[red]✗ Clear error: {e}[/red]")