# EntregaFinal-Magas

# 🎮 GG - Good Game

Sitio web para fans de los videojuegos, creado con django. Permite gestionar videojuegos, plataformas, valoraciones, y más.

---

---

## 🚀 Tecnologías usadas

- **Python**
- **Django**
- **SQLite**
- **Bootstrap**
- **Template customizado descargado de EndGame – Free Bootstrap 4 HTML5 Gaming Website Template**
- https://themewagon.com/themes/free-bootstrap-4-html5-gaming-website-template-endgame/#:~:text=EndGame%20is%20a%20free%20Bootstrap,a%20simple%20and%20minimalist%20approach.

---

## 🏗️ Estructura del Proyecto

```
EntregaFinal-Magas/
├── AppGames/                        ← App principal con juegos, páginas, valoraciones, etc.
│   ├── templates/
│   │   ├── AppGames/
│   │   │   ├── base.html
│   │   │   ├── index.html               ← Página de inicio
│   │   │   ├── video_juegos.html        ← Juegos con filtros, favoritos, búsqueda
│   │   │   ├── plataformas.html         ← Juegos por plataforma
│   │   │   ├── valoraciones.html        ← Reviews por puntuación
│   │   │   ├── about.html               ← Página "Acerca de mí"
│   │   │   ├── sitemap.html             ← Mapa de navegación
│   │   │   ├── *_form.html              ← Formularios para juegos, páginas, etc.
│   ├── static/
│   │   └── AppGames/                    ← Imágenes, íconos, estilos, JS
│   ├── models.py
│   ├── views/
│   │   └── general.py
│   │   └── plataformas.py
│   │   └── valoraciones.py
│   │   └── video_juegos.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── accounts/                        ← App separada para autenticación y perfiles de usuario
│   ├── templates/
│   │   ├── accounts/
│   │   │   ├── profile.html               ← Vista de perfil
│   │   │   ├── edit_profile.html          ← Edición de perfil
│   │   │   ├── password_change.html       ← Cambio de contraseña
│   │   │   ├── password_change_done.html  ← Contraseña modificada ok!
│   │   └── registration/
│   │       ├── login.html               ← Login
│   │       └── register.html            ← Registro
│   ├── models.py                      ← Modelo extendido Profile
│   ├── views.py                       ← Vistas de login, registro, perfil, etc.
│   ├── forms.py                       ← Formulario de perfil
│   ├── urls.py                        ← URLs de accounts
│   └── admin.py
│
├── media/                           ← Avatares subidos por usuarios (excluidos por .gitignore)
├── fixtures/
│   ├── datos_iniciales.json
│   ├── usuarios.json
├── db.sqlite3                       ← (Ignorado en el repo)
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
└── proyecto_web_django/         ← Carpeta del proyecto Django (settings, urls, wsgi)
    ├── settings.py
    ├── urls.py
    └── ...

```

---

## 🧩 Modelos principales

- `VideoJuego`: nombre, género, plataformas, fecha, tag.
- `Plataforma`: nombre.
- `Valoracion`: videojuego, estrellas (1-5), comentario.
- `Perfil`: user, avatar, fecha_nacimiento.
---


## 📦 Instalación local

1. **Cloná el repositorio**
```bash
git clone https://github.com/bdmagas/TuPrimeraPagina-Magas.git
cd TuPrimeraPagina-Magas
```

2. **Creá y activá un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate    # en Windows: venv\Scripts\activate
```

3. **Instalá dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplicá migraciones**
⚠️ **Importante:** Si ya tenés el archivo db.sqlite3, podés omitir el paso de migraciones.

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Cargar datos de ejemplo**
⚠️ **Opcional:** Este paso es necesario **solo si estás generando la base de datos desde cero**  
Si ya clonaste el proyecto con el archivo db.sqlite3, podés saltearlo.

```bash
python manage.py loaddata AppGames/fixtures/datos_iniciales.json
```

7. **¡Ejecutá el servidor!**
```bash
python manage.py runserver
```

Y navegá a:  
📍 `http://127.0.0.1:8000/`

---



## ✨ Funcionalidades

### 👾 Página de inicio (`/`)
- Slider de bienvenida.
- Trailer destacado.
- Anuncio especial destacado.

### 🔐 Autenticación
- Registro, login y logout de usuarios.
- Login con sistema de Django.
- Acceso limitado a ciertas funciones (dependiendo del perfil del usuario staff/no staff).

### 👤 Perfil de usuario
- Perfil de usuario con los campos: nombre, apellido, avatar, email, fecha de cumpleaños.
- Edición del perfil: /perfil/edit
- Avatar: Carga de imagen de perfil.
- Cambio de contraseña: /perfil/password_change

### 🎲 Videojuegos (`/games`)
- Listado de juegos con imagen y descripción.
- Filtro por letra (A-Z), género y tags.
- Paginación integrada.
- Buscador integrado.
- Marcar como favorito (AJAX toggle).
- Estilo visual atractivo con cards.
- Link en la card del juego para entrar a vista detallada


### 🖥️ Plataformas (`/platforms`)
- Muestra todas las plataformas.
- Al hacer clic, filtra los videojuegos según la plataforma elegida.

### ⭐ Valoraciones (`/reviews`)
- Lista de valoraciones ordenadas por estrellas.
- Posibilidad de filtrar por estrellas (1 a 5).
- Valoración incluye: juego, plataforma, comentario y fecha.
- Estilo visual atractivo con cards.

##### Importante
##### Hay que Loguearse para poder ingresar a las siguientes secciones (Games/Reviews/Plataformas)

### 📝 Formularios
- Crear/Editar/Borrar nuevo videojuego. --> solo para usuarios admin
- Agregar/Editar/Borrar nuevas plataformas. --> solo para usuarios admin
- Dejar una valoración con estrellas y comentario.

---

## 📄 Páginas informativas (/about/)
- Página de "Acerca de mí": /about

## 🗺️ Mapa del sitio (/sitemap)
- Muestra las rutas principales de la app.


## 🛠 Para el Admin

- Ingresá a `/admin` con tu superusuario.
- Desde ahí podés administrar plataformas, videojuegos, etc.

---

## 📷 Créditos de imágenes

- Template base: Themewagon / EndGame
- Íconos: FontAwesome
- Imágenes utilizadas solo con fines educativos.

---

## 💡 Mejoras futuras

- Rating promedio en cada juego. ✅
- Mejorar el sistema de favoritos por usuario.
- Comentarios entre usuarios.

---

## 💻 Desarrollado por

Barbie Magas  
Entrega Final
Curso de Python + Django + CODEHOUSE

---
