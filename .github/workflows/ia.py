import customtkinter as ctk

# Configurações de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ChatBotApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minha IA sobre o Neymar")
        self.geometry("400x500")

        # --- Interface ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Área de chat (texto)
        self.chat_display = ctk.CTkTextbox(self, width=380, height=400)
        self.chat_display.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.chat_display.configure(state="disabled") # Bloqueia edição manual

        # Campo de entrada
        self.input_field = ctk.CTkEntry(self, placeholder_text="Digite sua mensagem...", width=300)
        self.input_field.grid(row=1, column=0, padx=(10, 100), pady=10, sticky="ew")
        self.input_field.bind("<Return>", lambda e: self.send_message())

        # Botão enviar
        self.send_button = ctk.CTkButton(self, text="Enviar", width=80, command=self.send_message)
        self.send_button.grid(row=1, column=0, padx=(310, 10), pady=10)

        self.append_message("Bot: Olá! Como posso ajudar você hoje?\n")

    def append_message(self, text):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", text + "\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

    def get_bot_response(self, user_text):
        # Lógica simples de PLN
        user_text = user_text.lower()
        if "oi" in user_text or "ola" in user_text or "bom dia" in user_text or "boa tarde" in user_text or "boa noite" in user_text:
            return "Bot: Olá! Tudo bem? O que gostaria de saber do Neymar ?"
        elif "quem" in user_text and "é" in user_text:
            return "Bot: Neymar da Silva Santos Júnior (34 anos) é um futebolista brasileiro nascido em 5 de fevereiro de 1992, amplamente reconhecido como um dos melhores atacantes do mundo e maior artilheiro da história da Seleção Brasileira. Revelado pelo Santos, com passagens consagradas por Barcelona e PSG, retornou ao Santos em 2025."
        elif "sair" in user_text:
            self.destroy()
        elif "sair" in user_text:
            return "Bot: Neymar possui 1 filho e 3 filhas Davi Lucca (14 anos), Mavie (2 anos), Helena (1 ano) e Mel (8 meses)"
        elif "idade" in user_text or "anos" in user_text and "ele" in user_text or "neymar" in user_text:
            return "Bot: Neymar da Silva Santos Junior tem 34 anos de idade"
        elif "lances" in user_text or "jogadas" in user_text:
            return "Bot: Os  melhores lances do Neymar você pode ver aqui https://youtu.be/O-0OIB3j8eE?si=G-j1jM9Y4_4jCpcY"
        elif "nome" in user_text and "inteiro" in user_text or "completo" in user_text:
            return "Bot: Neymar da Silva Santos Junior"
        elif "Nascimento" in user_text or "nasceu" in user_text:
            return "Bot: Neymar nasceu em 07/02/1992"
        elif "vai" in user_text and "copa" in user_text:
            return "Bot: De acordo com o atual técnico da seleção brasileira, Carlo Ancelotti, o Neymar tem grandes chances de ir para a copa caso estiver fisicamente 100% dotado a presença do príncipe é carimbada pelo Carleto! "
        else:
            return "Bot: Ainda estou aprendendo a entender isso..."

    def send_message(self):
        user_text = self.input_field.get()
        if user_text:
            self.append_message(f"Você: {user_text}")
            self.input_field.delete(0, 'end')
            
            # Resposta do bot
            response = self.get_bot_response(user_text)
            self.after(500, lambda: self.append_message(response))

if __name__ == "__main__":
    app = ChatBotApp()
    app.mainloop()