def parse_recipes(recipieList):
    recipe_string = ""
    for recipeDict in recipieList:
        name = recipeDict["name"]
        ingredients = recipeDict["ingredients"]
        time = recipeDict["time"]
        recipe_string += f"{name},\r\n Ingredients: {ingredients}, \r\nReady in {time} minuets\r\r"
    return recipe_string


class User:

    def __init__(self):
        self.id = None
        self.firstName = None
        self.lastName = None
        self.recipie = {}
        self.recipes = []

    def show_data(self):
        user_data = f"{self.firstName} {self.lastName}, Recipes: {parse_recipes(self.recipes)}  "
        return user_data
