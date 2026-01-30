# Sistema de Troca de Gelo 5S - ONCOPROD/TRANSMEP

Sistema web desenvolvido em Django para gerenciar e registrar trocas de gelo para transporte de medicamentos, seguindo o padrão 5S.

## 🚀 Características

- ✅ Formulário intuitivo e responsivo com 6 passos
- ✅ Validação automática de temperaturas
- ✅ Upload de fotos (etiqueta, temperatura medicamento e gelo)
- ✅ Cálculo automático do período de ambientação (20 minutos)
- ✅ Preview de imagens antes do envio
- ✅ Interface moderna com Tailwind CSS
- ✅ Validação em tempo real com Alpine.js
- ✅ Histórico completo de trocas
- ✅ Filtros e busca avançada
- ✅ Responsivo para mobile

## 📋 Modelos de Caixas Suportados

1. **12 litros IF-2.000** - 02 unidades gelox ice foam 2.000
2. **12 litros IT-1050** - 03 unidades gelox ita fria 1050
3. **33 litros IF-1050 PRECAUÇÃO** - 01 unidade gelox Ice Foam-1050
4. **44 litros IT-1050** - 06 unidades gelox Ita Fria 1050
5. **80 litros IT-1050** - 10 unidades gelox Ita Fria 1050
6. **120 litros IT-1050** - 12 unidades gelox Ita Fria 1050

## 🌡️ Faixas de Temperatura

### Medicamento
- **Caixas padrão**: 2°C até 8°C
- **Caixa 33L (Precaução)**: 15°C até 25°C

### Gelo
- **Todas as caixas**: -5,0°C até -9,0°C

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.0.1
- **Frontend**: Tailwind CSS 3.x
- **JavaScript**: Alpine.js 3.x
- **Ícones**: Font Awesome 6.4
- **Upload de Imagens**: Pillow 10.2
- **Banco de Dados**: SQLite (padrão) / PostgreSQL (produção)

## 📦 Instalação

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

### Passo a Passo

1. **Clone o repositório ou extraia os arquivos**
```bash
cd /caminho/do/projeto
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure o projeto**

Crie a estrutura de diretórios:
```bash
mkdir -p troca_gelo/templates/troca_gelo
mkdir -p static
mkdir -p media
```

Mova os arquivos para suas respectivas pastas:
- `models.py`, `forms.py`, `views.py`, `urls.py`, `admin.py` → `troca_gelo/`
- `templates/` → mantenha a estrutura de templates
- `settings.py` → `config/settings.py`
- `config_urls.py` → `config/urls.py`

5. **Configure o arquivo settings**

Edite `config/settings.py` e ajuste:
```python
SECRET_KEY = 'sua-chave-secreta-aqui'  # Gere uma nova chave
DEBUG = True  # False em produção
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Adicione seu domínio em produção
```

6. **Crie o arquivo `troca_gelo/__init__.py`**
```bash
touch troca_gelo/__init__.py
```

7. **Crie o arquivo `troca_gelo/apps.py`**
```python
from django.apps import AppConfig

class TrocaGeloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'troca_gelo'
    verbose_name = 'Troca de Gelo 5S'
```

8. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

9. **Crie um superusuário (para acessar o admin)**
```bash
python manage.py createsuperuser
```

10. **Colete os arquivos estáticos**
```bash
python manage.py collectstatic --noinput
```

11. **Execute o servidor de desenvolvimento**
```bash
python manage.py runserver
```

12. **Acesse o sistema**
- Formulário: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Histórico: http://localhost:8000/lista/

## 📱 Estrutura do Projeto

```
projeto/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── troca_gelo/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── troca_gelo/
│       ├── formulario.html
│       ├── sucesso.html
│       ├── lista.html
│       └── detalhe.html
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## 🎯 Fluxo de Uso

1. **Passo 01**: Selecione o modelo da caixa
2. **Passo 02**: Informe o número do pedido
3. **Passo 03**: Selecione a data da embalagem
4. **Passo 04**: Tire/carregue foto da etiqueta
5. **Passo 05**: Tire/carregue foto da temperatura do medicamento e informe o valor
6. **Passo 06**: Tire/carregue foto da temperatura do gelo e informe o valor
7. Sistema calcula automaticamente o período de ambientação (20 minutos antes)
8. Ao finalizar, você pode iniciar uma nova troca

## ⚙️ Validações Implementadas

### Validações Frontend (Tempo Real)
- Verificação visual das faixas de temperatura
- Preview das imagens antes do envio
- Barra de progresso do formulário
- Alertas de campos obrigatórios

### Validações Backend (Django)
- Validação rigorosa das faixas de temperatura
- Limite de tamanho de arquivo (10MB)
- Campos obrigatórios
- Formato de imagem válido

## 🔒 Segurança

- CSRF Protection habilitado
- Validação de tipos de arquivo
- Sanitização de inputs
- Proteção contra SQL Injection (ORM Django)

## 📊 Funcionalidades Adicionais

### Admin Django
- Gerenciamento completo das trocas
- Filtros por modelo, data e status
- Busca por número de pedido
- Visualização de fotos
- Exportação de dados

### Histórico
- Listagem paginada (20 itens por página)
- Filtros por modelo e período
- Status visual das temperaturas
- Acesso aos detalhes completos

## 🚀 Deploy em Produção

### Configurações Importantes

1. **settings.py**
```python
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']
SECRET_KEY = os.getenv('SECRET_KEY')  # Use variável de ambiente
```

2. **Banco de Dados (PostgreSQL recomendado)**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'troca_gelo_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Servidor Web**
- Use Gunicorn ou uWSGI
- Configure Nginx como proxy reverso
- Habilite HTTPS (Let's Encrypt)

4. **Arquivos Estáticos e Media**
- Configure armazenamento em S3 ou similar
- Use CDN para arquivos estáticos

## 🐛 Troubleshooting

### Erro: "No module named 'PIL'"
```bash
pip install Pillow
```

### Erro: "CSRF token missing"
- Verifique se `{% csrf_token %}` está no formulário
- Limpe cache e cookies do navegador

### Imagens não aparecem
- Execute `python manage.py collectstatic`
- Verifique permissões da pasta `media/`
- Confirme `MEDIA_URL` e `MEDIA_ROOT` no settings

## 📝 Licença

Este projeto foi desenvolvido para uso interno da ONCOPROD/TRANSMEP.

## 👥 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação acima
2. Consulte os logs do Django
3. Entre em contato com o time de TI

## 🔄 Atualizações Futuras

- [ ] Exportação para Excel/PDF
- [ ] Notificações por e-mail
- [ ] Dashboard com estatísticas
- [ ] Integração com sistema de pedidos
- [ ] App mobile nativo
- [ ] Reconhecimento automático de temperatura via OCR

---

**Desenvolvido com Django + Tailwind CSS**