# Базовый образ с Node.js
FROM node:18-alpine

# Рабочая директория
WORKDIR /app

# Копируем файлы зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь проект
COPY . .

# Сборка проекта
RUN npm run build

# Запуск приложения
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]