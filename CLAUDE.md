# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 3.2 REST API backend for a dynamic content management system. The API serves content pages, sections, and components to a frontend application and provides admin interfaces for content management. It uses Django REST Framework for API endpoints, Token authentication, and includes Swagger documentation.

## Development Commands

### Environment Setup
```bash
# Using Pipenv (recommended)
pipenv install                      # Install dependencies
pipenv shell                        # Activate virtual environment

# Using pip directly
pip install -r requirements.txt     # Install from requirements.txt
```

### Running the Application
```bash
python manage.py runserver          # Start dev server on localhost:8000
python manage.py runserver 0.0.0.0:8000  # Expose to network
```

### Database Management
```bash
python manage.py makemigrations     # Create new migrations
python manage.py migrate            # Apply migrations
python manage.py createsuperuser    # Create admin user
```

### Django Admin
```bash
python manage.py shell              # Django shell
python manage.py dbshell            # Database shell
```

### Testing & Code Quality
```bash
python manage.py test               # Run tests
```

## Project Structure

### Django Apps

The project is organized into four main Django apps:

1. **core** - Core page structure and navigation
   - `Menu`: Navigation menu items with slug-based routing
   - `CorePage`: Dynamic pages with rich text content
   - `Section`: Page sections that contain components
   - `ComponentType`: Types of components available (FAQ, news, products, etc.)

2. **component** - Content components that populate sections
   - `ComponentData`: Generic component data
   - `CardMenu`: Card-based navigation components
   - `Product`: Product listings
   - `KnowAboutUs`: About us content items
   - `LatestNews`: News articles with active/inactive status
   - `FAQ`: Frequently asked questions
   - `Glance`: Statistical data (title + value)
   - `Announcement`: Announcement content
   - `MediaFile`: Media gallery items

3. **administrator** - Company profile and settings
   - `CompanyProfile`: Company information (title, description, contact, etc.)
   - `SocialLink`: Social media links associated with company profile

4. **accounts** - Authentication
   - Uses `dj-rest-auth` for token-based authentication
   - Endpoints: `/accounts/login/`, `/accounts/logout/`, etc.

### Model Architecture

#### Content Hierarchy
```
Menu → CorePage → Section → Component (various types)
```

1. **Menu**: Top-level navigation items (can appear on footer via `on_footer` flag)
2. **CorePage**: Pages linked to menu items, with slug-based routing
3. **Section**: Divides pages into sections, each with a specific `ComponentType` and position
4. **Components**: Various content types (FAQ, Products, News, etc.) that belong to sections

#### BaseComponentModel
All component models (except `Glance`) inherit from `BaseComponentModel`, providing common fields:
- `title`, `subtitle`, `description`
- `media`: FileField for images/videos
- `url`: Optional external link
- `position`: Display order
- `on_landing`: Flag for landing page display
- `created_on`: Auto-timestamp

### API Architecture

#### URL Structure
```
/admin/                              # Django admin interface
/swagger/                            # Swagger API documentation
/accounts/                           # Authentication endpoints (dj-rest-auth)
/administrator/
  - company-profile/                 # Company information
  - social-link/                     # Social media links
/core/
  - menu/                            # Navigation menus
  - core-page/                       # Pages
  - section/                         # Page sections
  - componenttype/                   # Component types
/component/
  - component-data/                  # Generic component data
  - card-menu/                       # Card menu items
  - products/                        # Product listings
  - know-about-us/                   # About us items
  - latest-news/                     # News articles
  - faq/                             # FAQ items
  - glance/                          # Statistical glances
  - announcements/                   # Announcements
  - media-files/                     # Media gallery
```

#### ViewSets and Permissions

All core and component ViewSets use `ModelViewSet` with custom permissions:

- **IsAdminOrStaffOrReadOnly**: Allows anyone to read (list/retrieve), but only authenticated admin/staff can create/update/delete
- **IsAdminOrStaffOnly**: Requires authentication and admin/staff status for all operations

Serializers use a pattern of having separate Read and Create/Update serializers:
- ReadOnly serializers include nested relationships (e.g., `MenuReadOnlySerializer` includes related pages)
- Create/Update serializers use IDs for foreign keys

#### Authentication

Uses **Token Authentication** via DRF:
- Default authentication class: `TokenAuthentication`
- Default permission class: `IsAuthenticated` (overridden per ViewSet)
- Login via `/accounts/login/` returns a token
- Clients must send: `Authorization: Token <token>` header

### Key Features

#### Auto-generated Slugs
Both `Menu` and `CorePage` models auto-generate unique slugs using `python-slugify` and `uuid4`:
```python
def save(self, *args, **kwargs):
    if not self.slug:
        id = uuid.uuid4()
        self.slug = slugify(str(id))
    super().save(*args, **kwargs)
```

#### Rich Text Editor
`CorePage.content` and `Section.content` use `RichTextField` from django-ckeditor for HTML content editing.

#### Media Files
- **MEDIA_URL**: `/media/`
- **MEDIA_ROOT**: `media` (relative directory)
- Media files are served in DEBUG mode via static file serving

#### CORS Configuration
CORS is fully open (`CORS_ALLOW_ALL_ORIGINS: True`) for development. This should be restricted in production.

#### Filtering
The `MenuView` supports filtering by `on_footer` query parameter:
```
GET /core/menu/?on_footer=true
```

### Database

**Development**: SQLite (`db.sqlite3`)
**Production**: Commented MySQL configuration exists in `settings.py`

### Deployment

#### cPanel Deployment
The project includes `.cpanel.yml` for automated deployment via cPanel Git integration:
- Deploys to: `/home/rmoktvux3m8e/public_html/singdevfpc.in/singdevfpc_backend/`
- Copies all files using `cp -R * $DEPLOYPATH`

#### WSGI Configuration
Production WSGI file: `passenger_wsgi.py` (for Passenger deployments)

#### Branch Structure
- **main**: Production branch
- **test-deployment**: Testing deployment branch (current)
- **develop**: Development branch
- **feature/authentication-api**: Authentication feature branch
- Multiple environment-specific branches (singhdevfpc, badayuni, etc.) suggest multi-tenant deployment

### Important Configuration Notes

#### Security Considerations
⚠️ **The following should be changed before production:**
- `SECRET_KEY` is hardcoded (line 24 in settings.py)
- `DEBUG = True` (should be False in production)
- `ALLOWED_HOSTS = ['*']` (should be restricted)
- CORS allows all origins (should be restricted)

#### Static Files
- **STATIC_URL**: `/static/`
- **STATIC_ROOT**: `/home/rmoktvux3m8e/public_html/singdevfpc.in/static` (production path)

#### Python Version
- Pipfile specifies: `python_version = "3.11"`

### Technology Stack

**Framework**: Django 3.2.11
**API**: Django REST Framework 3.13.1
**Authentication**: dj-rest-auth with Token Authentication
**Documentation**: drf-yasg (Swagger/OpenAPI)
**Rich Text**: django-ckeditor
**CORS**: django-cors-headers 3.11.0
**Filtering**: django-filter 21.1
**Image Processing**: Pillow 7.0.0
**Utilities**: python-slugify 5.0.2

### API Documentation

Swagger UI is available at `/swagger/` endpoint with:
- Title: "FDVRC Hadoti Backend API"
- Description: "REST API for Singdev Mahila Kisan Utpadak Producer Company Limited"
- Public access (no authentication required to view docs)

## Development Patterns

### Adding a New Component Type

1. Create model in `component/models.py` (inherit from `BaseComponentModel`)
2. Create serializers in `component/serializers.py` (Read and Create versions)
3. Create ViewSet in `component/views.py` (use `IsAdminOrStaffOrReadOnly`)
4. Register in `component/urls.py` router
5. Register in `component/admin.py` for Django admin access
6. Create and run migrations
7. Create corresponding `ComponentType` entry in database

### Creating API Endpoints

The project uses DRF's `DefaultRouter` for automatic CRUD endpoint generation:
- `GET /resource/` - List all
- `POST /resource/` - Create new
- `GET /resource/{id}/` - Retrieve one
- `PUT /resource/{id}/` - Full update
- `PATCH /resource/{id}/` - Partial update
- `DELETE /resource/{id}/` - Delete

### Custom Permissions

Custom permission classes in `hadoti_backend/permissions.py`:
- Check `request.user.is_authenticated`, `is_staff`, and `is_superuser`
- Differentiate read vs. write operations via `view.action`
