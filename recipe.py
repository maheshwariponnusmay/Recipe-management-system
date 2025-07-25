import json
import os

# 📁 JSON file to store recipes
DATA_FILE = 'recipes.json'

# 📦 Load existing recipes
def load_recipes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# 💾 Save updated recipes
def save_recipes(recipes):
    with open(DATA_FILE, 'w') as file:
        json.dump(recipes, file, indent=4)

# ➕ Add a recipe
def add_recipe():
    print("\n👨‍🍳 Add a New Recipe")
    name = input("🍽️ Enter recipe name: ")
    ingredients = input("🧂 Enter ingredients (comma-separated): ").split(',')
    instructions = input("📜 Enter instructions: ")

    recipe = {
        'name': name.strip(),
        'ingredients': [i.strip() for i in ingredients],
        'instructions': instructions.strip()
    }

    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print("✅ Recipe added successfully!\n")

# 📖 View all recipes
def view_recipes():
    print("\n📚 All Recipes")
    recipes = load_recipes()
    if not recipes:
        print("⚠️ No recipes found.")
        return

    for i, recipe in enumerate(recipes, 1):
        print(f"\n🔹 Recipe {i}: {recipe['name']}")
        print(f"   🧾 Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"   📝 Instructions: {recipe['instructions']}")

# 🔍 Search by recipe name
def search_by_name():
    name = input("🔎 Enter recipe name: ").strip().lower()
    recipes = load_recipes()
    found = False

    for recipe in recipes:
        if recipe['name'].lower() == name:
            print(f"\n✅ Found: {recipe['name']}")
            print(f"   🧾 Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"   📝 Instructions: {recipe['instructions']}")
            found = True
            break

    if not found:
        print("❌ Recipe not found.")

# 🔍 Search by ingredient
def search_by_ingredient():
    ingredient = input("🧂 Enter ingredient to search: ").strip().lower()
    recipes = load_recipes()
    found = False

    print(f"\n🔍 Recipes with ingredient '{ingredient}':")
    for recipe in recipes:
        if any(ingredient in ing.lower() for ing in recipe['ingredients']):
            print(f"✅ {recipe['name']}")
            print(f"   🧾 Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"   📝 Instructions: {recipe['instructions']}\n")
            found = True

    if not found:
        print("❌ No recipes contain that ingredient.")

# 🗑️ Delete a recipe
def delete_recipe():
    name = input("🗑️ Enter recipe name to delete: ").strip().lower()
    recipes = load_recipes()
    updated = [r for r in recipes if r['name'].lower() != name]

    if len(updated) == len(recipes):
        print("❌ Recipe not found.")
    else:
        save_recipes(updated)
        print("🧹 Recipe deleted successfully.")

# 📋 Main Menu
def main():
    while True:
        print("\n🍴 Recipe Management System")
        print("1️⃣ Add Recipe")
        print("2️⃣ View All Recipes")
        print("3️⃣ Search by Name")
        print("4️⃣ Search by Ingredient")
        print("5️⃣ Delete Recipe")
        print("6️⃣ Exit")

        choice = input("👉 Choose an option (1-6): ")

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_by_name()
        elif choice == '4':
            search_by_ingredient()
        elif choice == '5':
            delete_recipe()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == '__main__':
    main()
