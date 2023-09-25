from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment
 
# напишем уже знакомую нам функцию удаления статей
def delete_all_posts(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)
delete_all_posts.short_description = 'Удалить все статьи' # описание для более понятного представления в админ панеле задаётся, как будто это объект
 
# создаём новый класс для представления постов в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'author', 'rating', 'dateCreation') # оставляем только имя и цену товара
    list_filter = ('author', 'rating', 'dateCreation') # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'author') # тут всё очень похоже на фильтры из запросов в базу
    actions = [delete_all_posts] # добавляем действия в список


# создаём новый класс для представления авторов в админке
class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с авторами
    list_display = ('authorUser', 'ratingAuthor') 
    list_filter = ('authorUser', 'ratingAuthor') # добавляем примитивные фильтры в нашу админку
    search_fields = ('authorUser', 'ratingAuthor') # тут всё очень похоже на фильтры из запросов в базу

# напишем функцию удаления коментариев
def delete_all_comments(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)
delete_all_comments.short_description = 'Удалить все коментарии' # описание для более понятного представления в админ панеле задаётся, как будто это объект
 

# создаём новый класс для представления коментариев в админке
class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с коментариями
    list_display = ('commentUser', 'text', 'dateCreation', 'rating') 
    list_filter = ('commentUser', 'rating', 'dateCreation') # добавляем примитивные фильтры в нашу админку
    search_fields = ('commentPost', 'commentUser') # тут всё очень похоже на фильтры из запросов в базу
    actions = [delete_all_comments] # добавляем действия в список
    


# Register your models here.


 
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)

