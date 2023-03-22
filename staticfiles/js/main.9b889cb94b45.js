function toggleIngredients() {
    var ingredients = document.getElementById('ingredients');
    var instructions = document.getElementById('instructions');
  
    ingredients.classList.toggle('d-none');
    instructions.classList.add('d-none');
}
  
function toggleInstructions() {
    var ingredients = document.getElementById('ingredients');
    var instructions = document.getElementById('instructions');

    instructions.classList.toggle('d-none');
    ingredients.classList.add('d-none');
}
  
// Attach event listeners to the buttons
document.getElementById('ingredientsBtn').addEventListener('click', function() {
    toggleIngredients();
});

document.getElementById('instructionsBtn').addEventListener('click', function() {
    toggleInstructions();
});
  