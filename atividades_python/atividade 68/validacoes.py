# Modulo de validacoes para o sistema de cadastro de alunos
# Arquivo: validacoes.py
# Atividade 68

import re
from datetime import datetime


def validar_nome(nome):
    """Valida o nome do aluno. Retorna (True, nome_limpo) ou (False, mensagem_de_erro)."""
    nome = nome.strip()
    if not nome:
        return False, "O nome nao pode estar vazio."
    if len(nome) < 2:
        return False, "O nome deve ter pelo menos 2 caracteres."
    if not all(c.isalpha() or c.isspace() for c in nome):
        return False, "O nome deve conter apenas letras e espacos."
    return True, nome.title()


def validar_email(email):
    """Valida o e-mail do aluno. Retorna (True, email_limpo) ou (False, mensagem_de_erro)."""
    email = email.strip().lower()
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        return False, "O e-mail nao pode estar vazio."
    if not re.match(padrao, email):
        return False, "E-mail invalido. Use o formato: exemplo@email.com"
    return True, email


def validar_data_nascimento(data_str):
    """Valida a data de nascimento. Retorna (True, data_formatada) ou (False, mensagem_de_erro)."""
    data_str = data_str.strip()
    formatos = ["%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]
    for fmt in formatos:
        try:
            data = datetime.strptime(data_str, fmt)
            hoje = datetime.now()
            if data > hoje:
                return False, "A data de nascimento nao pode ser uma data futura."
            idade = (hoje - data).days // 365
            if idade > 120:
                return False, "Data de nascimento invalida (idade muito alta)."
            return True, data.strftime("%d/%m/%Y")
        except ValueError:
            continue
    return False, "Formato de data invalido. Use: DD/MM/AAAA"


def validar_matricula(matricula, alunos):
    """Valida se a matricula existe. Retorna (True, aluno) ou (False, mensagem_de_erro)."""
    matricula = matricula.strip().upper()
    if not matricula:
        return False, "A matricula nao pode estar vazia."
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return True, aluno
    return False, f"Matricula '{matricula}' nao encontrada."
