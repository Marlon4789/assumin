# 🎯 Assumin

Una aplicación web en Django para **registrar emociones y analizar datos con inteligencia artificial**.

## Descripción

Assumin es una plataforma que permite a los usuarios:
- Registrar sus emociones y estados emocionales
- Guardar y organizar información personal
- Analizar registros utilizando inteligencia artificial
- Compartir y colaborar en nuevas ideas
- Autenticarse de forma segura con Google

## 🚀 Características Principales

- **Registro de Emociones**: Interfaz intuitiva para registrar tus estados emocionales
- **Análisis con IA**: Utiliza inteligencia artificial para analizar patrones en tus registros
- **Autenticación Google**: Login seguro mediante Google OAuth
- **Gestor de Ideas**: Espacio para guardar y gestionar nuevas ideas
- **Panel de Administración**: Interfaz Django admin para gestionar datos
- **Base de Datos Local**: SQLite para almacenamiento seguro de datos

## 📦 Estructura del Proyecto

```
assumin/
├── core/                    # Configuración principal del proyecto Django
│   ├── settings.py         # Configuración de la aplicación
│   ├── urls.py             # Rutas principales
│   ├── wsgi.py             # Configuración WSGI
│   └── asgi.py             # Configuración ASGI
├── recording_emotion/       # App para registrar emociones
├── login/                  # App de autenticación
├── new_ideas/              # App para gestionar ideas
├── analysis_registers_ai/  # App de análisis con IA
├── templates/              # Plantillas HTML
├── venv/                   # Entorno virtual Python
└── manage.py               # Script de administración Django
```

## 🛠️ Instalación

### Requisitos Previos
- Python 3.8+
- pip (gestor de paquetes de Python)
- git

### Pasos de Instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/Marlon4789/assumin.git
cd assumin
```

2. **Crea un entorno virtual**
```bash
python -m venv venv
```

3. **Activa el entorno virtual**
   - En Windows:
   ```bash
   venv\Scripts\activate
   ```
   - En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

5. **Realiza las migraciones de la base de datos**
```bash
python manage.py migrate
```

6. **Crea un superusuario (admin)**
```bash
python manage.py createsuperuser
```

7. **Inicia el servidor**
```bash
python manage.py runserver
```

8. **Accede a la aplicación**
- Web: http://localhost:8000
- Admin: http://localhost:8000/admin

## 🔐 Configuración de Google OAuth

Para usar la autenticación con Google, debes:

1. Crear un proyecto en [Google Cloud Console](https://console.cloud.google.com/)
2. Obtener las credenciales OAuth 2.0
3. Crear un archivo `.env` en la raíz del proyecto con:
```
GOOGLE_API_ID_CLIENT=tu_client_id
GOOGLE_SECRET_CLIENT=tu_secret_client
```

## 📱 Funcionalidades por Módulo

### recording_emotion 🎤
- Crear nuevos registros de emociones
- Listar registros guardados
- Editar y eliminar registros

### login 🔑
- Autenticación de usuarios
- Login con Google
- Gestión de sesiones

### new_ideas 💡
- Guardar nuevas ideas
- Organizar ideas por categorías
- Compartir ideas

### analysis_registers_ai usando API de OpenIA 🤖
- Analizar registros con IA
- Generar reportes de emociones
- Identificar patrones

**Nota**: Este es un proyecto en desarrollo. Algunas características pueden cambiar.
