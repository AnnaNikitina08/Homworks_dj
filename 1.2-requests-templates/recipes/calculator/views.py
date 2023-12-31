from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'plov': {
        'мясо, кг': 0.4,
        'рис, кг': 0.2,
        'морковь, кг': 0.2,
        'лук, кг': 0.2

    }
}


def recipe_view(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(recipe_name, {})
    context = {
        'recipe': {ingredient: amount * servings for ingredient, amount in recipe.items()}
    }
    return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
