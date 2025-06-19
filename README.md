# 📌 Проект "Менеджер задач"

---

<details>
<summary><strong>📋 Условие и инструкция | Часть 1</strong></summary>

### 🎯 Цель проекта

- Создать структуру Менеджера Задач и реализовать:
  - Разработку моделей: `Task`, `SubTask`, `Category`
  - Настройку административной панели
  - Подключение базы данных (MySQL)
  - Создание миграций и объектов через Django admin
  - Настройку метаданных моделей и методов `__str__`

---

### 🛠️ Реализовать модели

#### 📌 Модель `Task`

Описание: Задача для выполнения.

**Поля:**
- `title`: Название задачи (уникально для даты)
- `description`: Описание задачи
- `categories`: Категории задачи (ManyToMany)
- `status`: Статус задачи (`New`, `In progress`, `Pending`, `Blocked`, `Done`)
- `deadline`: Дата и время дедлайна
- `created_at`: Дата и время создания (автоматически)

#### 📌 Модель `SubTask`

Описание: Отдельная часть основной задачи (`Task`).

**Поля:**
- `title`: Название подзадачи
- `description`: Описание подзадачи
- `task`: Ссылка на `Task` (ForeignKey)
- `status`: Статус задачи (`New`, `In progress`, `Pending`, `Blocked`, `Done`)
- `deadline`: Дата и время дедлайна
- `created_at`: Дата и время создания (автоматически)

#### 📌 Модель `Category`

Описание: Категория выполнения.

**Поля:**
- `name`: Название категории

---

### 🔧 Шаги для выполнения:

1. Создайте модели в `models.py`
2. Создайте и примените миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
3. Зарегистрируйте модели в `admin.py`
4. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
5. Зайдите в Django admin и добавьте объекты
6. Зафиксируйте изменения в Git (commit + push)
7. Приложите ссылку на репозиторий и скриншоты в ответе

</details>

---

<details>
<summary><strong>📋 Условие и инструкция | Часть 2</strong></summary>

### 🎯 Цель проекта

- Добавить строковое представление (`__str__`) и метаданные (`Meta`) к моделям
- Настроить административную панель для удобства управления

---

### ⚙️ Изменения в моделях

#### ✅ `Task`:
- `__str__`: возвращает `title`
- `Meta`:
  - `db_table`: `'task_manager_task'`
  - `ordering`: `['-created_at']`
  - `verbose_name`: `'Task'`
  - `unique_together`: `['title']`

#### ✅ `SubTask`:
- `__str__`: возвращает `title`
- `Meta`:
  - `db_table`: `'task_manager_subtask'`
  - `ordering`: `['-created_at']`
  - `verbose_name`: `'SubTask'`
  - `unique_together`: `['title']`

#### ✅ `Category`:
- `__str__`: возвращает `name`
- `Meta`:
  - `db_table`: `'task_manager_category'`
  - `verbose_name`: `'Category'`
  - `unique_together`: `['name']`

---

### 🛠️ Настройка Django Admin

В `admin.py` добавлены кастомные классы:
- `TaskAdmin`
- `SubTaskAdmin`
- `CategoryAdmin`

---

### 💾 Миграции и запуск

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

🔗 Перейти в Django Admin:
http://127.0.0.1:8000/admin/
```

</details>

---

<details>
<summary><strong>📋 Условие и инструкция | Часть 3 — CRUD</strong></summary>

### 🎯 Цель

Освоение основных операций **CRUD** (_Create, Read, Update, Delete_) на примере заданных моделей.

---

### 🛠️ Выполните запросы

#### 📌 Создание записей

✅ **Task**
- `title`: `"Prepare presentation"`
- `description`: `"Prepare materials and slides for the presentation"`
- `status`: `"New"`
- `deadline`: `today + 3 days`

✅ **SubTasks** для `"Prepare presentation"`:

1. **SubTask 1**
   - `title`: `"Gather information"`
   - `description`: `"Find necessary information for the presentation"`
   - `status`: `"New"`
   - `deadline`: `today + 2 days`

2. **SubTask 2**
   - `title`: `"Create slides"`
   - `description`: `"Create presentation slides"`
   - `status`: `"New"`
   - `deadline`: `today + 1 day`

---

#### 📖 Чтение записей

🔍 **Tasks со статусом `"New"`**
- Найти все задачи, где `status == "New"`

🔍 **SubTasks с просроченным статусом `"Done"`**
- Найти все подзадачи, где `status == "Done"` и `deadline < текущая дата`

---

#### ✏️ Изменение записей

1. Обновите статус задачи `"Prepare presentation"` на `"In progress"`
2. Измените `deadline` у `"Gather information"` на **два дня назад**
3. Обновите `description` у `"Create slides"`:
   > `"Create and format presentation slides"`

---

#### 🗑️ Удаление записей

- Удалите задачу `"Prepare presentation"` вместе со всеми её подзадачами

</details>
