class Review {
  constructor() {
    this.element = null;
    this.review = '';
  }

  setElement(element) {
    this.element = element;
  }

  setReview(newReview) {
    this.review = newReview;
    this.updateDisplay();
  }

  updateDisplay() {
    if (this.element) {
      this.element.innerHTML = `Review: ${this.review}`;
    }
  }
}
