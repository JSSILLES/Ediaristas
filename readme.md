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
        'NAME': 'ediaristas',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root'
    }
}

```

#### Alterar configurações do BD no arquivo `settings.py`
#### Migrar Banco de Dados
`python manage.py migrate`

#### Iniciar o Servidor
`python manage.py runserver`
