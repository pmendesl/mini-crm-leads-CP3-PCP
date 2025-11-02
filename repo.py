from pathlib import Path
import json, csv
from lead import Lead

class LeadRepository:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.data_dir = db_path.parent
        self.data_dir.mkdir(exist_ok=True)

    def _load(self) -> list[Lead]:
        if not self.db_path.exists():
            return []
        try:
            data = json.loads(self.db_path.read_text(encoding="utf-8"))
            return [Lead.from_dict(d) for d in data]
        except json.JSONDecodeError:
            # se corromper, começa vazio (decisão didática para agora)
            return []

    def _save(self, leads: list[Lead]):
        data = [lead.to_dict() for lead in leads]
        self.db_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def read_leads(self) -> list[Lead]:
        return self._load()

    def create_lead(self, lead: Lead):
        leads = self._load()
        leads.append(lead)
        self._save(leads)

    def export_csv(self, path: Path = None) -> Path | None:
        """Exporta os leads para CSV. Retorna o caminho do arquivo."""
        path = path if path else (self.data_dir / "leads.csv")
        leads = self._load()
        try:
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["name","company","email","stage","created"])
                w.writeheader()
                for lead in leads:
                    w.writerow(lead.to_dict())
            return path
        except PermissionError:
            # caso o arquivo esteja aberto em outro programa, por exemplo
            return None

# Inicialização do repositório
DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"
repo = LeadRepository(DB_PATH)
