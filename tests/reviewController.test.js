const Review = require('../public/javascripts/review');

describe('ReviewController', () => {
  let reviewController;
  let reviewElement;

  beforeEach(() => {
    reviewElement = document.createElement('div');
    reviewController = new ReviewController(reviewElement);
  });

  it('should set and display the review', () => {
    reviewController.setReview('Great product!');
    expect(reviewElement.innerHTML).toEqual('Review: Great product!');
  });

  it('should update the display when the review changes', () => {
    reviewController.setReview('Great product!');
    reviewController.setReview('Awful product.');
    expect(reviewElement.innerHTML).toEqual('Review: Awful product.');
  });
});
