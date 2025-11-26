# Привіт! 👋

Мене звати **[Гордей Михайло]**, я студент ЧНУ ім. Юрія Федьковича на спеціальності **прикладна математика**.  
Моя мета — стати висококваліфікованим DevOps-інженером, який будує надійні, масштабовані та безпечні системи.

---

## 🎯 Мої цілі в DevOps
- 🚀 Опановувати та впроваджувати **CI/CD пайплайни** (GitHub Actions, GitLab CI, Jenkins).
- ☁️ Розвиватися у напрямку **Cloud** (AWS, GCP, Azure).
- 📦 Поглибити знання у **Docker** та **Kubernetes** для контейнеризації та оркестрації.
- 🔐 Практикувати **безпеку** у DevOps (DevSecOps).
- 📊 Вивчати інструменти **моніторингу та логування** (Prometheus, Grafana, ELK stack).

---

## 📈 План розвитку
1. **Основи GitHub**  

2. **Скрипти**

3. **Командна розробка веб-додатків**

4. **Контеризація**  

5. **Розподілений деплой мікросервісів на PaaS**  

6. **Автоматизація інфраструктури з IaC**

7. **Моніторинг та логування**

8. **Security**
---

## Посилання на проєкт
[https://github.com/users/MiGer4/projects/1]

## Скріншот бота
<img width="697" height="401" alt="image" src="https://github.com/user-attachments/assets/9fa19b3f-c9c0-4f17-918e-67aecd0e3275" />

---

## 📬 Контакти
- 📧 Email: [mykhailo.hordei.w@gmail.com]
  
⭐️ Дякую, що завітали до мого профілю! Буду радий новим контактам та співпраці.

---https://github.com/MiGer4/devops-portfolio/tree/lab2

# Лабораторна робота №2

## Скріншоти гіт команд
<img width="1266" height="705" alt="image" src="https://github.com/user-attachments/assets/45506037-d053-482f-8b68-e1c708f14c7a" />

---

## Запуск скриптів

1. **api_monitoring.py**  
   ```sh
   python api_monitoring.py --endpoints endp1,endp2 --format [json|csv] --file output.json
   ```
   - `--endpoints` — список API-ендпоінтів через кому  
   - `--format` — формат результату: json або csv  
   - `--file` — ім'я вихідного файлу (необов'язково)

2. **log_parcser.py**  
   ```sh
   python log_parcser.py -f /var/log/nginx/access.log -o report.html --top 20
   ```
   - `-f` або `--file` — шлях до access.log  
   - `-o` або `--output` — файл для HTML-звіту  
   - `--top` — кількість топ IP/User-Agent

3. **move_to_dir.go**  
   ```sh
   go run move_to_dir.go [flags]
   ```
   **Прапорці:**
   - `-source` — директорія для пошуку файлів (за замовчуванням: поточна `.`)
   - `-dest` — директорія, куди переміщати файли (за замовчуванням: `./organized`)
   - `-ext` — розширення файлів для пошуку (за замовчуванням: `.txt`)
   - `-no-recursive` — не шукати у піддиректоріях (тільки у кореневій директорії)

   **Приклад запуску:**
   ```sh
   go run move_to_dir.go -source ./data -dest ./organized -ext .log -no-recursive
   ```
