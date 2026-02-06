from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Note, Category
from .forms import NoteForm, CategoryForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


#----------РЕГИСТРАЦИЯ----------
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# 1. Список заметок
class NoteListView(LoginRequiredMixin,ListView):  #Миксины: LoginRequiredMixin защищает страницы от неавторизованных гостей.
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'  # В HTML мы будем обращаться к списку как 'notes'

    def get_queryset(self):
        # ЭТО САМАЯ ВАЖНАЯ ЧАСТЬ!
        # Мы переопределяем стандартный запрос "дай всё".
        # Мы говорим: "Дай только те заметки, где user == текущий пользователь".
        return Note.objects.filter(user=self.request.user).order_by('-created_at')


# 2. Создание заметки
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('index')  # Куда перекинуть после успеха

    def form_valid(self, form):
        # Вот тут происходит магия присвоения автора!
        # Пользователь заполнил форму (Заголовок, Текст), но поле 'user' пустое.
        # Мы говорим: "Владелец этой новой заметки = текущий пользователь".
        form.instance.user = self.request.user
        return super().form_valid(form)


# 3. Редактирование заметки
class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html' # Используем тот же шаблон, что и для создания
    success_url = reverse_lazy('index')
    def get_queryset(self):
        # Разрешаем редактировать только СВОИ задачи
        return Note.objects.filter(user=self.request.user)


# 4. Удаление заметки
class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('index')
    def get_queryset(self):
        # Разрешаем удалять только СВОИ задачи
        return Note.objects.filter(user=self.request.user)


# 5. Создание категории
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('index')