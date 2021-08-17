# Projeto e-diaristas

### Instalando o Projeto

#### Clonar o Projeto
`https://github.com/JSSILLES/Ediaristas.git`

#### Instalar Dependências
`pip install -r requirements.txt`

#### Alterar Configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': porta,
        'USER': 'user_bd',
        'PASSWORD': 'password_bd'
    }
}

```

#### Alterar configurações do BD no arquivo `settings.py`
#### Migrar Banco de Dados
`python manage.py migrate`

#### Iniciar o Servidor
`python manage.py runserver`
