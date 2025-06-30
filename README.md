# TuPrimeraPagina-Magas

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
AppGames/
├── templates/
│   ├── AppGames/
│   │   ├── base.html
│   │   ├── index.html              ← Página de inicio
│   │   ├── video_juegos.html       ← Listado de videojuegos con filtros
│   │   ├── valoraciones.html       ← Lista ordenada por calificación
│   │   ├── plataformas.html        ← Juegos por plataforma
│   │   ├── *_form.html             ← Formularios para agregar datos
│   └── registration/
│       ├── login.html
│       └── register.html
├── static/
│   └── AppGames/                   ← Imágenes, íconos, estilos, JS
├── fixtures/
│   └── datos_iniciales.json       ← Datos precargados
│   └── usuarios.json              ← usuarios precargados
├── models.py                      ← Modelos: VideoJuego, Plataforma, Valoración
├── views.py                       ← Vistas lógicas
├── urls.py                        ← Rutas internas
├── forms.py                       ← Formularios personalizados
```

---

## 🧩 Modelos principales

- `VideoJuego`: nombre, género, plataformas, fecha, tag.
- `Plataforma`: nombre.
- `Valoracion`: videojuego, estrellas (1-5), comentario.

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
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Cargar datos de ejemplo**
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
- Registro de usuarios.
- Login con sistema de Django.
- Acceso limitado a ciertas funciones (si se configura).

##### Importante
##### Hay que Loguearse para poder ingresar a las siguientes secciones (Games/Reviews/Plataformas)

### 🎲 Videojuegos (`/games`)
- Listado de juegos con imagen y descripción.
- Filtro por letra (A-Z).
- Paginación integrada.

### 🖥️ Plataformas (`/platforms`)
- Muestra todas las plataformas.
- Al hacer clic, filtra los videojuegos según la plataforma elegida.

### ⭐ Valoraciones (`/reviews`)
- Lista de valoraciones ordenadas por puntaje.
- Posibilidad de filtrar por estrellas (1 a 5).
- Comentarios del usuario.

### 📝 Formularios
- Crear nuevo videojuego. --> solo para usuarios admin
- Agregar nuevas plataformas. --> solo para usuarios admin
- Dejar una valoración con estrellas y comentario.

---

## 🛠 Para el Admin

- Ingresá a `/admin` con tu superusuario.
- Desde ahí podés administrar plataformas, videojuegos, etc.

---

## 📷 Créditos de imágenes

- Template original: [Colorlib](https://colorlib.com/)
- Imágenes utilizadas solo con fines educativos.

---

## 💡 Mejoras futuras

- Sistema de favoritos por usuario.
- Comentarios entre usuarios.
- Rating promedio en cada juego.

---

## 💻 Desarrollado por

Barbie Magas  
Curso de Python + CODEHOUSE

---
