document.getElementById('searchButton').addEventListener('click', function() {
  var ingredient = document.getElementById('ingredientInput').value;
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/search', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      displayRecipes(response.recipes);
    }
  };
  xhr.send(JSON.stringify({ ingredient: ingredient }));
});

function displayRecipes(recipes) {
  var resultsContainer = document.getElementById('resultsContainer');
  resultsContainer.innerHTML = '';
  if (recipes.length > 0) {
      for (var i = 0; i < recipes.length; i++) {
          var recipe = recipes[i].recipe;
          var recipeDiv = document.createElement('div');
          recipeDiv.className = 'recipe';
          var title = document.createElement('h3');
          title.textContent = recipe.label;
          recipeDiv.appendChild(title);
          var image = document.createElement('img');
          image.src = recipe.image;
          recipeDiv.appendChild(image);
          var ingredients = document.createElement('p');
          ingredients.textContent = 'Ingredients: ' + recipe.ingredientLines.join(', ');
          recipeDiv.appendChild(ingredients);
          resultsContainer.appendChild(recipeDiv);
      }
  } 
  
  else {
      var noRecipes = document.createElement('p');
      noRecipes.textContent = 'No recipes found.';
      resultsContainer.appendChild(noRecipes);
  }
}
document.getElementById('sidebarToggle').addEventListener('click', function() {
  document.getElementById('sidebar').classList.toggle('open');
});

document.getElementById('sidebarClose').addEventListener('click', function() {
  document.getElementById('sidebar').classList.remove('open');
});
