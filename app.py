from repository import repo
from lead import Lead

class MiniCRMApp:
    def __init__(self, repository):
        self.repo = repository

    def _print_menu(self):
        print("\nMini CRM de Leads — Orientação a Objetos")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/empresa/e-mail)")
        print("[4] Exportar CSV")
        print("[0] Sair")

    def add_leads(self):
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()
        
        if not name or not email or "@" not in email:
            print("Nome e e-mail válido são obrigatórios.")
            return

        new_lead = Lead(name, company, email)
        self.repo.create_lead(new_lead)

        print("✔ Lead adicionado!")

    def list_leads(self):
        leads = self.repo.read_leads()
        if not leads:
            print("Nenhum lead ainda.")
            return
        
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, lead in enumerate(leads):
            print(f"{i:02d}| {lead.name:<20} | {lead.company:<17} | {lead.email:<21}")

    def search_flow(self):
        q = input("Buscar por: ").strip().lower()
        if not q:
            print("Consulta vazia.")
            return
        
        leads = self.repo.read_leads()
        results = []
        for i, lead in enumerate(leads):
            # Converte o objeto Lead para uma string pesquisável
            blob = f"{lead.name} {lead.company} {lead.email}".lower()
            if q in blob:
                results.append((i, lead))
        
        if not results:
            print("Nada encontrado.")
            return
        
        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, lead in results:
            print(f"{i:02d}| {lead.name:<20} | {lead.company:<17} | {lead.email:<21}")

    def export_leads(self):
        path = self.repo.export_csv()
        if path is None:
            print("Não consegui escrever o CSV. Feche o arquivo se estiver aberto e tente novamente.")
        else:
            print(f"✔ Exportado para: {path}")

    def run(self):
        while True:
            self._print_menu()
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_leads()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_flow()
            elif op == "4":
                self.export_leads()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    app = MiniCRMApp(repo)
    app.run()
