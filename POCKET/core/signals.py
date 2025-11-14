import json
import random
import string
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mitarbeiter

PASSWORD_FILE = "passwords.json"

def load_passwords():
    """Loads JSON file. If it doesnn´t exist, it creates an empty structure."""
    try:
        with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": {}}

def save_passwords(passwords):
    """it saves the user info in JSON file."""
    with open(PASSWORD_FILE, "w", encoding="utf-8") as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)

def generate_unique_username(vorname, nachname):
    """ It creates username: connects the names with '-', uses '.' by surname. """
    base_username = f"{vorname.replace(' ', '-').lower()}.{nachname.lower()}"
    username = base_username
    counter = 1

    while User.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1

    return username

def generate_custom_password(vorname, nachname):
    """ Generates a password in a special format for the user: 2 letter name + 2 letter surname + symbol + 3 numbers """
    symbol = random.choice("!@#$%^&*")
    numbers = ''.join(random.choices(string.digits, k=3))
    password = f"{vorname.replace(' ', '')[:2].lower()}{nachname[:2].lower()}{symbol}{numbers}"
    return password

@receiver(post_save, sender=Mitarbeiter)
def create_user_for_mitarbeiter(sender, instance, created, **kwargs):
    """ Automatically creates a user and password when a new employee is created. """
    passwords = load_passwords()

    if created and not instance.user:
        username = generate_unique_username(instance.vorname, instance.nachname)
        raw_password = generate_custom_password(instance.vorname, instance.nachname)

        user = User.objects.create(username=username)
        user.set_password(raw_password)  # Stores the password using Django's own hashing system
        user.save()

        instance.user = user
        instance.save()

        group = Group.objects.get(name=instance.rolle)
        user.groups.add(group)

        # 🔹 Save only the INITIAL PASSWORD GENERATED to the JSON file
        passwords["users"][username] = {
            "password_plain": raw_password,  # Only the first password generated is saved
            "created_at": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
        }

        save_passwords(passwords)

        print(f"Username '{username}' has been generated. First password: {raw_password}")
