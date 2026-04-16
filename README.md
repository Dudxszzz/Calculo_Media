# 📚 Calculadora de Médias Escolares

Verificador de notas trimestrais e média final

![Python](https://img.shields.io/badge/Python-3.x-3572A5?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-gray?style=flat-square)

---

## 📋 Sobre o projeto

Programa de linha de comando desenvolvido em Python para calcular a média trimestral de um aluno com base em três notas, verificando aprovação direta ou necessidade de prova final.

> Este foi meu primeiro projeto em Python — simples, mas funcional! 🎓

---

## ⚙️ Funcionamento

```
Inserir 3 notas → Calcular média → Média ≥ 7.0?
  ├── SIM → ✅ Aprovado por nota
  └── NÃO → Inserir nota final → (Média + Final) / 2 ≥ 5.0?
              ├── SIM → ✅ Aprovado na final
              └── NÃO → ❌ Reprovado
```

---

## 🚀 Como executar

### Pré-requisitos
- [Python 3.x](https://www.python.org/downloads/) instalado

### Rodando o projeto

```bash
# Clone o repositório
git clone https://github.com/Dudxszzz/media-escolar

# Acesse a pasta
cd media-escolar

# Execute o programa
python media.py
```

---

## 💡 Exemplos de saída

**Aprovado por média:**
```
Digite sua primeira nota: 8.0
Digite a segunda nota: 7.5
Digite a terceira nota: 9.0

A soma das notas trimestrais foi de: 24.5
E a média trimestral foi de: 8.2

Parabéns, você passou por nota! ;-;
```

**Vai para a final:**
```
A média trimestral foi de: 5.5
Qual foi a nota da média final? 7.0

Parabéns, você passou na final!
```

**Reprovado:**
```
A média trimestral foi de: 4.0
Qual foi a nota da média final? 3.5

Infelizmente, você não recuperou na final!
```

---

## 📐 Critérios de aprovação

| Situação | Condição | Resultado |
|---|---|---|
| Aprovado direto | Média ≥ 7.0 | ✅ Aprovado |
| Aprovado na final | (Média + Final) / 2 ≥ 5.0 | ✅ Aprovado |
| Reprovado | (Média + Final) / 2 < 5.0 | ❌ Reprovado |

---

## 🧑‍💻 Autor

Feito por **Eduardo Lima**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eduardomoreiralima/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:limaedu.contato@gmail.com)
