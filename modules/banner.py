from rich.console import Console
from rich.panel import Panel

console = Console()

def banner() -> None:
    art = r'''
 .S_sSSs     .S_SSSs     .S S.    sdSSSSSSSbs    sSSs   .S_sSSs                                                                  
.SS~YS%%b   .SS~SSSSS   .SS SS.   YSSSSSSSS%S   d%%SP  .SS~YS%%b                                                                 
S%S   `S%b  S%S   SSSS  S%S S%S          S%S   d%S'    S%S   `S%b                                                                
S%S    S%S  S%S    S%S  S%S S%S         S&S    S%S     S%S    S%S                                                                
S%S    d*S  S%S SSSS%S  S%S S%S        S&S     S&S     S%S    d*S                                                                
S&S   .S*S  S&S  SSS%S   SS SS         S&S     S&S_Ss  S&S   .S*S                                                                
S&S_sdSSS   S&S    S&S    S S         S&S      S&S~SP  S&S_sdSSS                                                                 
S&S~YSY%b   S&S    S&S    SSS        S*S       S&S     S&S~YSY%b                                                                 
S*S   `S%b  S*S    S&S    S*S       S*S        S*b     S*S   `S%b                                                                
S*S    S%S  S*S    S*S    S*S     .s*S         S*S.    S*S    S%S                                                                
S*S    S&S  S*S    S*S    S*S     sY*SSSSSSSP   SSSbs  S*S    S&S                                                                
S*S    SSS  SSS    S*S    S*S    sY*SSSSSSSSP    YSSP  S*S    SSS                                                                
SP                 SP     SP                           SP                                                                        
Y                  Y      Y                            Y                                                                         
                                                                                                                                 
 .S_sSSs     .S    sSSs    sSSs    sSSs_sSSs     .S_sSSs     .S_sSSs                                                             
.SS~YS%%b   .SS   d%%SP   d%%SP   d%%SP~YS%%b   .SS~YS%%b   .SS~YS%%b                                                            
S%S   `S%b  S%S  d%S'    d%S'    d%S'     `S%b  S%S   `S%b  S%S   `S%b                                                           
S%S    S%S  S%S  S%|     S%S     S%S       S%S  S%S    S%S  S%S    S%S                                                           
S%S    S&S  S&S  S&S     S&S     S&S       S&S  S%S    d*S  S%S    S&S                                                           
S&S    S&S  S&S  Y&Ss    S&S     S&S       S&S  S&S   .S*S  S&S    S&S                                                           
S&S    S&S  S&S  `S&&S   S&S     S&S       S&S  S&S_sdSSS   S&S    S&S                                                           
S&S    S&S  S&S    `S*S  S&S     S&S       S&S  S&S~YSY%b   S&S    S&S                                                           
S*S    d*S  S*S     l*S  S*b     S*b       d*S  S*S   `S%b  S*S    d*S                                                           
S*S   .S*S  S*S    .S*P  S*S.    S*S.     .S*S  S*S    S%S  S*S   .S*S                                                           
S*S_sdSSS   S*S  sSS*S    SSSbs   SSSbs_sdSSS   S*S    S&S  S*S_sdSSS                                                            
SSS~YSSY    S*S  YSS'      YSSP    YSSP~YSSY    S*S    SSS  SSS~YSSY                                                             
            SP                                  SP                                                                               
            Y                                   Y                                                                                
                                                                                                                                 
sdSS_SSSSSSbs    sSSs_sSSs     .S    S.     sSSs   .S_sSSs           .S_sSSs     .S_SSSs     .S   .S_sSSs      sSSs   .S_sSSs    
YSSS~S%SSSSSP   d%%SP~YS%%b   .SS    SS.   d%%SP  .SS~YS%%b         .SS~YS%%b   .SS~SSSSS   .SS  .SS~YS%%b    d%%SP  .SS~YS%%b   
     S%S       d%S'     `S%b  S%S    S&S  d%S'    S%S   `S%b        S%S   `S%b  S%S   SSSS  S%S  S%S   `S%b  d%S'    S%S   `S%b  
     S%S       S%S       S%S  S%S    d*S  S%S     S%S    S%S        S%S    S%S  S%S    S%S  S%S  S%S    S%S  S%S     S%S    S%S  
     S&S       S&S       S&S  S&S   .S*S  S&S     S%S    S&S        S%S    d*S  S%S SSSS%S  S&S  S%S    S&S  S&S     S%S    d*S  
     S&S       S&S       S&S  S&S_sdSSS   S&S_Ss  S&S    S&S        S&S   .S*S  S&S  SSS%S  S&S  S&S    S&S  S&S_Ss  S&S   .S*S  
     S&S       S&S       S&S  S&S~YSSY%b  S&S~SP  S&S    S&S        S&S_sdSSS   S&S    S&S  S&S  S&S    S&S  S&S~SP  S&S_sdSSS   
     S&S       S&S       S&S  S&S    `S%  S&S     S&S    S&S        S&S~YSY%b   S&S    S&S  S&S  S&S    S&S  S&S     S&S~YSY%b   
     S*S       S*b       d*S  S*S     S%  S*b     S*S    S*S        S*S   `S%b  S*S    S&S  S*S  S*S    d*S  S*b     S*S   `S%b  
     S*S       S*S.     .S*S  S*S     S&  S*S.    S*S    S*S        S*S    S%S  S*S    S*S  S*S  S*S   .S*S  S*S.    S*S    S%S  
     S*S        SSSbs_sdSSS   S*S     S&   SSSbs  S*S    S*S        S*S    S&S  S*S    S*S  S*S  S*S_sdSSS    SSSbs  S*S    S&S  
     S*S         YSSP~YSSY    S*S     SS    YSSP  S*S    SSS        S*S    SSS  SSS    S*S  S*S  SSS~YSSY      YSSP  S*S    SSS  
     SP                       SP                  SP                SP                 SP   SP                       SP          
     Y                        Y                   Y                 Y                  Y    Y                        Y           
                                                                                                                                                                                                                                 
'''

    # kirmizi tonları (RGB)
    red_shades = [
        (255, 0, 0),
        (255, 0, 25),
        (255, 0, 30),
        (255, 0, 45),
        (255, 0, 55),
        (255, 0, 75),
        (255, 0, 80)
    ]

    art_lines = art.strip("\n").split("\n")
    colored_lines = []

    for i, line in enumerate(art_lines):
        color = red_shades[i % len(red_shades)]
        hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
        colored_lines.append(f"[{hex_color}]{line}[/{hex_color}]")

    console.print("\n".join(colored_lines))

if __name__ == "__main__":
    banner()