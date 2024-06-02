class Rating {
  constructor() {
    this.element = null;
    this.rating = 0;
  }

  setElement(element) {
    this.element = element;
  }

  setRating(newRating) {
    this.rating = newRating;
    this.updateDisplay();
  }

  updateDisplay() {
    if (this.element) {
      this.element.innerHTML = `Rating: ${this.rating}/5`;
    }
  }
}
