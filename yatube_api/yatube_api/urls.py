from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from posts.models import Post

def root_view(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Yatube API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
            .endpoint { background: #f8f9fa; margin: 15px 0; padding: 15px; border-left: 4px solid #3498db; border-radius: 4px; }
            .method { background: #27ae60; color: white; padding: 4px 8px; border-radius: 3px; font-weight: bold; margin-right: 10px; }
            .url { font-family: monospace; color: #2c3e50; font-size: 16px; }
            .description { color: #7f8c8d; margin-top: 5px; }
            .example { background: #ecf0f1; padding: 10px; border-radius: 4px; margin-top: 10px; font-family: monospace; font-size: 14px; }
            .posts-example { margin: 20px 0; }
            .post-card { background: #ffffff; border: 1px solid #e1e8ed; border-radius: 12px; padding: 20px; margin: 15px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .post-header { color: #657786; margin-bottom: 10px; font-size: 14px; }
            .post-date { color: #8899a6; }
            .post-content { font-size: 16px; line-height: 1.5; color: #14171a; margin-bottom: 15px; }
            .post-stats { color: #657786; font-size: 14px; }
            .post-stats span { margin-right: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Yatube API</h1>
            <p>Добро пожаловать в API социальной сети Yatube!</p>
            
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="url">/api/v1/posts/</span>
                <div class="description">Получить список всех постов</div>
                <div class="example">curl -H "Authorization: Bearer YOUR_TOKEN" http://127.0.0.1:8000/api/v1/posts/</div>
            </div>

            <div class="endpoint">
                <span class="method">POST</span>
                <span class="url">/api/v1/posts/</span>
                <div class="description">Создать новый пост</div>
                <div class="example">curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"text":"Мой первый пост!"}' http://127.0.0.1:8000/api/v1/posts/</div>
            </div>

            <div class="endpoint">
                <span class="method">GET</span>
                <span class="url">/api/v1/groups/</span>
                <div class="description">Получить список групп</div>
                <div class="example">curl http://127.0.0.1:8000/api/v1/groups/</div>
            </div>

            <div class="endpoint">
                <span class="method">POST</span>
                <span class="url">/api/v1/jwt/create/</span>
                <div class="description">Получить JWT токен для аутентификации</div>
                <div class="example">curl -X POST -H "Content-Type: application/json" -d '{"username":"ivan","password":"pass12345"}' http://127.0.0.1:8000/api/v1/jwt/create/</div>
            </div>

            <div class="endpoint">
                <span class="method">GET</span>
                <span class="url">/api/v1/follow/</span>
                <div class="description">Получить список подписок</div>
                <div class="example">curl -H "Authorization: Bearer YOUR_TOKEN" http://127.0.0.1:8000/api/v1/follow/</div>
            </div>

            <div class="endpoint">
                <span class="method">POST</span>
                <span class="url">/api/v1/posts/{id}/comments/</span>
                <div class="description">Добавить комментарий к посту</div>
                <div class="example">curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"text":"Отличный пост!"}' http://127.0.0.1:8000/api/v1/posts/1/comments/</div>
            </div>

            <h2>📰 Примеры постов:</h2>
            <div class="posts-example">
                <div class="post-card">
                    <div class="post-header">
                        <strong>@ivan</strong> • <span class="post-date">13 октября 2025</span>
                    </div>
                    <div class="post-content">
                        Привет! Это мой первый пост в Yatube API. Теперь можно создавать посты через REST API! 🚀
                    </div>
                    <div class="post-stats">
                        <span>💬 3 комментария</span>
                        <span>❤️ 5 лайков</span>
                    </div>
                </div>

                <div class="post-card">
                    <div class="post-header">
                        <strong>@maria</strong> • <span class="post-date">12 октября 2025</span>
                    </div>
                    <div class="post-content">
                        Изучаю Django REST Framework. Очень мощный инструмент для создания API! 
                        Особенно нравится система сериализаторов и ViewSets.
                    </div>
                    <div class="post-stats">
                        <span>💬 7 комментариев</span>
                        <span>❤️ 12 лайков</span>
                    </div>
                </div>

                <div class="post-card">
                    <div class="post-header">
                        <strong>@alex</strong> • <span class="post-date">11 октября 2025</span>
                    </div>
                    <div class="post-content">
                        Создал новую группу "Программирование"! Присоединяйтесь, если интересуетесь разработкой. 
                        Будем делиться опытом и изучать новые технологии вместе.
                    </div>
                    <div class="post-stats">
                        <span>💬 15 комментариев</span>
                        <span>❤️ 28 лайков</span>
                    </div>
                </div>
            </div>

            <h2>📝 Как начать:</h2>
            <ol>
                <li>Создайте пользователя через админку: <a href="/admin/">/admin/</a></li>
                <li>Получите JWT токен: <code>POST /api/v1/jwt/create/</code></li>
                <li>Используйте токен в заголовке: <code>Authorization: Bearer YOUR_TOKEN</code></li>
            </ol>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', root_view, name='root'),
    path('redoc/', root_view, name='redoc'),  # Дублируем главную страницу для /redoc/
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]