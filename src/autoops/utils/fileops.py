
from pathlib import Path
from datetime import datetime
LOG_DIR = Path.cwd() / "autoops_data" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def save_log(filename: str, content: str) -> str:
    ts = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    path = LOG_DIR / f"{ts}_{filename}"
    path.write_text(content, encoding='utf-8')
    return str(path)
